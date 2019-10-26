import bs4,requests
import openpyxl,re
import sys
import xlsxwriter





print(sys.argv[1])
s=(sys.argv[2])
a=s.split('.html')
print(a)

wb=xlsxwriter.Workbook(str(sys.argv[1])+'.xlsx')
sheet=wb.add_worksheet()
wb.close()
wb=openpyxl.load_workbook(str(sys.argv[1])+'.xlsx')
sheet=wb.get_sheet_by_name('Sheet1')
i=1
while(sheet['A'+str(i)].value!=None):
	i+=1
start=i



headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
}

add='http://www.indiaparinam.com/c-programming-language-question-answer-expressions/true-false-questions'

#add=pyperclip.paste()
for k in range(1,7):
	s=a[0]
	add=s+'_'+str(k)+'.html'
	res=requests.get(add,headers=headers)
	print(res)
	soup=bs4.BeautifulSoup(res.text,'html.parser')

	elem=soup.findAll("span",{"itemprop":"name"})

	j=start
	for i in elem:
		ques=re.compile(r'<span itemprop="name">((\d*\w*\s*[\?\!\".;:,\'\-\(\)\[\]]*)+)')
		qu=ques.search(str(i))
		try:
			sheet['A'+str(j)].value=str(qu.group(1))
			j+=1
		except:
			 f=0

	elem=soup.findAll("b",{"itemprop":"text"})

	j=start
	for i in elem:
		ans=re.compile(r'<b itemprop="text">((\d*\w*\s*[\?\!\".;:,\'\-\(\)\[\]]*)+)')
		an=ans.search(str(i))
		try:
			sheet['B'+str(j)].value=str(an.group(1))
			j+=1
		except:
			 f=0
	start=j
wb.save(str(sys.argv[1])+'.xlsx')
#
#
print('New added = ',j-start,'\nTotal question = ',j-1)
#
