a = [3, -1, 5, 3, 8, -2, 5]
sos = ["Datan", "Batan", "Tatan", "Saveliy"]
tas = 7
pop = 2

#1
b = sum(a)
print(b)

#2
c = max(a)
print(c)

#3
d = sum(1 for x in a if x % 2 == 0)
print(d)

#4
e = [x * 2 for x in a]
print(e)

#5
f = max(sos, key=len)
print(f)

#6
g = [x for x in a if x >= 0]
print(g)

#7
h = list(set(a))
i2 = sorted(h)[-2]
print(i2)

#8
j2 = a[::-1]
print(j2)

#9
k = set()
l = []
for x in a:
    if x not in k:
        l.append(x)
        k.add(x)
print(l)

#10
n = a == a[::-1]
print(n)

#11
o = [x for x in a if x % 2 == 0]
p = [x for x in a if x % 2 != 0]
print("Чётные:", o)
print("Нечётные:", p)

#12
q = []
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] + a[j] == tas:
            q.append((a[i], a[j]))
print(q)

#13
r = sos[:]
for i in range(len(r)):
    for j in range(i + 1, len(r)):
        if len(r[i]) > len(r[j]):
            r[i], r[j] = r[j], r[i]
print(r)

#14
s = t = a[0]
for x in a[1:]:
    t = max(x, t + x)
    s = max(s, t)
print(s)

#15
pop = pop % len(a)
u = a[-pop:] + a[:-pop]
print(u)