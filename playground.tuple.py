tuple1 = (1, "ojo", 2, 3, [])
#tuple1[4].append(5)
tuple1[4].extend([1, 3, "kent"])

tuple1 = tuple1 + (1, 6)
tuple1 += (1, 6)

names = ["Afeez", "Eniola", "Janet"]
names += tuple1
names = tuple(names)

# print(names.index("Afeez"))
# print(names)
# print(tuple1)

# Set - a set does not allow duplicate element
x = {1, 2, 1, 3, 2, 2, 4, 5, 1}
# empty curly braces should not be used to declare an empty set
y = set()
# you can use subscription  on sets [you cant pick an element by their index]
y = {1, 3, 7, 9, 10, 2}
x.add(10)
print(x.difference(y))

# stack has a last in first out concept
# queue has a first in first out concept
