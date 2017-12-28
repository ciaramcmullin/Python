# Ciara McMullin
# Intro to Computer Programming
# Assignment 5

# create while loops for students and tests
while True:
    students = int(input("How many students are in your class? "))
    if students < 0:
        print ("Invalid # of students, try again.")
    else:
        break
while True:
    tests = int(input("How many tests in this class? "))
    if tests < 0:
        print ("Invalid # of tests, try again.")
    else:
        print ()
        print ("Here we go!")
        break

# create for loop for students and tests
# calculate average for each student
overall = 0
for i in range (1, students + 1):
    total = 0
    print ("**** Student #",i,"****")
    for t in range (1, tests + 1):
        t = str(t)
        score = int(input("Enter score for test #" + t + ": "))
        while True:
            if score < 0:
                print ("Invalid score, try again")
                score = int(input("Enter score for test #" + t + ": "))
            else:
                total += score
                break
   
    avg = total / tests
    overall += avg
    print ("Average score for student #", i, " is ", format(avg, ".2f"))
# get average for all the students
all_students = overall / students
print ()
print ("Average score for all students is: ", format(all_students, ".2f"))
