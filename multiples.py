# (Multiples) Use if statements to determine whether 1024 is a multiple of 4 and
# whether 2 is a multiple of 10. (Hint: Use the remainder operator.)

number1 = 1024
number2 = 10

if number1 % 4 == 0:
	print(number1,' is a multiple of 4')
else:
	print(number1, ' is not a multiple of 4')

if number2 % 2 == 0:
	print(number2, ' is a multiple of 2')

print(number2, 'is not a multiple of 2')