def string_slicing (a):
	if a is None:
        	return "Input cannot be None"
	elif not isinstance(a, str):
        	return "Input must be a string"
	elif len(a) < 2:
		return ""
	else:
		first_two = a[:2]
		last_two = a[-2:]
		return first_two + last_two
	

print(string_slicing('0'))
