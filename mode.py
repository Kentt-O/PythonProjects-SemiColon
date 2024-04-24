iscore = [1, 2, 2, 3, 4]
jscore = [3, 4, 4, 5, 6]

print(max(set(iscore), key=iscore.count))
print(max(set(jscore), key=jscore.count))