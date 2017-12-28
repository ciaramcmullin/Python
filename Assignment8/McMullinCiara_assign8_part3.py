# Ciara McMullin
# Assignment 8

# Part 3

# make lists for cards, values, comp, and comp values
cards  = ['10 of Hearts', '9 of Hearts', '8 of Hearts', '7 of Hearts', '6 of Hearts', 
          '5 of Hearts', '4 of Hearts', '3 of Hearts', '2 of Hearts', 'Ace of Hearts', 
          'King of Hearts', 'Queen of Hearts', 'Jack of Hearts', '10 of Diamonds', 
          '9 of Diamonds', '8 of Diamonds', '7 of Diamonds', '6 of Diamonds', 
          '5 of Diamonds', '4 of Diamonds', '3 of Diamonds', '2 of Diamonds', 
          'Ace of Diamonds', 'King of Diamonds', 'Queen of Diamonds', 'Jack of Diamonds', 
          '10 of Clubs', '9 of Clubs', '8 of Clubs', '7 of Clubs', '6 of Clubs', 
          '5 of Clubs', '4 of Clubs', '3 of Clubs', '2 of Clubs', 'Ace of Clubs', 
          'King of Clubs', 'Queen of Clubs', 'Jack of Clubs', '10 of Spades', 
          '9 of Spades', '8 of Spades', '7 of Spades', '6 of Spades', '5 of Spades', 
          '4 of Spades', '3 of Spades', '2 of Spades', 'Ace of Spades', 
          'King of Spades', 'Queen of Spades', 'Jack of Spades']

values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 
          10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, 10, 9, 8, 7, 6, 5, 
          4, 3, 2, 1, 10, 10, 10]
computers = ['10 of Hearts', '9 of Hearts', '8 of Hearts', '7 of Hearts', '6 of Hearts', 
          '5 of Hearts', '4 of Hearts', '3 of Hearts', '2 of Hearts', 'Ace of Hearts', 
          'King of Hearts', 'Queen of Hearts', 'Jack of Hearts', '10 of Diamonds', 
          '9 of Diamonds', '8 of Diamonds', '7 of Diamonds', '6 of Diamonds', 
          '5 of Diamonds', '4 of Diamonds', '3 of Diamonds', '2 of Diamonds', 
          'Ace of Diamonds', 'King of Diamonds', 'Queen of Diamonds', 'Jack of Diamonds', 
          '10 of Clubs', '9 of Clubs', '8 of Clubs', '7 of Clubs', '6 of Clubs', 
          '5 of Clubs', '4 of Clubs', '3 of Clubs', '2 of Clubs', 'Ace of Clubs', 
          'King of Clubs', 'Queen of Clubs', 'Jack of Clubs', '10 of Spades', 
          '9 of Spades', '8 of Spades', '7 of Spades', '6 of Spades', '5 of Spades', 
          '4 of Spades', '3 of Spades', '2 of Spades', 'Ace of Spades', 
          'King of Spades', 'Queen of Spades', 'Jack of Spades']
computer_values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 
          10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, 10, 9, 8, 7, 6, 5, 
          4, 3, 2, 1, 10, 10, 10]

# create new lists to append; import random function
hand = []
hand_values = []
hand_computer = []
computer_value = []
import random

# do first two cards for player
card1 = random.choice(cards)
location = cards.index(card1)
value1 = values[location]
cards.remove(card1)
values.remove(value1)
hand.append(card1)
hand_values.append(value1)

card2 = random.choice(cards)
location = cards.index(card2)
value2 = values[location]
cards.remove(card2)
values.remove(value2)
hand.append(card2)
hand_values.append(value2)

# create for loop for total
total = 0
for i in hand_values:
    total += int(i)
    
# print total
print ("Player hand: ", hand, " is worth ", total)

# create while loop for game
while total <= 21:
    move = input("(h)it or (s)tand? ")
    if move == "h":
        card = random.choice(cards)
        location = cards.index(card)
        value = values[location]
        cards.remove(card)
        values.remove(value)
        hand.append(card)
        hand_values.append(value)
        total += int(value)
        print ("You drew ", card)
        print ("Player hand: ", hand, " is worth ", total)
        if total > 21:
            print ("Bust!")
            print ("Computer Wins!")
            break
    if move == "s" and total < 21:
        card1 = random.choice(computers)
        location = computers.index(card1)
        value1 = computer_values[location]
        computers.remove(card1)
        computer_values.remove(value1)
        hand_computer.append(card1)
        computer_value.append(value1)

        card2 = random.choice(computers)
        location = computers.index(card2)
        value2 = computer_values[location]
        computers.remove(card2)
        computer_values.remove(value2)
        hand_computer.append(card2)
        computer_value.append(value2)

        comp_total = 0
        for i in computer_value:
            comp_total += int(i)
        print ("Computer hand: ", hand_computer, " is worth ", comp_total)
        while True:
            new_card = random.choice(computers)
            location = computers.index(new_card)
            new_value = computer_values[location]
            computers.remove(new_card)
            computer_values.remove(new_value)
            hand_computer.append(new_card)
            computer_values.append(new_value)
            print ("Computer drew ", new_card)
            comp_total += int(new_value)
            if comp_total == 21:
                print ("Dealer hand ", hand_computer, " is worth ", comp_total)
                print ("Computer got 21!  Blackjack!")
                print ("Computer wins!")
                break
            elif comp_total > 21:
                print ("Bust!", "\n", "Player wins!")
                break
            elif comp_total > total:
                print ("Computer hand: ", hand_computer, " is worth ", comp_total)
                print ("Computer wins!")
                break
        break
                
                
            
            
            
        
        
        
