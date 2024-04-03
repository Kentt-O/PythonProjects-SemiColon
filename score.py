score =int(input('Enter score: '))

if score >= 80 and score <= 100:
	print('Your score is', score ,'your grade is A')

elif score >= 65 and score <= 79:
	print('Your score is', score ,'your grade is B')

elif score >= 50 and score <= 64:
	print('Your score is', score ,'your grade is C')

elif score >= 40 and score <= 49:
	print('Your score is', score ,'your grade is D')
else: 
	print('Your score is', score, 'you are a criminal')