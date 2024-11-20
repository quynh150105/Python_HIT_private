#danh sach cac ban da dang ki
A = {"A","D","C","B","Q","E","K","F"}
#danh sach cac ban da checkin
B = {"A","C","D","G","E"}

print("Danh sach cac ban chua checkin la:", A-B)

tong = int((len(A) + len(B)))
print("So luong cac ban da dang ki va checkin: ", tong)

A = list(A)
A.sort()
print("Danh sach cac ban da dang ki la: ",A)
