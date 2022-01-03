
import math

def addition(a, b):
	return(a+b)
def substract(a, b):
	return (a-b)
def modular(a, b):
	return math.fmod(a, b)
num = int(input("wht operation u want to perform choose 1 for addition 2 for substraction 3 for cos 4 for sin 5 for tan 7 for remainder"))
while num < 7:
	if num ==1:
		print('enter the values')
		x = int(input('give the first value'))
		y = int(input('give the second value'))
		result = addition(x, y)
		print('the sum is', result)
		
	elif num ==2:
		print('enter the values')
		x1 = int(input('give first the value'))
		y1 = int(input('give second value'))
		result1 = substract(x1, y1)
		print('difference is', result)
	elif num ==3:
		x2 = int(input('first value'))
		y2 = int(input('second value'))
		result2 = modular(x2, y2)
		print('the result is', result2)

		
	else:
		print('choose a valid option')
		

	new = int(input('do u want to continue?yes =1 no = 0'))
	if new == 1:
		num = int(input("wht operation u want to perform"))
	elif new ==0:
		print('thanks for using my calc, ciao u soon')
		break






