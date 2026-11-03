import csv,os
D=os.path.expanduser('~/kinship-cases/komarova/')
def load(f):
    with open(D+f,newline='') as h: r=list(csv.DictReader(h)); 
    with open(D+f,newline='') as h: hdr=next(csv.reader(h))
    return hdr,r
def save(f,hdr,rows):
    with open(D+f,'w',newline='') as h:
        w=csv.DictWriter(h,fieldnames=hdr); w.writeheader(); w.writerows(rows)
def upd(rows,key,kid,**kw):
    for r in rows:
        if r[key]==kid: r.update(kw); return
    raise SystemExit('no '+kid)
def add(hdr,rows,**kw):
    assert not any(r[hdr[0]]==kw[hdr[0]] for r in rows), kw[hdr[0]]
    rows.append({k:kw.get(k,'') for k in hdr})

# ---------- artifacts
h,A=load('artifact-register.csv')
fam=dict(captured_at='2026-11-02',source_type='family-statement',language_script='ru-Cyrl',provenance_level='family-memory',directness='direct',originality='original',legibility='good',status='active')
add(h,A,artifact_id='A-0065',source_title='Telegram #1131103: ответы Ирины Ивановны (через Настю) на вопросы 3–10',source_url_or_path='telegram @AnastassiaKomarova #1131103',record_date='2026-11-02',person_ids='P-0004;P-0023;P-0045;P-0046;P-0047;P-0043;P-0021;P-0005;P-0009;P-0020',names_as_written='Елена Ивановна Коршикова; дед Федор; Надежда Федоровна Архипчук; Николай Федорович Снимщиков; Павел Евсеевич; Фёкла Николаевна',summary='Мать Ивана — Елена Ивановна Коршикова; отец Федор не воевал, был на оккупированной территории, убит при освобождении (слухи). Иван уехал взрослым вслед за сестрой Надеждой Федоровной Архипчук, братом Николаем и матерью. Иван ум. 8.05.2009 в Москве, похоронен на Хованском. Павел Евсеевич воевал (Львов 1941, отступление, контузия); с Фёклой Николаевной познакомился в Орехово-Зуеве в 1943, увёз на Украину, где служил. Зайчук — девичья фамилия Галины. Фото без подписей у Ирины и Гены. Больше знают Галина и «т. Зина». Эльвира, возм., род. в Москве; мать Софья Шутис — Литва или Москва',independence_group='IG-FAM-IRINA',reliability_notes='слова Ирины Ивановны, переданы Настей; «слухи» про Федора — не проверено',**fam)
add(h,A,artifact_id='A-0066',source_title='Telegram #1131105: ответы Ирины Ивановны на вопросы 1–4 (через Настю)',source_url_or_path='telegram @AnastassiaKomarova #1131105',record_date='2026-11-02',person_ids='P-0004;P-0022;P-0046;P-0048;P-0049;P-0043;P-0005;P-0021',names_as_written='Иван Федорович; Семен Федорович; Ксения Федоровна; Ольга Федоровна; Павел Евсеевич; Фёкла Николаевна Шарабарина',summary='Иван Федорович: по документам 18.07.1942, по словам сестёр — июль 1941, д. Реплата Курской обл. После войны семья (кроме отца) → Луховицы; старшая дочь вышла за украинца → Фастов, за ней часть семьи; другая часть → Москва: старший брат Семен Федорович, Ксения Федоровна (Москва), Ольга Федоровна (Реутов). Павел Евсеевич, 1914, родом из Красиловки (там родные). Галина род. 1944 в с. Казачья Лопань Харьковской обл., где служил Павел. Фёкла Николаевна Шарабарина, 1916, из с. Ясная Поляна Дмитровского р-на Курской обл., фамилию, кажется, не меняла',independence_group='IG-FAM-IRINA',reliability_notes='семейная память; дата Ивана — «по документам»',**fam)
add(h,A,artifact_id='A-0067',source_title='Telegram #1131106: родители Фёклы',source_url_or_path='telegram @AnastassiaKomarova #1131106',record_date='2026-11-02',person_ids='P-0021;P-0050;P-0051',names_as_written='Николай Тимофеевич Шарабарин; Варвара Анатольевна',summary='Родители Фёклы — Николай Тимофеевич Шарабарин (ум. 1972) и Варвара Анатольевна (фамилия неизвестна)',independence_group='IG-FAM-IRINA',reliability_notes='отчество «Анатольевна» необычно для ~1890 — проверить',**fam)
add(h,A,artifact_id='A-0068',source_title='Find a Grave: «И Ф Снимщиков», 18.06.1942 – 08.05.2009, Хованское кладбище',source_url_or_path='https://www.findagrave.com/memorial/321706498',captured_at='2026-11-02',source_type='grave-index',repository_or_archive='Find a Grave',archival_reference='Хованское, Центральное, ЗИ/121/45А/0146',record_date='2009',place_as_written='Khovanskoye',language_script='ru-Cyrl/en',person_ids='P-0004',names_as_written='И Ф Снимщиков',summary='Надгробие: инициалы И. Ф., даты 18.06.1942 – 08.05.2009. Дата смерти день в день совпадает с семейной (A-0065), кладбище совпадает',provenance_level='volunteer-transcription',directness='direct',originality='derivative',independence_group='IG-FAG',legibility='good',related_claim_ids='C-0014',reliability_notes='месяц рождения 06 против «18.07.1942 по документам» (A-0066) — ошибка надписи или транскрипции',status='evidence')
add(h,A,artifact_id='A-0069',source_title='Со слов Насти (через Михаила): Галина — день рождения 6 февраля; разница с Настей «ровно 52 года»; младшая сестра Лидия Павловна Зайчук род. в Фастове, ~на 5 лет младше',source_url_or_path='chat 2026-11-02',record_date='2026-11-02',person_ids='P-0005;P-0052',names_as_written='Галина Павловна; Лидия Павловна Зайчук',summary='6 февраля; «52 года» → 1943, но A-0066 даёт 1944 (знакомство родителей 1943) — принят 6.02.1944. Лидия ~1949, Фастов',independence_group='IG-FAM-NASTYA',reliability_notes='год из разницы возрастов — округлён',**fam)
save('artifact-register.csv',h,A)

# ---------- persons
h,P=load('person-register.csv')
upd(P,'person_id','P-0004',preferred_label='Снимщиков Иван Федорович',living_status='deceased',names_as_written='Снимщиков Иван; Иван Федорович (A-0021, A-0066); «И Ф Снимщиков» (надгробие)',birth_estimate='18.07.1942 по документам (надгробие: 18.06.1942); фактически ~07.1941 (со слов сестёр)',death_estimate='08.05.2009, Москва',places='д. Реплата (Репецкая Плата) Курской обл. → Луховицы → Фастов → Москва; похоронен на Хованском',historical_jurisdictions='Мантуровский р-н Курской обл. (быв. Тимский у.)',relatives_as_reported='отец Федор, мать Елена Ивановна Коршикова; братья Семен, Николай; сёстры Надежда (Архипчук), Ксения, Ольга; жена Галина Павловна Зайчук; дети Ирина, Геннадий',source_artifact_ids='A-0001;A-0021;A-0065;A-0066;A-0068',candidate_status='confirmed',merge_or_split_rationale='= «И Ф Снимщиков» Find a Grave (C-0014): дата смерти и кладбище совпадают день в день',notes='дед по матери')
upd(P,'person_id','P-0005',preferred_label='Снимщикова (Зайчук) Галина Павловна',living_status='living',names_as_written='Зайчук Галина Павловна (девичья — подтверждено A-0065)',birth_estimate='6.02.1944 (A-0066, A-0069; «52 года» давало 1943)',places='с. Казачья Лопань Харьковской обл. → Фастов',relatives_as_reported='отец Павел Евсеевич Зайчук, мать Фёкла Николаевна Шарабарина; сестра Лидия; муж Иван Федорович Снимщиков; дети Ирина, Геннадий',source_artifact_ids='A-0001;A-0065;A-0066;A-0069',candidate_status='reported',notes='бабушка по матери; жива — данные минимальны. Акт о рождении онлайн нет (Дергачёвский ДРАЦС); Фастов 1944–48 — нет')
upd(P,'person_id','P-0012',preferred_label='Зайчук Павел Евсеевич (= P-0043)',birth_estimate='1914',places='с. Красиловка (родом); служил: Львов 1941, Орехово-Зуево 1943, Казачья Лопань 1944; Фастов',relatives_as_reported='жена Фёкла Николаевна Шарабарина; дочери Галина 1944, Лидия ~1949',occupation_or_status='военнослужащий; контужен',source_artifact_ids='A-0006;A-0065;A-0066',candidate_status='probable',merge_or_split_rationale='= P-0043 (C-0015): отчество, село и год совпадают',notes='прадед; запись семьи')
upd(P,'person_id','P-0043',candidate_status='probable',merge_or_split_rationale='= P-0012 (C-0015): семья — Павел Евсеевич, 1914, родом из Красиловки',notes='прадед Насти (вероятно)')
upd(P,'person_id','P-0021',preferred_label='Шарабарина Фёкла Николаевна',names_as_written='Фекла (A-0020); Фёкла Николаевна Шарабарина (A-0066)',normalized_name_variants='Фёкла/Текля; Шарабарина/Шаробарина',birth_estimate='1916',places='с. Ясная Поляна «Дмитровского р-на Курской обл.» → Орехово-Зуево (1943) → Украина → Фастов (похоронена)',historical_jurisdictions='Дмитровский р-н: Курская обл. 1934–37, ныне Орловская обл. (проверить)',relatives_as_reported='отец Николай Тимофеевич Шарабарин, мать Варвара Анатольевна; муж Павел Евсеевич Зайчук; дочери Галина 1944, Лидия, Татьяна (ум. в младенчестве); 2 брака, 1-й муж погиб на войне',source_artifact_ids='A-0020;A-0065;A-0066;A-0067',notes='прабабушка по матери; фамилию, видимо, не меняла')
upd(P,'person_id','P-0022',places='Москва',relatives_as_reported='сестра Ивана',source_artifact_ids='A-0021;A-0066')
upd(P,'person_id','P-0023',preferred_label='Снимщиков Федор (отец Ивана)',living_status='deceased',death_estimate='~1943, при освобождении (слухи)',places='Репецкая Плата Курской обл. (оккупация 1941–43)',relatives_as_reported='жена Елена Ивановна Коршикова; дети Семен, Николай, Надежда, Ксения, Ольга, Иван',occupation_or_status='не воевал; на оккупированной территории',source_artifact_ids='A-0021;A-0065;A-0066',merge_or_split_rationale='Киевский Федор Васильевич 1909/10 (воевал до 1946) и Ф.В. 1913–1984 — НЕ он (A-0065). Кандидат: Федор Семенович ~1886 (P-0027) — не проверено',notes='прадед; отчество неизвестно')
upd(P,'person_id','P-0024',candidate_status='rejected',notes='дед Иван род. 1941/42 — не он')
upd(P,'person_id','P-0044',notes='отвергнут как предок: киевский Федор Васильевич воевал, а прадед Федор — нет (A-0065)')
base=dict(living_status='deceased?',candidate_status='reported')
add(h,P,person_id='P-0045',preferred_label='Снимщикова (Коршикова) Елена Ивановна',names_as_written='Елена Ивановна Коршикова',places='Репецкая Плата → Луховицы → Фастов?',relatives_as_reported='муж Федор; дети Семен, Николай, Надежда, Ксения, Ольга, Иван',source_artifact_ids='A-0065;A-0066',notes='прабабушка по матери',**base)
add(h,P,person_id='P-0046',preferred_label='Архипчук (Снимщикова) Надежда Федоровна',names_as_written='Надежда Федоровна Архипчук',places='Репецкая Плата → Луховицы → Фастов',relatives_as_reported='старшая дочь Федора; муж-украинец Архипчук',source_artifact_ids='A-0065;A-0066',notes='сестра деда Ивана',**base)
add(h,P,person_id='P-0047',preferred_label='Снимщиков Николай Федорович',names_as_written='Николай Федорович Снимщиков',relatives_as_reported='брат Ивана',source_artifact_ids='A-0065',notes='брат деда Ивана; не путать с Николаем Тимофеевичем Шарабариным',**base)
add(h,P,person_id='P-0048',preferred_label='Снимщиков Семен Федорович',names_as_written='Семен Федорович',places='Москва',relatives_as_reported='старший брат Ивана',source_artifact_ids='A-0066',**base)
add(h,P,person_id='P-0049',preferred_label='Ольга Федоровна (Снимщикова)',names_as_written='Ольга Федоровна',places='Реутов',relatives_as_reported='сестра Ивана',source_artifact_ids='A-0066',**base)
add(h,P,person_id='P-0050',preferred_label='Шарабарин Николай Тимофеевич',living_status='deceased',names_as_written='Николай Тимофеевич Шарабарин',death_estimate='1972',places='с. Ясная Поляна (Дмитровский р-н)',relatives_as_reported='отец Тимофей; жена Варвара; дочь Фёкла 1916',source_artifact_ids='A-0067',candidate_status='reported',notes='прапрадед')
add(h,P,person_id='P-0051',preferred_label='Шарабарина Варвара «Анатольевна»',names_as_written='Варвара Анатольевна',relatives_as_reported='муж Николай Тимофеевич; дочь Фёкла',source_artifact_ids='A-0067',notes='прапрабабушка; отчество проверить',**base)
add(h,P,person_id='P-0052',preferred_label='Зайчук Лидия Павловна',living_status='living',names_as_written='Зайчук Лидия',birth_estimate='~1949',places='Фастов',relatives_as_reported='сестра Галины',source_artifact_ids='A-0069',candidate_status='reported',notes='живая — не искать; Фастов 1946–48 — нет')
add(h,P,person_id='P-0053',preferred_label='Зайчук Евсевий Игнатьевич',living_status='deceased',names_as_written='Евсевий Игнатьев Зайчук',birth_estimate='~1892 (21 в I.1914)',places='с. Красиловка',relatives_as_reported='отец Игнатий Симеонов (?); жена Елисавета Даниловна Коритнюк; дети Павел 1914, Дария 1916, София 1918',occupation_or_status='крестьянин',confession_or_community_as_recorded='православный',source_artifact_ids='A-0060',candidate_status='probable',notes='прапрадед (через C-0015)')
add(h,P,person_id='P-0054',preferred_label='Зайчук (Коритнюк) Елисавета Даниловна',living_status='deceased',names_as_written='Елисавета Даниилова Коритнюк/Коритник',birth_estimate='~1893 (20 в I.1914)',places='с. Красиловка',relatives_as_reported='муж Евсевий; дети Павел, Дария, София',confession_or_community_as_recorded='православная',source_artifact_ids='A-0060',candidate_status='probable',notes='прапрабабушка (через C-0015)')
save('person-register.csv',h,P)

# ---------- claims
h,C=load('claims-register.csv')
upd(C,'claim_id','C-0013',status='rejected (как предок)',rationale=next(r for r in C if r['claim_id']=='C-0013')['rationale']+'. 02.11: семья — прадед Федор не воевал (A-0065), а киевский Ф.В. воевал до 1946 ⇒ это не отец Ивана',next_action='')
add(h,C,claim_id='C-0014',claim_text='Дед Иван Федорович Снимщиков = «И Ф Снимщиков» (Find a Grave, Хованское, 18.06.1942–08.05.2009)',subject_person_ids='P-0004',claim_type='identity;death;burial',artifact_ids='A-0065;A-0066;A-0068',supporting_independence_groups='IG-FAM-IRINA;IG-FAG',contradicting_artifact_ids='',status='corroborated',confidence='high',rationale='дата смерти 8.05.2009 и кладбище совпадают день в день; инициалы И. Ф. и год 1942 совпадают; месяц рождения 06 vs 07 — расхождение',next_action='фото памятника / ritual.mos.ru для месяца рождения')
add(h,C,claim_id='C-0015',claim_text='Павел Евсеевич Зайчук (отец Галины) = Павел, род. 5.XI.1914 в Красиловке у Евсевия Игнатьева Зайчука и Елисаветы Данииловой',subject_person_ids='P-0012;P-0043;P-0053;P-0054',claim_type='identity;parent',artifact_ids='A-0060;A-0065;A-0066',supporting_independence_groups='IG-FAM-IRINA;IG-FS-KRASYLIVKA',contradicting_artifact_ids='',status='probable',confidence='medium-high',rationale='семья: отчество Евсеевич, 1914, родом из Красиловки; метрика: Павел 5.XI.1914, отец Евсевий; других Павлов Евсеевичей в индексе нет',next_action='документ Павла с датой рождения (военный/ПН)')
add(h,C,claim_id='C-0016',claim_text='Галина Павловна Зайчук род. 6.02.1944 в с. Казачья Лопань Харьковской обл.; родители Павел Евсеевич и Фёкла Николаевна Шарабарина',subject_person_ids='P-0005;P-0012;P-0021',claim_type='birth-parentage',artifact_ids='A-0066;A-0069;A-0065',supporting_independence_groups='IG-FAM-IRINA;IG-FAM-NASTYA',contradicting_artifact_ids='A-0069',status='single-source (семья)',confidence='medium',rationale='знакомство родителей 1943 ⇒ 1944; «ровно 52 года» давало 1943 — округление',next_action='акт — только Дергачёвский ДРАЦС (запрос от Галины/детей)')
add(h,C,claim_id='C-0017',claim_text='Родители Фёклы — Николай Тимофеевич Шарабарин (ум. 1972) и Варвара Анатольевна; Фёкла род. 1916 в с. Ясная Поляна',subject_person_ids='P-0021;P-0050;P-0051',claim_type='parent;birth',artifact_ids='A-0066;A-0067',supporting_independence_groups='IG-FAM-IRINA',contradicting_artifact_ids='',status='single-source (семья)',confidence='medium',rationale='семейная память',next_action='метрика 1916 Ясной Поляны (FamilySearch)')
add(h,C,claim_id='C-0018',claim_text='Родители деда Ивана — Федор Снимщиков и Елена Ивановна Коршикова; сиблинги Семен, Николай, Надежда (Архипчук), Ксения, Ольга; родина — Репецкая Плата',subject_person_ids='P-0004;P-0023;P-0045;P-0046;P-0047;P-0048;P-0022;P-0049',claim_type='parent;sibling;birth',artifact_ids='A-0021;A-0065;A-0066',supporting_independence_groups='IG-FAM-IRINA;IG-FAM-NASTYA',contradicting_artifact_ids='',status='single-source (семья)',confidence='medium-high',rationale='семейная память; Ксения подтверждена дважды',next_action='отчество Федора; метрики/похозкниги Репецкой Платы (ГАКО)')
save('claims-register.csv',h,C)

# ---------- relationships
h,R=load('relationship-register.csv')
n=len(R)
def rel(a,t,b,cl,art,st,cf,ra):
    global n; n+=1
    add(h,R,relationship_id=f'R-{n:04d}',person_a_id=a,relationship_type=t,person_b_id=b,biological_legal_household='biological',claim_ids=cl,supporting_artifact_ids=art,status=st,confidence=cf,rationale=ra)
for c in ['P-0004','P-0046','P-0047','P-0048','P-0022','P-0049']:
    rel('P-0023','parent-of',c,'C-0018','A-0065;A-0066','reported','medium-high','семья')
    rel('P-0045','parent-of',c,'C-0018','A-0065;A-0066','reported','medium-high','семья')
rel('P-0004','spouse-of','P-0005','','A-0001','reported','high','семья')
rel('P-0004','parent-of','P-0003','','A-0001','reported','high','семья')
rel('P-0005','parent-of','P-0003','','A-0001','reported','high','семья')
for c in ['P-0005','P-0052']:
    rel('P-0012','parent-of',c,'C-0016','A-0065;A-0066;A-0069','reported','high','семья')
    rel('P-0021','parent-of',c,'C-0016','A-0065;A-0066;A-0069','reported','high','семья')
rel('P-0012','spouse-of','P-0021','C-0016','A-0065','reported','high','познакомились 1943, Орехово-Зуево')
rel('P-0050','parent-of','P-0021','C-0017','A-0067','reported','medium','семья')
rel('P-0051','parent-of','P-0021','C-0017','A-0067','reported','medium','семья')
rel('P-0053','parent-of','P-0043','C-0015','A-0060','single-source','high','метрика 1914')
rel('P-0054','parent-of','P-0043','C-0015','A-0060','single-source','high','метрика 1914')
rel('P-0053','spouse-of','P-0054','C-0015','A-0060','single-source','high','брак 31.I.1914')
save('relationship-register.csv',h,R)

# ---------- search log
h,S=load('search-log.csv')
for sid,tg,goal,q,src,res,nx in [
 ('S-0082','P-0005;P-0012','Галина 1942–44 в Фастове (проход 5)','рождения город+сёла 1944–48, поновлені 3701/4126/4496/4497; Галины по отцу и февралю','commons.wikimedia.org (ДАКО Р-5634)','negative','см. zaychuk-5-fastiv-births.md; закрыто — Галина род. в Казачьей Лопани'),
 ('S-0083','P-0052','Лидия Павловна 1946–48 в Фастове','рождения 1946–47 целиком, 1948 частично; Лидия + отец Павел / мать Фекла','commons.wikimedia.org','negative','не дочитаны 4498, 4502, 4878–4880, 4871/4872/4874; вероятно Лидия 1949+ (ДРАЦС)'),
 ('S-0084','P-0005','акт рождения Галины 1944, Казачья Лопань','ДАХО Р-6531/Р-6532 на Commons; каталог FamilySearch Харьковская обл./Дергачёвский р-н','commons; familysearch.org','not-available-online','запрос в Дергачёвский ДРАЦС (заявитель — Галина/дети)')]:
    add(h,S,search_id=sid,timestamp='2026-11-02',target_person_ids=tg,research_goal=goal,query=q,language_locale='uk;ru',source_or_domain=src,result_status=res,next_step=nx)
save('search-log.csv',h,S)
print('ok')
