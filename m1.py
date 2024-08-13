from os import system
from json import dumps
system("cls")


def func(son:str):
    dct={}
    for raqam in son:
        if not raqam.isdigit():
            continue
        if not dct.get(raqam):
            dct[raqam]=1
        else:
            dct [raqam]+=1
    return dct

son=str(input("sonni kiriting:"))
natija=func(son)

sorted=dict(sorted(natija.items()))

print(dumps(sorted,indent=4))
#uyga vazifa 1