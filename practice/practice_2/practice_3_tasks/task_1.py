a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

a.extend(b)
print(a.count(5))

while 5 in a:
    a.remove(5)

a.extend(c)

print(a.count(3))
print(a)
