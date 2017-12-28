#Ciara McMullin
# assignment 7
# section 2
# part 1

#part a
while True:
    name = input("Enter a username: ")

    # determine the size of username
    length = len(name)
    print ("* Length of username: ", length)

    # see if name is alpha-numeric
    if name.isalnum ()== True:
        print ("* All characters are alpha-numeric: True")
    else:
        print ("* All characters are alpha-numeric: False")

    # test for 1st character
    if name[0].isdigit == True or name[-1].isdigit() == True:
        print ("* First & last characters are not digits: False")
    else:
        print ("* First & last characters are not digits: True")
        
    uppers = 0
    lowers = 0
    digits = 0

    # look at each character
    # see what kind they are

    for c in name:
        if c.isupper()== True:
            uppers += 1
        if c.islower() == True:
            lowers += 1
        if c.isdigit() == True:
            digits += 1
    print ("* # of uppercase characters in the username: ", uppers)
    print ("* # of lowercase characters in the username: ", lowers)
    print ("* # of digits in the username: ", digits)

    # see if username is good

    if (length >= 8) and (length <= 15) and (name.isalnum() == True) and (name[0].isdigit() == False) and (name[-1].isdigit() == False) and (uppers > 0) and (lowers > 0) and (digits > 0):
        print ("Username is valid!")
        break
    else:
        print ("Username is invalid, please try again")


   
