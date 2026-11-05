# -*- coding: utf-8 -*-
"""Собирает публичный сайт site/ из case/tree.html и реестров дела.

Живые люди попадают на древо только именем и степенью родства:
их карточки, даты и документы не публикуются.
"""
import csv, html, json, os, re, shutil, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CASE = os.path.join(ROOT, 'case')
SITE = os.path.join(ROOT, 'site')

LIVING = {'nastya', 'igor', 'irina', 'viktor', 'larisa', 'galina'}
LIVING_REL = {'nastya': 'Настя', 'igor': 'отец', 'irina': 'мать', 'viktor': 'дед по отцу', 'larisa': 'бабушка по отцу',
              'galina': 'бабушка по матери'}
LIVING_SIB = {'s-gennadiy', 's-sofya', 's-zsibs'}
LIVING_CARDS = {'gennadiy', 'sofya'}
PIDS = {
    'nastya': 'P-0001', 'igor': 'P-0002', 'irina': 'P-0003', 'viktor': 'P-0011', 'larisa': 'P-0006', 'ivan': 'P-0004',
    'galina': 'P-0005', 'nikolay': 'P-0008', 'elvira': 'P-0010;P-0009', 'fedor': 'P-0023;P-0025;P-0066', 'elena': 'P-0045', 'pavel': 'P-0012;P-0043',
    'fekla': 'P-0021', 'egor': 'P-0014;P-0019;P-0028;P-0036;P-0037;P-0063;P-0064;P-0065', 'natalyaa': 'P-0015', 'sofyash': 'P-0020', 'evsevy': 'P-0053', 'elisav': 'P-0054',
    'nikolsh': 'P-0050;P-0055;P-0056;P-0057;P-0058;P-0059', 'varvara': 'P-0051', 'ignat': 'P-0060', 'feodora': 'P-0061', 'daniil': 'P-0062', 'pyotr': 'P-0016;P-0029;P-0030;P-0031',
    'natyak': 'P-0017', 'andrey': 'P-0032;P-0038', 'mavra': 'P-0033', 'efim': 'P-0034', 'yakov': 'P-0039', 'evfimia': 'P-0040',
    'fsimeon': 'P-0042',
}
PUBLIC_IMG_DIRS = ('inputs/yandex-archive/', 'inputs/pamyat-naroda/', 'inputs/familysearch/', 'inputs/obd/')
LEAKS = ('22.11.1995', '15.06.1962', '6.02.1944', '06.02.1944', 'nastya-message', 'nastya-answers')
SCRUB = [
    (r'<p class="src">[^<]*(Сообщени|Михаил|Telegram)[^<]*</p>', ''),
    (r'\s*Книг ЗАГС Фастова за 1949 год и позже онлайн нет, поэтому запись о рождении Лидии \(если 1949–50\) — только в Фастовском ДРАЦС\.', ''),
]
DROP_LI = re.compile(r'<li>(?:(?!</li>).)*?(nastya-|Telegram|Год рождения Галины|Ирина Ивановна называет)(?:(?!</li>).)*?</li>', re.S)
FALLBACK = {'natyak': 'pyotr'}
SCANS = {
    'egor': ['inputs/yandex-archive/cgam-203-780-697-scan141-georgiy-1888.png'],
    'nikolay': ['inputs/yandex-archive/cgamo-252-1-317-scan117-komarov-nikolay-1923.png', 'inputs/yandex-archive/cgamo-252-1-317-scan117-parents.png',
                'inputs/pamyat-naroda/komarov-ne-1923-nagradnoy-list-full.jpg', 'inputs/pamyat-naroda/komarov-ne-1923-nagradnoy-list-top.png'],
    'elvira': ['inputs/pamyat-naroda/shutiss-elvira-demob-1946-row.png', 'inputs/pamyat-naroda/shutiss-elvira-demob-1946-date.png'],
}


def scrub(s):
    for pat, rep in SCRUB:
        s = re.sub(pat, rep, s)
    return s


def section(t, cls, end):
    m = re.search(r'<section class="%s"[^>]*>(.*?)</section>\s*%s' % (cls, end), t, re.S)
    s = re.sub(r'<h2[^>]*>.*?</h2>', '', m.group(1))
    return DROP_LI.sub('', s).replace('<code>~/kinship-cases/komarova/</code>', '<a href="https://github.com/sokomishalov/komarova-genealogy">репозитории</a>')


def main():
    t = open(os.path.join(CASE, 'tree.html'), encoding='utf-8').read()
    nodes = []
    for m in re.finditer(r'\{ id: "(\w+)",\s*g:\s*(\d+), x:\s*(-?\d+),\s*n: "([^"]*)", s: "([^"]*)", st: "(\w+)"(?:, c: "(\w+)")?(, unk: 1)?', t):
        nid, g, x, n, s, st, c, unk = m.groups()
        nodes.append(dict(id=nid, g=int(g), x=int(x), n=n, s=s, st=st, c=c, unk=bool(unk)))
    sib = {}
    for m in re.finditer(r'\{ id: "([\w-]+)",\s*sib: "(\w+)",\s*x:\s*-?\d+,\s*n: "([^"]*)", s: "([^"]*)", st: "(\w+)", to: "(\w+)" \}', t):
        sid, of, n, s, st, to = m.groups()
        living = sid in LIVING_SIB
        sib.setdefault(of, []).append(dict(n=n, d='' if living else n + ' — ' + s, st='living' if living else st, to=to))
    target = dict(re.findall(r'(\w+): "(\w+)"', re.search(r'const target = \{(.*?)\};', t).group(1)))
    cards = {}
    for m in re.finditer(r'<details class="person s-(\w+)" id="(\w+)"><summary>(.*?)</summary><div class="pbody">(.*?)</div></details>', t, re.S):
        st, cid, summ, body = m.groups()
        pname = re.search(r'<span class="pname">(.*?)</span>', summ)
        pyrs = re.search(r'<span class="pyrs">(.*?)</span>', summ)
        cards[cid] = dict(name=html.unescape(re.sub('<.*?>', '', pname.group(1))) if pname else '',
                          years=html.unescape(re.sub('<.*?>', '', pyrs.group(1))) if pyrs else '', body=scrub(body))
    gaps = section(t, 'gaps', r'<section class="sources"')
    srcs = section(t, 'sources', r'</div>\s*<script')

    arts = list(csv.DictReader(open(os.path.join(CASE, 'artifact-register.csv'), encoding='utf-8')))
    os.makedirs(SITE, exist_ok=True)
    scans_dir = os.path.join(SITE, 'scans')
    shutil.rmtree(scans_dir, ignore_errors=True)
    os.makedirs(scans_dir)
    ids = {n['id'] for n in nodes}
    by_id = {n['id']: n for n in nodes}
    out = []
    for n in nodes:
        living = n['id'] in LIVING
        card = cards.get(n['id'])
        body = card['body'] if card else ''
        if not card and not living:
            tg = target.get(n['id']) or FALLBACK.get(n['id'])
            if tg and tg in by_id:
                body = f'<p>Подробности — в общей карточке: <button type="button" data-go="{tg}">{html.escape(by_id[tg]["n"])}</button></p>'
        if not living:
            seen = set()
            for s in sib.get(n['id'], []):
                to = s['to']
                if to in ids or to in LIVING_CARDS or to in seen or to not in cards:
                    continue
                seen.add(to)
                body += f'<h4>{html.escape(cards[to]["name"])}</h4>' + cards[to]['body']
        docs = []
        if not living and n['id'] in PIDS:
            pids = PIDS[n['id']].split(';')
            for a in arts:
                if not any(p in a['person_ids'].split(';') for p in pids):
                    continue
                if a['source_type'].startswith('family') or a['status'] == 'rejected':
                    continue
                parts = [p.strip() for p in re.split(r'\s*;\s*', a['source_url_or_path'])]
                urls = [p for p in parts if p.startswith('http')]
                imgs = []
                for p in parts:
                    for q in [s.strip() for s in p.split(',')]:
                        if q.startswith(PUBLIC_IMG_DIRS) and re.search(r'\.(png|jpe?g)$', q, re.I):
                            src = os.path.join(CASE, q)
                            if os.path.isfile(src):
                                shutil.copy(src, os.path.join(scans_dir, os.path.basename(q)))
                                imgs.append('scans/' + os.path.basename(q))
                docs.append(dict(id=a['artifact_id'], t=a['source_title'], ref=a['archival_reference'] or a['repository_or_archive'],
                                 d=a['record_date'], url=urls[0] if urls else '', imgs=imgs))
        imgs = []
        for q in SCANS.get(n['id'], []):
            shutil.copy(os.path.join(CASE, q), os.path.join(scans_dir, os.path.basename(q)))
            imgs.append('scans/' + os.path.basename(q))
        if imgs:
            docs.insert(0, dict(id='SCANS', t='Сохранённые сканы документов', ref='ЦГА Москвы, ЦГАМО, ЦАМО', d='', url='', imgs=imgs))
        sibs = [dict(n=s['n'], d=s['d'], st=s['st']) for s in sib.get(n['id'], [])]
        out.append(dict(id=n['id'], g=n['g'], x=n['x'], n=n['n'], s=LIVING_REL[n['id']] if living else n['s'],
                        st='living' if living else n['st'], c=n['c'], unk=n['unk'],
                        name=(card or {}).get('name') or n['n'], years='' if living else (card or {}).get('years', ''),
                        body='' if living else body, docs=docs, sibs=sibs))
    data = dict(nodes=out, gaps=gaps, sources=srcs)
    tpl = open(os.path.join(ROOT, 'tools', 'site_template.html'), encoding='utf-8').read()
    page = tpl.replace('/*__DATA__*/null', json.dumps(data, ensure_ascii=False).replace('</', '<\\/'))
    open(os.path.join(SITE, 'index.html'), 'w', encoding='utf-8').write(page)
    open(os.path.join(SITE, '.nojekyll'), 'w').close()
    leaks = [w for w in LEAKS if w in page]
    print('nodes', len(out), 'docs', sum(len(o['docs']) for o in out), 'scans', len(os.listdir(scans_dir)), 'leaks', leaks)
    if leaks:
        sys.exit(1)


if __name__ == '__main__':
    main()
