# Ciara McMullin
#intro to programming section 2
# assignment 6


# import functions and random

import myfunctions
import random


# PART 2G

# ask for problems

while True:
    problems = int(input("How many problems would you like to attempt? "))
    if problems <= 0:
        print("Invalid number, try again")
    else:
      break

# get width
while True:
    width= int(input("How wide do you want your digits to be? 5-10: "))
      
    if (width < 5) or (width > 10):
        print ("Invalid width, try again")
    else:
        break

print("Here we go!")

# create accumlator
# create for loop

correct_answers = 0
num = 1
while num <= problems:
    num +=1
    print ("What is .....")
    a = random.randint(0,9)
    b = random.randint(0,9)
    c = random.randint(1,2)
    myfunctions.print_number(a, width)
    if c == 1:
        print (myfunctions.plus(width))
        c = "+"
    else:
        print(myfunctions.minus(width))
        c="-"
    myfunctions.print_number(b,width)
    problem_answer = int(input("= "))

    check_problem = myfunctions.check_answer(a,b,problem_answer,c)
    if check_problem == True:
        correct_answers += 1
        print("Correct!")

    elif check_problem == False:
        print ("Sorry, that's not correct.")

print ()
print ("You got ", correct_answers, "out of ", problems, "correct!")

        
   


    
            
    
