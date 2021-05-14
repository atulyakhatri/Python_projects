import random

print("\nGuess-the-number\n")

name = input("Enter your name:\n")
comp = random.randrange(100)

points = 10

com = 0
def score():
    global guess,com,points
    if guess> comp:
        com = 1
        points -= 1
        
    elif guess < comp:
        com= 0
        points -= 1

def file_create():
    global final
    content = str({name:points})
    try:
        f = open(f"{name}.txt","xt")
        app = f.write(content)
        f.close()
    except:
        f = open(f"{name}.txt","at")
        char = f.tell()
        f.seek(char)
        app = f.write(content)
        f.close()
    finally:
        try:
            a = open("base.txt","xt")
            a.write({f"{name}:{points}"})
            a.close()
        except:
            a = open("base.txt","at")
            sen = a.tell()
            a.seek(sen)
            a.write(f"{name}:{points}\n")
            a.close()
        f = open(f"{name}.txt")
        final = f.read()
        f.close()

def main():
    global guess,final,com
    
    guess = int(input("Enter a number between 1 and 100:\n"))
    if guess > 100 or guess <0:
        raise ValueError("Please enter number between 1 and 100")
    
    a = True
    while a:
        score()
        if com == 1:
            guess = int(input(f"Enter a number below {guess}\n"))
        else:
            guess = int(input(f"Enter a number above {guess}\n"))
            
        if points == 0:
            print("You lost the game!")
            a = False
        if guess == comp:
            print("Won!")
            a = False
        
    file_create()
    print(f"You won by {points} points\nYour records are {final}")
    
if __name__ == "__main__":
    main()
