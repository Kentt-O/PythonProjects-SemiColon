spree_list = []
rows, cols = 4, 5
for i in range(rows):
    col = []
    for j in range(cols):
        product = i * j
        col.append(product)
        spree_list.append(col)

for i in range(rows):
    for j in range(cols):
        print(spree_list[i][j], end=" ")
    print()


def return_even_numbers(list_of_nums: list):
    numbers = []
    for number in list_of_nums:
        if number % 2 == 0:
            numbers.append(number)
    print(numbers)


return_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])


def even_list2(list_of_numbers):
    return [number_ for number_ in list_of_numbers if number_ % 2 == 0]


nums = list(range(1, 51))
print(nums)
print(even_list2(nums))
