# Problem #1: Valid Triangle Tester
# Ciara McMullin
# 9/26/16
# Section 2
print ("Valid Triangle Tester")
print ()

# prompt the user to enter in 3 points (floats)
x1 = float(input("Enter Point #1 - x position: "))
y1 = float(input("Enter Point #1 - y position: "))
x2 = float(input("Enter Point #2 - x position: "))
y2 = float(input("Enter Point #2 - y position: "))
x3 = float(input("Enter Point #3 - x position: "))
y3 = float(input("Enter Point #3 - y position: "))
print ()

# use the distance formula to compute distance between each point
side1 = ((x1-x2)**(2)+(y1-y2)**(2))**(.5)
side2 = ((x1-x3)**(2)+(y1-y3)**(2))**(.5)
side3 = ((x3-x2)**(2)+(y3-y2)**(2))**(.5)
print ("The length of each sie of your test shape is: ")
print ()

# print distance to two decimal places
side1_ = float(format(side1, ".2f"))
side2_ = float(format(side2, ".2f"))
side3_ = float(format(side3, ".2f"))
print ("Side 1: ", side1_)
print ("Side 2: ", side2_)
print ("Side 3: ", side3_)
print ()

# determine if valid triangle;if valid determine what type of triangle
if side1_ + side2_ > side3_ and side2_ + side3_ > side1_ and side3_ + side1_ > side2_:
    print ("This is a valid triangle!")
    if side1_ == side2_ == side3_ :
        print ("This is an equilateral triangle")
    elif side1_ == side2_ or side1_ == side3_ or side2_ == side3_ :
        print ("This is an isoceles triangle")
    elif side1_ != side2_ != side3_ :
        print ("This is a scalene triangle")
else:
    print ("This is not a valid triangle!")









    
    
    
    
    


