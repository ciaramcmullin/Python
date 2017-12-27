# Problem #2: Guess the Number Game
# Ciara McMullin
# 9/26/16
# Section 2

print ("I'm thinking of a number between 1 and 10!")

# make all of the functions in the "random" module
import random

# pick a random integer between 1 and 10
number = random.randint(1, 10)

# ask user for number between 1 and 10
guess = int(input("What's your guess? " ))

# see if user guessed right
if number == guess :
    print ("You got it!")
    print ("The secret number was ", number, ".", sep="")
    print ("It took you 1 try to guess the number.")
    
elif number > guess:
    print ("Too low, try again.")
    guess = int(input("What's your guess? " ))
    if number == guess:
        print ("You got it!")
        print ("The secret number was ", number, ".", sep="")
        print ("It took you 2 tries to guess the number.")
    elif number > guess:
        print ("Too low, try again.")
        guess = int(input("What's your guess? " ))
        if number == guess :
            print ("You got it!")
            print ("The secret number was ", number, ".", sep="")
            print ("It took you 3 tries to guess the number.")
        elif number != guess :
            print ( "The secret number was ", number, ".", sep="")
            print ("You didn't guess the number.")
    elif number < guess:
        print ("Too high, try again.")
        guess = int(input("What's your guess? " ))
        if number == guess :
            print ("You got it!")
            print ("The secret number was ", number, ".", sep="")
            print ("It took you 3 tries to guess the number.")
        elif number != guess :
            print ( "The secret number was ", number, ".", sep="")
            print ("You didn't guess the number.")      
        
elif number < guess:
    print ("Too high, try again.")
    guess = int(input("What's your guess? " ))
    if number == guess:
        print ("You got it!")
        print ("The secret number was ", number, ".", sep="")
        print ("It took you 2 tries to guess the number.")
    elif number > guess:
        print ("Too low, try again.")
        guess = int(input("What's your guess? " ))
        if number == guess :
            print ("You got it!")
            print ("The secret number was ", number, ".", sep="")
            print ("It took you 3 tries to guess the number.")
        elif number != guess :
            print ( "The secret number was ", number, ".", sep="")
            print ("You didn't guess the number.")
    elif number < guess:
        print ("Too high, try again.")
        guess = int(input("What's your guess? " ))
        if number == guess :
            print ("You got it!")
            print ("The secret number was ", number, ".", sep="")
            print ("It took you 3 tries to guess the number.")
        elif number != guess :
            print ( "The secret number was ", number, ".", sep="")
            print ("You didn't guess the number.")
    
