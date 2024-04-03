SCORES_ENTERED = 10
total_scores = 0

for i in range(10):
	score = int(input('Enter score: '))
	total_scores += score
print('Average score is', total_scores / SCORES_ENTERED) 

	