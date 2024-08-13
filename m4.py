from os import system
system('cls')

def func(matn, left_hand, right_hand):
    lst_right = []
    lst_left = []

    for item in matn:
        if item in left_hand:
            lst_left.append(item)
        elif item in right_hand:  
            lst_right.append(item)
    
    return (lst_left), (lst_right)

with open("istalgan.txt", "r") as file:
    matn = file.read()
    
left_hand = ['q','a','z','w','s','x','e','d','c','r','f','v','t','g','b','1','2','3','4']
right_hand = ['6','7','y','u','h','j','m','n','8','i','k',',','9','o','l','.','0','p',';','/','-','=','[',']','"','?']

natija_left, natija_right = func(matn, left_hand, right_hand)

print("Left:", natija_left)
print("Right:", natija_right)

