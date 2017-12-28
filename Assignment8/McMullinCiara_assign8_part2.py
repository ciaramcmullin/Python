# Ciara McMullin
# Assignment 8
# part 2

#product lists
product_names = ["salad", "chicken", "fruit"]
product_costs = [0.99, 1.29, 1.49]
product_amount = [10, 5, 20]

# create while loop for input
while True:
    options = input("(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: ")
# option of search; use if statements 
    if options == "s":
        name = input("Enter a product name: ")
        if name in product_names:
            location = product_names.index(name)
            print ("We sell ", name, " at ", product_costs[location], "per unit")
            print ("We currently have ", product_amount[location], " in stock")
            print ()
        else:
            print ("Sorry, we don't sell ", name)
            print ()
    elif options == "l":
# option l; use for loop
        print (format("Product",'<20s') , format("Price",'<20s'), "Quantity")
        for i in product_names:
               location = product_names.index(i)
               print (format(str(i), '<20s') , format(str(product_costs[location]),'<20s'), product_amount[location], end = "\n")
        print () 
    elif options == "q":
# option q; break while loop
        print ("See you soon!")
        break
# option a; use three while loops
    elif options == "a":
        while True:
            new = input("Enter a new product name: ")
            if new in product_names:
                print("Sorry, we already sell that product. Try again.")
            else:
                while True:
                    cost = float(input("Enter a product cost: "))
                    if cost <= 0:
                        print("Invalid cost. Try again.")
                    else:
                        break
                while True:
                    amount = int(input("How many of these products do we have? "))
                    if amount <= 0:
                        print("Invalid quantitiy. Try again.")
                    else:
                        break
                print ("Product added!")
                product_names.append(new)
                product_costs.append(cost)
                product_amount.append(amount)
                break
# option r; use if statements
    elif options == "r":
        removing = input("Enter a product name: ")
        if (removing) in product_names:
            locate = product_names.index(removing)
            del product_names[locate]
            del product_costs[locate]
            del product_amount[locate]
            print ("Product removed!")
        else:
            print("Product doesn't exist. Can't remove.")
# option u; use if statements and while loop
    elif options == "u":
        name_up = input("Enter a product name: ")
        if name_up in product_names:
            print ("What would you like to update?")
            update = input("(n)ame, (c)ost or (q)uantity: ")
            if update == "n":
                while True:
                    new = input("Enter a new name: ")
                    if new in product_names:
                        print("Duplicate name!")
                    else:
                        print("Product name has been updated")
                        print()
                        location = product_names.index(name_up)
                        product_names[location] = new
                        break
# create update of cost
            elif update == "c":
                while True:
                    cost = float(input("Enter a new cost: "))
                    if cost <= 0:
                        print ("Invalid cost!")
                    else:
                        location = product_names.index(name_up)
                        product_costs[location] = cost
                        print ("Product cost has been updated")
                        print()
                        break
# create update of quanitity
            elif update == "q":
                while True:
                    quanity = int(input("Enter a new quantity:"))
                    if quanity <= 0:
                        print("Invalid quantity!")
                    else:
                        print("Product quantity has been updated")
                        print()
                        location = product_names.index(name_up)
                        product_amount[location] = quanity
                        break
            else:
                print("Invalid option")
                print()
        else:
            print ("Product doesn't exist. Can't update.")
            print ()
# create option e; use list methods and for loop
    elif options == "e":
        biggest = max(product_costs)
        big_locate = product_costs.index(biggest)
        smallest = min(product_costs)
        small_locate = product_costs.index(smallest)
        print("Most expensive product: ", biggest, " (",product_names[big_locate],")", sep = "")
        print ("Least expensive product: ", smallest, " (",product_names[small_locate],")", sep = "")
        total = 0
        for i in product_costs:
            locate = product_costs.index(i)
            add = i * product_amount[locate]
            total += add
            
        print("Total value of all products: ", format(total, '.2f'), sep = "")
        print ()

        
        
                
                    
    else:
        print ("Invalid option, try again")
        print ()
        

    


        
