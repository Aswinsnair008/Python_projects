#guessing number in the range of 100
import random as random #we are importing the modulle called random for this
num = random.randrange(100) #the finction randrange will generate random numbers for us
guess = 5 #we have 5 chances to guess the number, this is the counter running incrementally
while guess >= 1: #when the guess value is greater than 1,then continue the below
	your_guess=  int(input("give your guess"))#asking for input from user and storing the value in a variable called your_guess
	def check(x): #we are defining a function check and passing a variable x
		if your_guess==x:#here the num value is checked with the your_guess value if equal the print statement will be printed
			print('you won')
		elif your_guess >x :
			print ("your guess is greater, think slow")
		else:
			print('your guess is small, think faster')
	if guess >2:#if the guess value is greater than 2 this code will be run
		check(num)#we are passing the value stored in variable num to the function check
	elif guess ==2:#here once the guess value is equal to 2 then this part will run and hence user will be given a warning as next will be the last chance
		check(num)
		print('next will be your last chance')
	else:
		print('sorry! you lose')
	guess = guess-1#here the guess value is decremented by 1


