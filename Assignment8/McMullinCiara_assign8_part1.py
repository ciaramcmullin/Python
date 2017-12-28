# Ciara McMullin
# Asssignment 8

#create while loop for number
while True:
    n = int(input("Enter an integer number greater or equal 10: "))
    if n < 10:
        print ("Sorry try again!")
    else:
        break

# create lists
flags_list = ["P"]                     
flags_list = flags_list * (n + 1)      

flags_list[0] = "N"                    
flags_list[1] = "N"                    



# create for loops and prime list
for i in range(2, n + 1):
    if flags_list[i] == "P":
        for j in range(2 * i, n + 1, i):
            flags_list[j] = "N"



primes = []                            

for i in range(2, n + 1):
    if flags_list[i] == "P":
        primes.append(i)

# create for loop and print results
i = 0                       
print()

for prime in primes:
    if i < 10:
        print(prime, end = "\t")
        i = i + 1
    else:
        print()
        print (prime, end ="\t")
        i = 1
        
