from os import system
system("cls")

lst = []
while True:
    num = int(input("son kiriting (0 kirtilsa toxtaydi): "))  
    if num == 0:
        break  
    lst.append(num)

print("kiritilgan sonlar:", lst)

for i in range(len(lst) - 1):  
    if lst[i] + 1 == lst[i + 1]:
        print(f"para sonlar: {lst[i]}, {lst[i + 1]}")


# extra 1