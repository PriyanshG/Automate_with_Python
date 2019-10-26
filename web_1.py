import webbrowser,sys,pyperclip

sys.argv
#check whether command line argument were passed 
if len(sys.argv)>1:
	add='+'.join(sys.argv[1:])
else:
	add=pyperclip.paste()

#https://www.google.com/search?ei=jtfeXPi0EcbgrQGju6q4BQ&q=fellow+ship
webbrowser.open('https://www.google.com/search?ei=jtfeXPi0EcbgrQGju6q4BQ&q='+add)
print(add)


