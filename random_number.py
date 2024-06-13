import numbers
import random


def random_numbers():
    random.seed(10)
    numbers = random.sample(range(1, 51), 10)

    return numbers


print(random_numbers())


def len_of_list(lst):
    count = 0
    for i in lst:
        count += 1
    return count


print(len_of_list(random_numbers()))


def sum_of_evens(lst):
    sum = 0
    for index in range(0, len_of_list(lst)):
        if index % 2 == 0:
            sum += lst[index]
    return sum


print(sum_of_evens(random_numbers()))


def sum_of_odd(lst):
    sum = 0
    for index in range(0, len_of_list(lst)):
        if index % 2 != 0:
            sum += lst[index]
    return sum


print(sum_of_odd(random_numbers()))


def sum_of_thirds(lst):
    sum = 1
    for index in range(2, len_of_list(lst), 2):
        sum *= lst[index]
    return sum


print(sum_of_thirds(random_numbers()))


def list_average(lst):
    sum = 0
    for index in range(0, len_of_list(lst)):
        sum = lst[index] / len_of_list(lst)
    return sum


print(list_average(random_numbers()))


def largest(lst):
    largest_number = 0
    for index in range(0, len_of_list(lst)):
        if lst[index] > largest_number:
            largest_number = lst[index]
    return largest_number


print(largest(random_numbers()))


def smallest_number(lst):
    smallest = lst[0]
    for index in range(0, len_of_list(lst)):
        if lst[index] < smallest:
            smallest = lst[index]
    return smallest


print(smallest_number(random_numbers()))

collection = ["Bastard", "Vengeance", "explode", "surge", "small"]


def string_count(words):
    word = []
    for letter in words:
        if len_of_list(letter) >= 2 and letter[0] == letter[-1]:
            word.append(letter)
        return word


print(string_count(collection))


def list_display():
    numbers_from_one_to_fifteen = []
    for index in range(1, 16):
        numbers_from_one_to_fifteen.append(index)
    return numbers_from_one_to_fifteen


print(list_display())


def duplicate_list_display():
    lst = list_display()
    temp = lst
    duplicated = lst + temp
    return duplicated


print(duplicate_list_display())


def remove_duplicate():
    remover = set(duplicate_list_display())
    return remover


print(remove_duplicate())


def add_third_elements(lst):
    sum = 0
    for index in range(2, len_of_list(lst), 3):
        sum += lst[index]
    return sum


print(add_third_elements(random_numbers()))


def sum_list_indexes(lst):
    sum = 0
    for index in range(0, len_of_list(lst)):
        sum = lst[0] + lst[-1] + ((lst[4] + lst[5]) / 2)
    return sum


print(sum_list_indexes(random_numbers()))


def numbers_collection():
    numbers = set()
    for number in range(1, 11):
        numbers.add(int(input("Enter score: ")))
    return numbers


print(numbers_collection())


def sum_collection(sett):
    total = sum(sett)
    return total


print(sum_collection(numbers_collection()))


def remove_item(sett, number):
    for _ in range(0, len_of_list(sett)):





def find_intersection(sett1, sett2):
    return sett1.intersection(sett2)


def find_union(sett1, sett2):
   return sett1.union(sett2)


def is_subset(sett1, sett2):
    return sett1.issubset(sett2)


def remove_element_(sett1):
    return sett1.clear()


def max_min(sett2):
    return f"maximum: {max(sett2)}, minimum: {min(sett2)}"


def length_of_seth(sett):
    count = 0
    for i in sett:
        count += 1
    return count


def empty_tup():
    score = ()


def