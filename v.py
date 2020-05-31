import random

secret = random.randrange(1,101)

guess = 0
tries = 0
while guess != secret:
    guess = int(input("make a guess!:]"))
    tries = tries + 1 

    if guess > secret:
        print("too high!:o")
    elif guess < secret:
        print("too low!:(")
    else:
        print ("good!:)")
    if guess > 101:
        print("remember, the guess is always < 101.:| ")
        

print("number of tries you took: :] ", tries)
    
