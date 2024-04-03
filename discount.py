price = int(input("Enter price: "))
discount_percentage = int(input('Enter discount in %: '))

convert_percentage = float(discount_percentage / 100.0)
percentage_discount = price * convert_percentage
discounted_price = price - percentage_discount

print('The price after discount is ', discounted_price)
