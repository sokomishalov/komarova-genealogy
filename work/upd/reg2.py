import csv,os
D=os.path.expanduser('~/kinship-cases/komarova/')
def load(f):
    with open(D+f,newline='') as h: rows=list(csv.DictReader(h))
    with open(D+f,newline='') as h: hdr=next(csv.reader(h))
    return hdr,rows
def save(f,hdr,rows):
    with open(D+f,'w',newline='') as h: w=csv.DictWriter(h,fieldnames=hdr); w.writeheader(); w.writerows(rows)
def add(hdr,rows,**kw):
    assert not any(r[hdr[0]]==kw[hdr[0]] for r in rows); rows.append({k:kw.get(k,'') for k in hdr})
h,A=load('artifact-register.csv')
add(h,A,artifact_id='A-0070',captured_at='2026-11-02',source_title='ОБД: Шарабарин Лаврентий Тимофеевич — донесение Орехово-Зуевского ГВК 27.08.1946',source_url_or_path='https://obd-memorial.ru/html/info.htm?id=57820422',source_type='military-record',repository_or_archive='ЦАМО / ОБД Мемориал',archival_reference='ЦАМО 58-18004-439, образ 6',record_date='1946-08-27',place_as_written='Курская обл., Дмитров[ский] р-н, с. Поле-Пробужд[ение]; Орехово-Зуево',language_script='ru-Cyrl',person_ids='P-0055',names_as_written='Шарабарин Лаврентий Тимофеевич; жена Шарабарина Агрип. Мак.',summary='уроженец с. Прабожье Поле Дмитриевского у.; призван 08.07.1941 Орехово-Зуевским ГВК; пропал без вести 12.1941; жена Агриппина — Орехово-Зуево',provenance_level='archival-scan',directness='direct',originality='original-scan',independence_group='IG-OBD-SHARABARIN',legibility='good',related_claim_ids='C-0019',reliability_notes='родство с Николаем Тимофеевичем не доказано',status='lead')
add(h,A,artifact_id='A-0071',captured_at='2026-11-02',source_title='ОБД: Шарабарины из Дмитриевского р-на (Ясная Поляна Фатеевского с/с, Пробожье)',source_url_or_path='agent-reports/sharabarina.md §1',source_type='index',repository_or_archive='ОБД Мемориал',record_date='1941–1945',place_as_written='Курская обл., Дмитриевский р-н, Фатеевский с/с, п. Ясная Поляна',language_script='ru-Cyrl',names_as_written='Иван Радионович 1922; Александр Кузьмич 1912; Василий Иванович 1920',summary='гнездо Шарабариных — Ясная Поляна / Прабожье Дмитриевского р-на Курской обл. ⇒ «Дмитровский» = Дмитриевский',provenance_level='index',directness='indirect',originality='derivative',independence_group='IG-OBD-SHARABARIN',legibility='good',status='context')
save('artifact-register.csv',h,A)
h,P=load('person-register.csv')
for r in P:
    if r['person_id']=='P-0021':
        r['places']='с. Ясная Поляна / Прабожье Поле Дмитриевского р-на (у.) Курской обл. → Орехово-Зуево (1943) → Харьковская обл. (1944) → Фастов (похоронена)'
        r['historical_jurisdictions']='«Дмитровский» в семье = почти наверняка Дмитриевский р-н/у. Курской обл. (ОБД: Шарабарины из п. Ясная Поляна Фатеевского с/с)'
        r['source_artifact_ids']+=';A-0071'
add(h,P,person_id='P-0055',preferred_label='Шарабарин Лаврентий Тимофеевич',living_status='deceased',names_as_written='Шарабарин Лаврентий Тимофеевич',death_estimate='пропал без вести 12.1941',places='с. Прабожье Поле Дмитриевского у. → Орехово-Зуево',relatives_as_reported='жена Агриппина Мак.',occupation_or_status='рядовой',source_artifact_ids='A-0070',candidate_status='hypothesis',merge_or_split_rationale='вероятный брат Николая Тимофеевича (отчество + село + Орехово-Зуево)',notes='дядя Фёклы?')
add(h,P,person_id='P-0056',preferred_label='Шарабарин Фрол Николаевич (1912)',living_status='unknown',names_as_written='Шарабарин Фрол Николаевич',birth_estimate='1912',occupation_or_status='капитан; Красная Звезда, ОВ I ст.',source_artifact_ids='',candidate_status='lead',notes='кандидат в братья Фёклы; место рождения — в образе наградного листа ПН (CAPTCHA)')
save('person-register.csv',h,P)
h,C=load('claims-register.csv')
add(h,C,claim_id='C-0019',claim_text='Лаврентий Тимофеевич Шарабарин (Прабожье Поле → Орехово-Зуево, проп. 1941) — брат Николая Тимофеевича, дядя Фёклы',subject_person_ids='P-0055;P-0050;P-0021',claim_type='sibling',artifact_ids='A-0070;A-0067;A-0065',supporting_independence_groups='IG-OBD-SHARABARIN;IG-FAM-IRINA',status='hypothesis',confidence='medium',rationale='отчество Тимофеевич, гнездо Дмитриевского у., Орехово-Зуево — где Фёкла жила в 1943',next_action='спросить семью; ГАКО ф.217 — метрики Прабожья/Фатеевки')
save('claims-register.csv',h,C)
h,S=load('search-log.csv')
for sid,tg,goal,q,src,res,nx in [
 ('S-0085','P-0012;P-0043','Павел Евсеевич в ЗАГС Красилівки 1935–48','браки 1935–36, 1943–46; рождения 1937–39, 1944–48; поновлені Ставище 1944','commons (ДАКО Р-5634)','negative','книг 1941–43 и браков 1937–42 нет; см. zaychuk-6-krasylivka.md'),
 ('S-0086','P-0043;P-0053','родня Павла в МК Красиловки 1900–1919; ОБД/ПН Павла','FamilySearch МК; ОБД/Подвиг народа варианты Евсеевич/Евсиевич/Овсеевич/Заичук','familysearch.org; obd-memorial.ru; podvignaroda.ru','negative (ПН — CAPTCHA)','ПН госпитали — после CAPTCHA пользователем'),
 ('S-0087','P-0021;P-0050','Шарабарины, Ясная Поляна','ОБД Шарабарин; nashipredki приходы Прабожье Поле, Фатеевка','obd-memorial.ru; nashipredki.com','found','A-0070;A-0071 — метрик 1916 онлайн нет → ГАКО ф.217')]:
    add(h,S,search_id=sid,timestamp='2026-11-02',target_person_ids=tg,research_goal=goal,query=q,language_locale='ru;uk',source_or_domain=src,result_status=res,artifact_ids=('A-0070;A-0071' if sid=='S-0087' else ''),next_step=nx)
save('search-log.csv',h,S)
print('ok')
