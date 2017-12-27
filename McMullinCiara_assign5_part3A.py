# Ciara McMullin
# Intro to computer programming
# section 2

# create while loop to get positive number
while True:
    number = int(input("Enter a positive number to test: "))
    if number <= 0:
        print ("Sorry try again!")
    else:
        break
if number == 1:
    print ("1 is not a prime number")
start = 2

# create for loop to see if prime number
for i in range (2, number):
    if (number % i == 0) and i != number:
        print (i, "is a divisor of ", number, " ... stopping")
        print (number, "is not a prime number.")
        break
               
    else:
        print ( i, "is NOT a divisior of ", number, "...continuing")
        if (number - 1) == i:
            print ()
            print (number, "is a prime number!")

        
        
    
    
    
