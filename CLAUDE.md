# Исследование рода Комаровых — правила для Claude

Дело ведётся навыком `ex-ussr-kinship-research`. Каталог дела — `case/` (на этой машине `~/kinship-cases/komarova` — симлинк сюда).
Аудит: `python3 ~/.claude/skills/ex-ussr-kinship-research/scripts/audit_evidence.py --case-dir case`.

## Как работать
- Отвечать по-русски, предельно кратко. Исследовать самостоятельно, не спрашивать «продолжать?».
- Корень древа — Настя (Анастасия Игоревна Комарова), жена Михаила.
- Новые находки — в реестры `case/*.csv` (python `csv.DictWriter` по существующему заголовку) и `case/research-state.md`.
- Древо: правится `case/tree.html` (массивы `P` — прямые предки `{ id, g, x, n, s, st, c }`, `S` — братья/сёстры `{ id, sib, x, n, s, st, to }`, `target` — чья карточка открывается; карточки `<details class="person" id=...>`), затем PDF и сайт.
- PDF: `sed 's/<details class="person/<details open class="person/g' case/tree.html > case/pdf-source/tree-print.html` и headless Chrome `--no-pdf-header-footer --virtual-time-budget=5000 --print-to-pdf="$PWD/case/Древо-Комаровых-Снимщиковых.pdf" "file://$PWD/case/pdf-source/tree-print.html"`.
- Сайт: `python3 tools/build_site.py` (падает при утечке дат живых и семейных скриншотов). Новых живых — в `LIVING`/`LIVING_REL`/`LIVING_SIB`, новых людей — в `PIDS`, сохранённые сканы — в `SCANS`.
- Промежуточные скрипты и выгрузки класть в `work/`; бинарные и большие файлы — в `work/raw/` (не в git).
- После каждого обновления: собрать сайт, `git commit` и `git push` в ветку `research` (её публикует GitHub Pages). Пуш — от аккаунта `sokomishalov` (не `sokomishalov-jp`).

## Ограничения
- Живые (Настя, Игорь, Ирина, Виктор, Лариса, Галина, Лидия, Геннадий, Софья Николаевна, тётя Зина, современные Снимщиковы): минимум данных, контакты и адреса не искать, на сайте — только имя.
- CAPTCHA и логины проходит Михаил; не обходить капчи, блокировки, без E-poisk. Условия за пользователя не принимать. Cookies и токены не сохранять.
- Запросы в архивы — только по указанию Михаила. Ничего в Telegram без «да» и без показа текста.
