import re

namere=re.compile(r'Agent \w+')
print(namere.findall('Agent alice gave the secret documents to Agent Bob'))
print(namere.sub('anonymous','Agent alice gave the secret documents to Agent Bob'))


namere=re.compile(r'Agent (\w)\w+')
print(namere.sub(r'Agent \1**','Agent alice gave the secret documents to Agent Bob'))
