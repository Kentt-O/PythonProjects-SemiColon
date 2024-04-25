def  adding_suffix(a):
	if a is None:
        	return "Input cannot be None"
	elif not isinstance(a, str):
        	return "Input must be a string"
	elif len(a) < 3:
		return a
	elif (a[-3:] == 'ing'):
		return a+'ly'
	else:
		last_three = (a[-3:] != 'ing')
		return a+'ing'
	

print(adding_suffix('abc'))
print(adding_suffix('string'))
print(adding_suffix('on'))
