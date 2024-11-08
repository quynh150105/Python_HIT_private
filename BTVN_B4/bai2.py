n = int(input("n= "))
a = [input() for i in range(n)]
print(a)

m = int(input("m= "))
b = [input() for i in range(m)]
print(b)

c = list()

i,j = 0,0

while i < n or j < m:
    if i < n:
        c.append(a[i])
        i = i+1
    if j < m:
        c.append(b[j])
        j = j+1

print(c)
