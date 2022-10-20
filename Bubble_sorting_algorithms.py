# Алгоритмы сортировки
# обмен, выбор и вставка

# bubble sorting algorithm


# ls = [6, 4, 7, 5, 9, 1, 3, 4, 8, 9]
ls = [1, 2, 6, 3, 4, 5, 7, 8, 9, 10]
count = 0  # debug

for j in range(len(ls) - 1):
    flag = True

    for i in range(
            len(ls) - 1 - j):  # тк последнряя итерация не нужна, мы заканчиваем сравнение на предпоследнем элементе
        count += 1  # debug
        if ls[i] > ls[i + 1]:
            flag = False
            t = ls[i]
            ls[i] = ls[i + 1]
            ls[i + 1] = t
    if flag:
        break

print("count =", count)
print(ls)
