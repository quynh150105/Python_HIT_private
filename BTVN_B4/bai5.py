n = int(input("n= "))
a = [int(input()) for i in range(n)]

x = int(input("x can tim:  "))
a.sort()

L =0
R = len(a)-1
Mid = int((L+R)/2)

check=0

while(a[Mid]!=x):
    check+=1
    if(a[Mid]<x):
        L = Mid
    else:
        R = Mid
        
    Mid = int((L+R)/2)

    if(check==n):
        mid=-1
        break

print(Mid)