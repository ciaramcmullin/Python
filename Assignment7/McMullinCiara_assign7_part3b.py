#Ciara McMullin
# assignment 7
# section 2
# part 3
import McMullinCiara_assign7_part3a

while True:
    option = input("(e)ncode, (d)ecode or (q)uit: ")
    if option == "q":
        break
    elif option == "e":
        num = int(input("Enter a number between 1 and 5: "))
        if num > 5 or num < 1:
            print ("Sorry try again!")
        else:
            word = input("Enter a phrase to encode: ")
            new_word = add_letters(word, num)
            final = shift_characters(new_word, num)
            print ("Your encoded word is: ", final)
    elif option == "d":
        num = int(input("Enter a number between 1 and 5: "))
        if num > 5 or num < 1:
            print ("Sorry try again!")
        else:
            word = input("Enter a phrase to decode: ")
            new_word = remove_letters(word,num)
            final = shift_characters(new_word,(-num))
            print ("Your decoded word is: ", final)
            
        
    
