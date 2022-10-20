# сортировка выбор

ls = [6, 4, 7, 5, 9, 1, 3, 4, 8, 9]
count = 0
for j in range(len(ls) - 1):
    index_min_value = j

    for i in range(j + 1, len(ls)):
        count += 1
        if ls[i] < ls[index_min_value]:
            index_min_value = i

    ls[j], ls[index_min_value] = ls[index_min_value], ls[j]

print(ls)
print("count =", count)