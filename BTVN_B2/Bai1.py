a = int(input())
b= int(input())
#a
print ("a+b= " ,a+b)
#b
print("a-b=" , a-b)
#c
print("a*b=" , a*b)
#d
print("a//b= ", a//b)
#e
print("a**b=", a**b )
#f
print("a%b=", a%b)
#g
if a > b:
     print("a > b")
elif a < b:
     print("a < b")
else:
    print("a == b")
#h
print("a and b: " , a and b )
#i
print("a or b : ", a or b)
#j
print("a xor b = ",a ^ b)
#k
print("NOT (a == b) = ", not (a == b))
#l
print("a >> 5 = ",a >> 5)
#m
print("a << 6 = ",a << 6)
#n
awn = bin(a)[2:][::-1]
print("he co so 2 dao nguoc cua a: " + awn)