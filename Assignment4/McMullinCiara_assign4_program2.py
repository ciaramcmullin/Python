# Ciara McMullin
# Section 2
# Pick Up Sticks
# Assignment 4

# get number of sticks from user
sticks = 0
while True:
    
    sticks = int(input("How many sticks (10-100): "))
    if sticks >= 10 and sticks <= 100:
        print ("Great Let's play ...")
        print ()
        break
    elif sticks > 100:
        print ("Sorry, that's too many sticks. Try again.")
    elif sticks < 10:
            print ("Sorry, that's too few sticks. Try again.")

# make accumlator for turn
turn = 0

# create while loop for game
while sticks == 0 or sticks > 0:

    if turn == 0:
        if sticks == 0:
            print ("There are no sticks left on the table!  Game over. ")
            print ("Player 1 wins!")
            break

        else:
# create while loop for player 1
            while True:
             
                print ("Turn: Player 1")
                print ("There are ", sticks, " sticks on the table.")
                take = int(input("How many sticks do you want to take (1, 2 or 3)? "))
                if ((take == 1) or (take == 2) or (take ==3)) and sticks >= take:
                    sticks = sticks - take
                    turn += 1
                    print ()
                    break
                else :
                    print ("Sorry, that's not a valid number.")
                    print ()
                    
                
        if turn == 1:
            if sticks == 0:
                print ("There are no sticks left on the table!  Game over. ")
                print ("Player 2 wins!")
                break
            else:
# create while loop for player 2
                while True:
                    print ("Turn: Player 2")
                    print ("There are ", sticks, "on the table.")
                    take = int(input("How many sticks do you want to take (1, 2 or 3)? "))
                    if ((take == 1) or (take == 2) or (take == 3)) and sticks >= take :
                        sticks = sticks - take
                        turn -= 1
                        print ()
                        break
                    else :
                        print ("Sorry, that's not a valid number.")
                        print ()
                    


            
            
        
