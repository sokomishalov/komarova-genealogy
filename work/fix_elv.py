# -*- coding: utf-8 -*-
import csv, os
os.chdir(os.path.expanduser('~/kinship-cases/komarova'))
rows = list(csv.reader(open('person-register.csv', encoding='utf-8')))
for r in rows:
    if r[0] == 'P-0010':
        r[1] = 'Шутис(с) Эльвина (ранее ошибочно «Эвелина»)'
        r[3] = 'Шутис Эльвина; Комарова Эльвина (Ваганьковское, 1925–1990)?'
        r[9] = 'сестра Эльвиры'
        r[12] = 'A-0001;A-0016;A-0064'
        r[14] = '2.11.2026 семья: сестёр звали Эльвира и Эльвина, «Эвелины не было». Кто из двух — мать Ларисы и Софьи, уточняется: «Комарова Эльвина 1925–1990» на Ваганьковском носит фамилию Комарова → возможно, мать — Эльвина'
for r in rows:
    if r[0] == 'P-0009':
        r[14] = 'ПН: Шутисс Эльвира Иосифовна 1926, сержант (A-0007) — Эльвира; чья она мать — уточнить (см. P-0010)'
csv.writer(open('person-register.csv', 'w', newline='', encoding='utf-8')).writerows(rows)
with open('artifact-register.csv', 'a', newline='', encoding='utf-8') as fh:
    csv.writer(fh).writerow(['A-0064', '2026-11-02', 'Сообщение Михаила: «Эвелины не было, есть Эльвира и Эльвина, мы немного перепутали все»', 'chat 2026-11-02', 'family-statement', '', '', '2026-11-02', '', 'ru-Cyrl', 'P-0009;P-0010', 'Эльвира; Эльвина', 'исправление семьи: сёстры — Эльвира и Эльвина', 'family-memory', 'direct', 'original', 'IG-FAM-NASTYA', 'good', '', '', 'C-0001;C-0005', 'кто из сестёр — мать, не сказано', 'active'])
print('ok')
