import os

for folderName,subfolders,filenames in os.walk('../Codes'):
	print('The folder is ' + folderName)
	print('The subfolders are in is ' + folderName+'are' +str(subfolders))
