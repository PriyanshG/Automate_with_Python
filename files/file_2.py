hellofile=open('./hello.txt')  #default is read mode
content=hellofile.read()
print(content)

hellofile=open('./hello.txt')
print(hellofile.readlines())

hellofile=open('./hello.txt','a') #a for append
hellofile.write('''Hello bro!
How are uou''')

hellofile.write('''Hello bro!
How are uou''')


import shelve #for db
shelfFile=shelve.open('mydata')
shelfFile['cats']=['HI','dds','df']
shelfFile.close()


shelfFile=shelve.open('mydata')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))


