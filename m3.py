from os import system
system("cls")

def func(number: str):
    count = 0
    for raqam in number:
        if raqam == '0':
            count += 1
        else:
            break  
    return count

son = input("Sonnni kiriting: ")
natija = func(son)
print(natija,"ta 0 bor ")


#uyga vazifa 3