import pdftotext as ppdf

pdf=open('MBA.pdf','rb')
read=ppdf.PDF(pdf)

print(read[0])

print('\n')
print('\n')
print('\n')
print('\n')
print('\n')


import re



for i in range (0,0):
	print(read[0][i])

lis=re.compile(r'((\w*\s*[&,]*)*)\(Shift I\)\s(\d\s-\s\d)\s\d')
l=(read[0].split('\n'))
i=l[7];
print(i)
li=lis.search(str(i))
print(li.group(0))
