import re

def pri(ob):
	try:
		print(ob.group())
	except:
		print('No match Found')

batre=re.compile(r'Batman|Batwoman')

batre=re.compile(r'Bat(woman|man)')

batre=re.compile(r'Bat(wo)?man')


ob=batre.search('Hi,I am a Batman')
pri(ob)


ob=batre.search('Hi,I am a Batwoman')
pri(ob)


ob=batre.search('Hi,I am a Batwowoman')
pri(ob)

mobre= re.compile(r'(\d\d-)?\d\d\d\d\d\d\d\d\d')
mob=mobre.search('My contact number are +91-9452685369 ,+919936794955,8756865699,9988776655')
pri(mob) #?can only used with search not with findall



batre=re.compile(r'Bat(wo)*man')   #* means zero or more
ob=batre.search('Hi,I am a Batwowoman')
pri(ob)
print('\n')

batre=re.compile(r'Bat(wo)+man')   #+ means zero or more
ob=batre.search('Hi,I am a Batwowoman')
pri(ob)
ob=batre.search('Hi,I am a Batwoman')
pri(ob)
ob=batre.search('Hi,I am a Batman')
pri(ob)



mobre= re.compile(r'(((\+)?\d\d(-)?)?\d\d\d\d\d\d\d\d\d\d( )*(,)?( )*){3}')
mob=mobre.search('My contact number are +91-9452685369 ,+919936794955,  8756865699,9988776655')
pri(mob) #can only used with search not with findall


print('\n')
mobre= re.compile(r'(((\+)?\d\d(-)?)?\d\d\d\d\d\d\d\d\d\d( )*(,)?( )*){2,3}')
mob=mobre.search('My contact number are +91-9452685369 ,+919936794955,  8756865699,9988776655')
pri(mob) #can only used with search not with findall
mob=mobre.search('My contact number are +91-9452685369 ,+919936794955,  865699,998877665')
pri(mob) #can only used with search not with findall

print('\n')   #?mark will print minimum number 
mobre= re.compile(r'(((\+)?\d\d(-)?)?\d\d\d\d\d\d\d\d\d\d( )*(,)?( )*){2,3}?')
mob=mobre.search('My contact number are +91-9452685369 ,+919936794955,  8756865699,9988776655')
pri(mob) #can only used with search not with findall
