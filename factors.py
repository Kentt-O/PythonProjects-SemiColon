user_input = int(input("Enter a digit: "))

counter = 1
factors = 0

while counter <= user_input:
	if user_input % counter == 0:
		factors = factors + 1
	counter = counter + 1

print("The factors are", factors)
