a = [4, -1, 4, -3, 8, 2, 5]
sos = ["Datan", "Batan", "Tatan", "Saveliy"]

#1
b = sum(a)
print(b)

#2
c = max(a)
print(c)

#3
summ = 0
for i in a:
    if i % 2 == 0:
        summ += 1
print(summ)

#4
a2 = [3, -1, 5, -3, 8, 2, 5]
for i in range(len(a2)):
    a2[i] *= 2
print(a2)

#5

#6
for i in a:
    if i <= 0:
        a.remove(i)
print(a)

#7
for i in a:
    if a[i] >= i:
        print(a[i])

#8

#9