# Ciara McMullin
# Intro to Programming
# Assignment 5

# get inputs from user
budget = int(input("Enter budget for your party: "))
cost_slice = float(input("Cost per slice of pizza: "))
cost_pizza = float(input("Cost per whole pizza pie: "))
number = int(input("How many people will be attending your party? "))
total = 0

# create for loop 

for i in range (1,number + 1):
        i_ = str(i)
        slices = int(input("Enter number of slices for person #" + i_ + ": "))
        while True:
            if slices < 0:
                print ("Not a valid entry, try again!")
                slices = int(input("Enter number of slices for person #" + i_ + ": "))
            else:
                break
        total += slices
# get slices, pies, total cost, left over, and over
            
float_pie = total / 8
pie = total // 8
slices_total = int((float_pie-pie) * 8)
total_cost = ((pie * cost_pizza) + (slices_total * cost_slice))
left_over = budget - total_cost
over = total_cost - budget

# compute results
if total_cost < budget:
    print ("You should purchase ", pie, " pies and ",slices_total, " slices")
    print ("Your total cost will be: ", format(total_cost, ".2f"))
    print ("You will still have ", format (left_over, ".2f"), "left after your order")
elif total_cost == budget:
    print ("You should purchase ", pie, " pies and ",slices_total, " slices")
    print ("Your total cost will be: ", format(total_cost, ".2f"))
    print ("You will have no money left after your order.")
elif total_cost > budget:
    print ("Your order cannot be completed.")
    print ("You would need to purchase ", pie, " pies and ", slices_total, "slices")
    print ("This would put you over budget by ", format(over, ".2f"))
    
