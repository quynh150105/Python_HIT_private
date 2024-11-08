n = int(input("n= "))
num_list1 = [int(input()) for i in range(n)]
print(num_list1)

m = int(input("m= "))
num_list2 = [int(input()) for i in range(m)]
print(num_list2)

answer = []

for i in range(n):
    if num_list1[i] in num_list2 :
        answer.append(num_list1[i])
print(answer)
