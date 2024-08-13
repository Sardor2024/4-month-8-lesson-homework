from os import system
system("cls")

lst = []
while True:
    num = int(input("Son kiriting (0 kiritilsa to'xtaydi): "))  
    if num == 0:
        break  
    lst.append(num)

print("Kiritilgan sonlar:", lst)

for i in range(len(lst) - 1):  
    if lst[i] + 1 == lst[i + 1]:
        print(f"Juft sonlar: {lst[i]}, {lst[i + 1]}")


# extra vazifa 