#importing the modules
import string
import random
import re
from functools import reduce

def password(): #creating a password generating function 
    """This is a password generator"""
    store = [] #It will contain passwords
    for i in range(4):# using string module to generate the password
        cap = random.choice(string.ascii_uppercase)
        store += cap
        small = random.choice(string.ascii_lowercase)
        store += small
        digit = random.choice(string.digits)
        store += digit
        punct = random.choice(string.punctuation)
        store += punct
    random.shuffle(store)# Shuffling it
    random.shuffle(store)# Shuffling it again 
    word = reduce((lambda x,y:x+y),store)#Making the password a string
    return word

def w_checker(test):# Checking the password
    "This is a password checker"
    string_check= re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    digit_check = re.compile("[1234567890]")
    cap_check = re.compile("[ABCDEFGHIJKLMNOPQRSTUVWXYZ]")
    small_check = re.compile("[abcdefghijklmnopqrstuvwxyz]")
    if test.isspace() == True:
        print("Please enter a password ")
    if len(test) > 16:# password should contain below or eual to 16 characters
        print("Don't enter a password above 16 characters")
    if len(test) < 4:# password should not contain less than 4 characters
        print("Don't enter a password below 4 characters")
    if(string_check.search(test) == None):# it should contain special characters
        print("Enter any of the special characters")
    if (digit_check.search(test) ==None):# it should contain digits
        print("Enter any of the digits")
    if (cap_check.search(test) ==None):# it should contain capital letters
        print("Enter any of the Capitals")
    if (small_check.search(test) == None):#It should contain small letters
        print("Enter any of the small")

def gen_check():#creating  a function for generating and checking the password
    word = input("Enter password or we can suggest enter suggest for suggestion:\n")
    #Getting the password from the user
    if word== "suggest":#Asking for password suggestion
        print(f"This is your password '{password()}'")
        print("Thanks")
    else:#Checking the user given password
        w_checker(word)
        print("Fine")
    
    

if __name__ == "__main__":
    gen_check()
