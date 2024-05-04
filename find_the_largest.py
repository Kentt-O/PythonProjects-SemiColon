def find_the_largest(number1, number2, number3):
	nums = [number1,number2,number3]
	largest = 0

	for number in nums:
		if number > largest:
			largest = number

	return largest