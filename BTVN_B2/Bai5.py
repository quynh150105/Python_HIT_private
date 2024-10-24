#a
a = int(input("nhap so a: "))
count = 0
while( a != 0):
    a = a//8
    count += 1*3
print(count)

#b
a = int(input())

b = dir(a)

for i in b:
    print(i)

