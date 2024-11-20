n = int(input("So luong key, value: "))

dict = {}

for i in range(n):
    key = input("input key: ")
    value = input("value: ")
    dict[key] = value

new_dict = {}

for key,value in dict.items():
    if value in new_dict:
        print("None")
    new_dict[value] = key

print(new_dict)
