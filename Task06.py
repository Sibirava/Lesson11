a = [1, 2, 3, 4, 5]
b = a

b = a.copy()
b = a[:]
a[3] = 100

#a[:3] = [0] #--> 4 и 5 заменили на ноль
#a[3] = 100 #--> 4ку заменили на 100

print(a)
print(b)

# a = 5
# print(type(a))
# b = a
# a = 10
# print(a)
