# If question == True:
a = [1, 1, 1, 6, 2, 2, 2, 4, 3, 2, 2, 6, 4, 6]
b = [1, 2, 5]

c = len(a) - 1
for i in a[::-1]:
    if i in b:
        a.pop(c)
    c -= 1
print(a)
