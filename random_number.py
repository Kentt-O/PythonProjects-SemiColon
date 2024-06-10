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


def largest():
    largest = 0
    for index in range(0, len_of_list()):



