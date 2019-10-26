import re

ph=re.compile(r'(\d\d)-(\d\d\d\d\d\d\d\d\d\d)')
ob=ph.search('Call me on 91-9452685369 or +91-9936794955 or +91-999')
print(ph.findall('Call me on 91-9452685369 or +91-9936794955 or +91-999'))
print(ob.group())
print(ob.group(1))   #grouped bt ()


ph=re.compile(r'\(\d\d\)-(\d\d\d\d\d\d\d\d\d\d)')
ob=ph.search('Call me on (91)-9452685369 or +91-9936794955 or +91-999')
print(ob.group())



msg='Bat'
batregex=re.compile(r'Bat(man|motorcycle|bat)')
mo=batregex.search(msg)
try:
	print(mo.group())
except:
	print('Empty')

