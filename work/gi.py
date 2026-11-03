import re,html,sys
h=open(sys.argv[1],encoding='utf-8',errors='ignore').read()
t=re.sub(r'<script.*?</script>','',h,flags=re.S)
i=t.find('</select>',t.rfind('<select')); t=t[i:]
t=html.unescape(re.sub(r'<[^>]+>','\n',t))
lines=[l.strip() for l in t.split('\n') if l.strip()]
m=[l for l in lines if l.startswith('Matches Found')]
print(m[:1])
for k,l in enumerate(lines):
  if l.startswith('Original Title') or l.startswith('image '): print('  ',l)
