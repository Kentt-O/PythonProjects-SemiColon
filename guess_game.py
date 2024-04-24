import random

RANDOM_NUMBER = random.randrange(1, 10)
guess_input = int(input('Guess the number: '))

while RANDOM_NUMBER != guess_input:
	guess_input = int(input('Guess the number: '))

	if guess_input == RANDOM_NUMBER:
		print('Random Number is : ', RANDOM_NUMBER)
		print ('Welldone!! you guessed right !')
		break

	else:
		print('Random Number is : ', RANDOM_NUMBER)
		print('Try Again')




	

