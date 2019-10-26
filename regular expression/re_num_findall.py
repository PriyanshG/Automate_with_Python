import re

def pri(ob):
	try:
		print(ob)
	except:
		print('No match Found')


mobre= re.compile(r'(\d\d\d)(\d\d\d\d\d\d)')
mob=mobre.findall('My contact number are +91-9452685369 ,+919936794955,8756865699,9988776655')
pri(mob)

vowelRE=re.compile(r'[aeiouAEIOU]')    #r'(a|e|i|o)
print(vowelRE.findall('I am your friend and I cant loose you! We will live togther'))
print('\n')

dvre=re.compile(r'[aeiouAEIOU]{2}')
print(dvre.findall('I am your friend and I cant loose you! We will live togther'))

vowelRE=re.compile(r'[^aeiouAEIOU]+')    # not r'(a|e|i|o)
print(vowelRE.findall('I am your friend and I cant loose you! We will live togther'))
print('\n')

vowelRE=re.compile(r'^HELLO')    #starting with HELLO
print(vowelRE.findall('HELLOI am your friend and I cant loose you! We will live togther'))
print('\n')

vowelRE=re.compile(r'world$')    #end with world
print(vowelRE.findall('HELLOI am your friend and I cant loose you! We will live togther world'))
print('\n')

vowelRE=re.compile(r'.at')    #words end with at and have one character at beginning
print(vowelRE.findall('The cat in the hat sat on the flat mat.'))
print('\n')

vowelRE=re.compile(r'.{1,2}at')    #.means anything
print(vowelRE.findall('Theat at cat in the hat sat on the flat mat.'))
print('\n')


nameRE=re.compile(r'First Name : (.*) Last Name : (.*)')
print(nameRE.findall('First Name : Priyansh Gaharana Last Name : Gaharana'))
print('\n')


re.compile(r'.*',re.DOTALL)  #total characterincludeing \n
re.compile(r'[aieou]',re.I)  #ignorecase 

