import csv,os
D=os.path.expanduser('~/kinship-cases/komarova')
def rw(n,fn):
    p=f'{D}/{n}'
    with open(p,newline='',encoding='utf-8') as f: r=list(csv.DictReader(f)); hdr=list(r[0].keys())
    fn(r)
    with open(p,'w',newline='',encoding='utf-8') as f: w=csv.DictWriter(f,fieldnames=hdr); w.writeheader(); w.writerows(r)
def a(rows):
    for r in rows:
        if r['artifact_id']=='A-0079':
            r.update(source_title='МК 1903, ч.2 (браки), май: Василий Васильев Крайнов (19, сын Василия Дмитриева, д. Оладьина, 1-м браком) × девица Анна Петрова Комарова (17 л. 10 мес. 21 дн.), дочь крестьянина д. Телешова Петра Андреева Комарова',
              source_url_or_path='https://yandex.ru/archive/catalog/5ba23318-e5d3-4c7e-80d1-e27095e80652/177',record_date='1903-05 (каталог 1903; OCR-заголовок «1907» ошибочен)',
              names_as_written='Василій Василіевъ Крайновъ; Анна Петрова Комарова; Петръ Андреевъ Комаровъ; поручители по невесте Егоръ Алексіевъ Шиленковъ (д. Нестерцево) и Ѳеодоръ Петровъ Комаровъ (д. Телешова); по жениху Василій Ивановъ Мухановъ, Сѵмеонъ Василіевъ Крайновъ',
              summary='отец невесты — Пётр Андреев Комаров (по образу); поручитель по невесте — её брат Фёдор Петров Комаров (по расшифровке)',
              provenance_level='archival-scan',directness='direct',originality='original-scan',independence_group='IG-CGAM-203-780-3340',legibility='good',access_notes='графа невесты сверена по образу 02.11; поручители — по расшифровке',status='verified')
def p(rows):
    for r in rows:
        if r['person_id']=='P-0065': r['notes']+=' | род. ~1884 (19 в 1903), сын Василия Дмитриева Крайнова'
        if r['person_id']=='P-0028': r['candidate_status']='confirmed'
def c(rows):
    for r in rows:
        if r['claim_id']=='C-0025':
            r['supporting_independence_groups']+=';IG-CGAM-203-780-3340'
            r['rationale']+=' | 02.11: брак 1903 (образ): Анна — дочь Петра Андреева; Фёдор Петров Комаров — поручитель по невесте. Три записи 1903–1904 связывают Фёдора с Анной и Крайновым'
            r['next_action']='брак Фёдора и Марии ~1903–04'
def rel(rows):
    for r in rows:
        if r['relationship_id']=='R-0036': r.update(supporting_artifact_ids='A-0079;A-0077',independence_groups='IG-CGAM-203-780-3340;IG-CGAM-203-780-3359',confidence='high',rationale='запись о браке 1903, сверена по образу')
def s(rows):
    rows.append(dict(zip(rows[0].keys(),['S-0098','2026-11-02','P-0028;P-0019;P-0065','отец невесты в браке 1903','203-780-3340 ск.177','ru','yandex.ru/archive','','found','A-0079','','0','брак Фёдора и Марии'])))
rw('artifact-register.csv',a); rw('person-register.csv',p); rw('claims-register.csv',c); rw('relationship-register.csv',rel); rw('search-log.csv',s)
t=f'{D}/tree.html'; h=open(t,encoding='utf-8').read()
old='Крёстный — Василий Васильевич Крайнов из Оладьина, муж Анны Петровны Комаровой (сестры Фёдора, брак 1903), а сам Фёдор крестил детей Крайновых.'
new='Крёстный — Василий Васильевич Крайнов из Оладьина, муж Анны Петровны Комаровой. В записи их брака (май 1903, ЦГА Москвы 203-780-3340, скан 177, сверено по изображению) невеста названа дочерью «деревни Телешова Петра Андреева Комарова», а поручителем с её стороны записан Фёдор Петров Комаров. Позже Фёдор сам крестил детей Крайновых.'
assert old in h; h=h.replace(old,new); open(t,'w',encoding='utf-8').write(h)
with open(f'{D}/research-state.md','a',encoding='utf-8') as f: f.write('\n- 02.11 ✔ A-0079 брак 1903 (203-780-3340 ск.177, образ): Анна — дочь Петра Андреева Комарова; поручитель по невесте Фёдор Петров Комаров → C-0025 сильно укреплён.\n')
print('ok')
