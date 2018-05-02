a = [1, 4, 5, 7, 8, 12]
b = [4, 5, 9, 12, 15, 2]

c = []
for element in a :
    if element in b :
        c.append(element)

print(c)
