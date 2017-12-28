#Ciara McMullin
# assignment 7
# section 2
# part 2

#part 2b
name = input("Name: ")
new_name = name.lower()

name_good = ""       
for i in new_name:
    if i.isalpha() == True:
         name_good += i
       
print ("Your 'cleaned up' name is: ", name_good)

total = 0
length = len(name_good)
num = 0
for character in name_good:
    number = ord(character)-96
    num += 1
    while num != length:
        total += number
        print (str(number), end = " + ")
        break
    if num == length:
        total += number
        print (number, "=", total)


    
