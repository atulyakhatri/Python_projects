import random 
Snake = "s"
Water= "w"
Gun = "g"
print("Welcome to snake water gun game")
c =0
while(1):
    c +=1
    ask = input("Enter s for sanke, w for water,g for gun:\n")
    choiceList = [Snake,Water,Gun]
    choice = random.choice(choiceList)
    if ask=="s" and choice == Snake:
        print("draw")
        continue
    elif ask=="w" and choice == Water:
        print("draw")
        continue
    elif ask=="g" and choice == Gun:
        print("draw")
        continue
    elif ask == "s" and choice == Gun:
        print("You lost the match")
        continue
    elif ask == "w" and choice == Snake:
        print("You lost the match")
        continue
    elif ask == "g" and choice == Water:
        print("You lost the match")
        continue
    elif ask == "s" and choice == Water:
        print("You won the match ",end =" ")
        break
    elif ask == "w" and choice == Gun:
        print("You won the match ",end=" ")
        break
    elif ask == "g" and choice == Snake:
        print("You won the match ",end =" ")
        break
    else:
        print("Enter a valid letter")
        continue
print(f"\bin {c} times")