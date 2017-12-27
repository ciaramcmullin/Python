# Problem #3: Grade Calculator
# Ciara McMullin
# 9/19/16
# Section 002

# ask user for name and class
user_name = input("What is your name? ")
name_of_class = input("What class are you in? ")
print()

# get test weight, test scores, and then average
test_weight = input("How much are tests worth in this class: ")
test1 = int(input("Enter test score #1: "))
test2 = int(input("Enter test score #2: "))
test3 = int(input("Enter test score #3: "))
print ()
test_average = (test1 + test2 + test3) / 3
# get test average to two decimal places
new_test_average = format (test_average, ".2f")
print ("Your test average is: ", new_test_average, )
print ()
# get homework weight, homework scores, and then average
homework = input("How much are homework assignments worth in this class: ")
homework1 = int(input("Enter homework score #1: "))
homework2 = int(input("Enter homework score #2: "))
homework3 = int(input("Enter homework score #3: "))
homework_average = (homework1 + homework2 + homework3) / 3
# get homework average to two decimal places
new_homework_average = format (homework_average, ".2f")
# outcome the results and calculate final grade
print ()
print ("Your homework average is: ", new_homework_average)
print ()
test_percent = (float(new_test_average) * .40)
homework_percent = (float(new_homework_average) * .60)
final_score = test_percent + homework_percent
new_final_score = format (final_score, ".2f")
print ("Thanks,", user_name + ". Your final score in ", name_of_class, "is", new_final_score)
