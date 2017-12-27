# Problem #1: Dynamic Tip Calculator
# Ciara McMullin
# Section 002
# 9/19/16

# print introduction
print ("Hello! I'm here to help you calculate your tip.")

# get bill amount in float, tip in integer, and number spliting bill
bill_amount = float(input("How much was your bill? : " ))
tip_amount = int(input("How much tip would you like to leave? : " ))
individuals_splitting_bill = int(input("How many individuals are splitting the bill? : "))

# get tip amount, add tip to total bill, and split among 4 people
tip = (tip_amount / 100) * bill_amount
total_bill = tip + bill_amount
indiviual = total_bill / 4
# get tip, bill, and indivual to 2 decimal places
new_tip = format (tip, ".2f")
new_bill = format(total_bill, ".2f")
new_indiviual = format(indiviual, ".2f")

# output results
print ()
print ("Thanks! Calculating your bill & tip ...")
print ()
print ("You need to leave $" + new_tip, "as a tip.")
print ("Your total bill will be $" + new_bill + ".")
print ("Each individual should pay $" + new_indiviual + ".")
