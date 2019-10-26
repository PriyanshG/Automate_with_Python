import openpyxl,os

os.chdir('/run/media/priyansh/697BADB67547A75B/automate_the_things/')

wb=openpyxl.load_workbook('google.xlsx')
sheet=wb.get_sheet_by_name('Sheet1')

i=1
while(sheet['B'+str(i)].value!=None):
	if sheet['B'+str(i)].value=='TRUE':
		sheet['C'+str(i)].value='FALSE'
	else:
		sheet['C'+str(i)].value='TRUE'
	i+=1

wb.save('google.xlsx')


