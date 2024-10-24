print("Chao mung den CLB Tin Hoc HIT")

print("CLB Tin Hoc HIT truc thuoc Khoa CNTT - 10 diem")

str1 = "CLB Tin Hoc HIT truc thuoc Khoa CNTT "

for i in str1:
    if i.isupper():
        print(i,end = " ")
print()
for i in str1:
    if i.islower():
        print(i, end = " ")
print()

str2 = "CLB Tin Hoc HIT truc thuoc Khoa CNTT"
if "CNTT" in str2:
    print("Yes")
else:
    print("No")

str3 = "CLB Tin Hoc HIT truc thuoc Khoa CNTT"
for i in str3:
    if(i.islower()):
        i = i.upper()
        print(i, end = "")
    else:
        i = i.lower()
        print(i, end = "")
        