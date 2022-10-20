# алгоритм вставка ( если список уже отсортирован+)
# insert sorting algorithm

#ls = [6, 4, 7, 5, 9, 1, 3, 4, 8, 9]
ls = [1, 2, 6, 3, 4, 5, 7, 8, 9, 10]
count = 0
for i in range(1, len(ls)):
    item = ls[i]
    j = i - 1
    while item < ls[j] and j >= 0:
        count += 1
        ls[j + 1] = ls[j]
        j -= 1

    ls[j + 1] = item

print(ls)
print("count =", count)
