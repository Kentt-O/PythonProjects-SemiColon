largest_number = 0
smallest_number = 0
user_input = 0
		
			
while user_input != -10:  
	user_input = int(input("Enter numbers (to stop press -10): "))
	if user_input > largest_number:
		largest_number = user_input
		user_input = user_input + 1
	if smallest_number == 0:
		smallest_number = user_input
	elif user_input < smallest_number:
		smallest_number = user_input
		
		
			
print("The largest number is", largest_number,"The smallest number is",smallest_number);

