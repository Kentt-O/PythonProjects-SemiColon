def consonants(word):
	vowel = 0
	consonant = 0

	for letter in word:
		if letter == 'a' :
			vowel += 1
		elif letter ==   'e' :
			vowel += 1
		elif letter == 'i' :
			vowel += 1
		elif letter  == '0':
			vowel += 1
		elif letter  == 'u' :
			vowel += 1
		else :
			consonant = consonant +1

	
	
	print('Consonants :', consonant, 'Vowels :', vowel)
	

consonants('abc')