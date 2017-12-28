# Ciara McMullin
# Section 2
# Roll the Dice
# Assignment 4

# get sides of dice
while True:

    sides = int(input("How many sides on your dice (4, 6, 8, 10, 12 or 20)? "))
    if (sides == 4) or (sides == 6) or (sides == 8) or (sides == 10) or (sides == 12) or (sides == 20) :
        print ("Thanks! Here we go ...")
        break
    else:
        print ("Sorry, thats not a valid size.")
        print ()
        
# get random int from sides

rolls = 0
doubles = 0
die1 = 0
die2 = 0
total1 = 0
total2 = 0
while True:
    import random
    
    number1 = random.randint(1, sides)

    number2 = random.randint(1, sides)
# get accumlator for rolls, dies and doubles
    rolls = rolls + 1

    die1 = die1 + 1

    die2 = die2 + 1

    total1 += number1

    total2 += number2
    
    print (rolls, ". die number 1 is ", number1, " and die number 2 is ", number2, sep = "")
    
    if number1 == number2 :
        doubles = doubles + 1

        
# if true break the while loop
    if number1 == 1 and number2  == 1 :
        print ()
        print ("You got snake eyes! Finally! On try number ", rolls, "!", sep = "")
        double_percent = format (((doubles / rolls) * 100), '.2f')
    
        die1_avg = total1 / (rolls)
        die2_avg = total2 / (rolls)
        print ("Along the way you rolled doubles ", doubles, " times. (", double_percent, "% of all rolls were doubles)", sep = "")
        print ("The average roll for die #1 was", format (die1_avg, ".2f" ))
        print ("The average roll for die #2 was", format (die2_avg, ".2f" ))

        break
    

        
        
        




