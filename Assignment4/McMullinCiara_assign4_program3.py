# Ciara McMullin
# Section 2
# Arrows
# Assignment 4


# create variable star
star = 0
r = 1
l = 2

# get integer from user
while True:
    col = int(input("How many columns? "))
    direction = input("Direction? (l)eft or (r)ight: ")
    if col > 0 and (direction == "l" or direction == "r"):
        break
    elif col <= 0 or (direction != "l") or (direction != "r") :
        print ("Invalid entry, try again!")
            
# right direction
if direction == "r":
    
    while star < (col - 1):
        print (" " * star, "*")
# have stars accumlator go up by 1 each time
        star += 1

# create while loop for second half of stars
    while col > 0:
        print (" " * (col-1), "*")
# create stars accumlator that decreases by 1 each time
        col -= 1

# new variables
col2 = col
star = 1


# left direction
if direction == "l":

# while loop for first half
    while col > 0:
        print (" " * (col - 1), "*")
        col -=1
# while loop for second half
    while star <= (col2 - 1):
        print (" " * star, "*")
        star += 1


    

    
    
        


