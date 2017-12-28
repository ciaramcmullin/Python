# Ciara McMullin
# Intro to Computer Programming


# create while loop for start and end number
while True:
    start = int(input("Start number: "))
    end = int(input("End number: "))
    if start <= 0 or end <= 0:
        print ("Start and end must be positive")
    elif end <= start:
        print ("End number must be greater than start number")
    else:
        break
# create for loop for range
total = 0   
for num in range (start, end + 1):
    total += 1
    if num > 1:
        for i in range (2,num):
            if (num % i) == 0:
                break
        else:
            if total == 10:
                print ("\n", num)
            else:
                print (num, end = "\t")
        
