n = int(input("Nhap so dai cho 2 tuple: "))

print("Nhap tuple A: ")
A = tuple(int(input()) for i in range(n))
print("Nhap tuple B: ")
B = tuple(input() for i in range(n))

tbc = sum(A)/len(A)
count = 0
for i in A:
    if i > tbc:
        count += 1
print("tbc la: ", tbc)
print("So ptu lon hon tbc la: ",count)

tup_chan = tuple(i for i in A if i%2==0)
tup_le = tuple(i for i in A if i%2 ==1)
print("tup_chan la: ", tup_chan)
print("tup_le la: ", tup_le)

k = input("ki tu k can tim la: ")
print("so lan xuat hien cua k trong B la: ",B.count(k))

temp = tuple(i for i in B if len(i) >= 5)
print("so phan tu co do dai >= 5 la: ",temp)

C = tuple(zip(A,B))
print("tuple C la: ", C)
