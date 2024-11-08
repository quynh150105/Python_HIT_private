k = int(input("nhap k: "))
a = [int(input()) for i in range(k)]
print(a)

n = int(input("nhap n: "))
m = int(input("nhap m: "))

if n*m <= k:
    answer = []
    index = 0
    for i in range(n):
        row =[]
        for j in range(m):
            row.append(a[index])
            index +=1
        answer.append(row)
    print(answer)