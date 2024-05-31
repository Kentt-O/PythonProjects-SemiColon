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


