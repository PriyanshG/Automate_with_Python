import random

print('Hello,What is your name ?')
name=input()

print('I am thinking oof number between 1 to 50 ')
n=random.randint(1,50)

flag=0
for i in range(1,7):
	print('Guess a number')
	x=int(input())
	
	if x<n:
		print('Your guess is too low')
	elif x>n:
	    print('Your guess is too high')
	else:
		flag=1
		break

if flag==1:
	print('Your guess is correct')
else:
	print("Better luck next time " + name + "!!! Number is " + str(n))

	
