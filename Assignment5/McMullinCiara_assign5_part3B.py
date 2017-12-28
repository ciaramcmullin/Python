# Ciara McMullin
# Intro to programming




# create for loop for all prime numbers

print ("1 is technically not a prime number")
for num in range(2,1001):
    for i in range(2,num):
        if (num % i == 0):
            break
    else:
        print(num, "is a prime number!")
