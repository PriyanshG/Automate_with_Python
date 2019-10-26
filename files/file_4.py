import os
os.getcwd()
try:
	os.unlink('hello.txt')
except: 
	print('not found')

try:
	os.rmdir('New Folder')  #should be empty
except: 
	print('not found')


import shutil #shellutility
shutil.rmtree('New Folder')


#send2trash is used to send the deleted file to bin

