amount = int(input('Enter amount: '))
rate = int(input('Enter interest rate '))
num_of_years = int(input('Enter the numbr of years: '))

count = 0

for year in range (0 , num_of_years):
	interest_rate = (rate / 100.0) * amount
	amount = interest + amount
	count += 1
	print (f"Year {count} you have {amount:.2f}")
	