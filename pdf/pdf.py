import PyPDF2 as ppdf

pdffile1=open('meetingminutes1.pdf','rb')
reader1=ppdf.PdfFileReader(pdffile1)

#print(reader.numPages)

#page=reader.getPage(0);

#print(page.extractText())

pdffile2=open('meetingminutes2.pdf','rb')
reader2=ppdf.PdfFileReader(pdffile2)


writer=ppdf.PdfFileWriter()

for p1 in range (reader1.numPages):
	if p1%2:
		page=reader1.getPage(p1-1)
	else:
		page=reader1.getPage(p1)
	writer.addPage(page)


for p2 in range (reader2.numPages):
	page=reader2.getPage(p2)
	writer.addPage(page)


outputfile=open('combined.pdf','wb')
writer.write(outputfile)
pdffile1.close()
pdffile2.close()
