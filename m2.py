from os import system
from json import dumps

system("cls")

def bigger1(bigger_price, n):
    sorted_func = sorted(bigger_price, key=lambda p: p["price"], reverse=True)
    return sorted_func[:n]

n = int(input("nechta qiymat chiqarilsin: "))   
print(n)

bigger_price = [
    {"name": "bread", "price": 100},
    {"name": "wine", "price": 138},
    {"name": "meal", "price": 142},
    {"name": "pen", "price": 97}
]

natija = bigger1(bigger_price, n)
print(natija)
#uyga vazifa 2