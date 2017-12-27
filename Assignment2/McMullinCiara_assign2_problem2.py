# Problem #2: Place Value Madness
# Ciara McMullin
# 9/19/16
# Section 002

# get two numbers
value1 = int(input("Enter value 1: "))
value2 = int(input("Enter value 2: "))


# get ones places
one1 = value1 % 10
one2 = value2 % 10
one_total = one1 + one2
# get tens places
ten1 = ((value1 % 100) - one1) // 10
ten2 = ((value2 % 100) - one2) // 10
ten_total = ten1 + ten2
# get hundreds places
hundred1 = ((value1 % 1000) - (value1 % 100)) // 100
hundred2 = ((value2 % 1000) - (value2 % 100)) // 100
hundred_total = hundred1 + hundred2
# get thousands places
thousand1 = (value1 - (value1 % 1000)) // 1000
thousand2 = (value2 - (value2 % 1000)) // 1000
thousand_total = thousand1 + thousand2

# print outcome
print ()
print ("Place Value Totals: ")
print()
print ("\t", one1, "+", one2, "=", str(one_total) + " one(s)")
print ("\t", ten1, "+", ten2, "=", str(ten_total) + " ten(s)")
print ("\t", hundred1, "+", hundred2, "=", str(hundred_total) + " hundred(s)")
print ("\t", thousand1, "+", thousand2, "=", str(thousand_total) + " thousand(s)")


