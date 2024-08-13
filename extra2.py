from os import system
system("cls")

data = input("malumotni kiriting (misol un:behruz:1,vali:0): ")
dct = dict(item.split(":") for item in data.split(","))
winner = []
loser = []

print("Dictionary:", dct)
for key, value in dct.items():
    if int(value) == 0:  
        loser.append((key)) 
    else:
        winner.append((key)) 

print("winner 1 :", winner)
print("loser  0 :",loser)

#extra 2




