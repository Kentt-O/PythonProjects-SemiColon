positive_numbers = 0
negative_numbers = 0
zeros = 0
userInput = 0

while userInput != -100:
	userInput = int(input('Enter numbers (to stop press -100): '))
	if userInput == 0: 
		zeros = zeros + 1
	
	elif userInput < 0:
		negative_numbers = negative_numbers + 1
	
	else :
		positive_numbers = positive_numbers + 1

print("Positive numbers are", positive_numbers,  "Negative numbers are", negative_numbers,"Zeros are", zeros)
	