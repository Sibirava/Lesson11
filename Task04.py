ls = [6, 4, 7, 5, 9, 1, 3, 4, 8, 9]

print("Before: ", ls)

ls.sort()   #стандартная сортировка сортирует по возрастанию, если ничего не передавать ю reverse false -  по возрастанию

print("After sorting: ", ls)

ls.sort(reverse = True)
print("After another sorting: ", ls)
