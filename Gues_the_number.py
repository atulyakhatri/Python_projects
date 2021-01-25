#Guess the number game
print("You have to comlete this in 5 rounds")
n = 18
y = 5
while(y):
    x = int(input("Enter the number:\n"))
    y -= 1
    if x == n:
        print("Congratulations! you got this")
        print("You got this in",5-y,"round" )
        break
    elif x >= n:
        print("This number is larger than expected\nTry smaller number")
        print(y,"Rounds left")
        if y ==0:
            print("Game over")
    elif x <= n:
        print("This number is smaller than expected\nTry larger number")
        print(y,"Rounds left")
        if y ==0:
            print("Game over")
        continue
        
