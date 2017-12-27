# Using the print function
# Ciara McMullin
# 9/19/16
# Section 02


# get three names from the user

name1 = input("Please enter name #1: ")
name2 = input("Please enter name #2: ")
name3 = input("Please enter name #3: ")
print ()
print ("Here are your names in every possible order: ")
print ("--------------------------------------------")
print ()
# display the names back to user in every possible order

print ("1.", name1 + ",", name2 + ",", name3)
print ()
print ("2.", name1 + ",", name3 + ",", name2)
print ()
print ("3.", name2 + ",", name1 + ",", name3)

print ()
# display the names back to user with new lines per name
print ("4.", name2)
print (name3)
print (name1)
print ()
print ("5.", name3)
print (name2)
print (name1)
print ()
print ("6.", name3)
print (name1)
print (name2)


