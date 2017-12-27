# Problem #3: Birthday Analyzer
# Ciara McMullin
# Section 2
# 10/3/16

print ("Instructions: Enter the start date and birthdate for an employee to determine their age at the start of employment.")

# promt user to enter start date and birthday
start_date = int( input ("Enter start date MMDDYYYY: "))

birthday = int( input( "Enter birth date MMDDYYYY: "))

# get birthday days, months, and years
year = birthday % 10000

month = (birthday % 100000000) // 1000000

day = (birthday % 1000000) // 10000

# get show days, months, and years
start_year = start_date % 10000

start_month = (start_date % 100000000) // 1000000

start_day = (start_date % 1000000) // 10000

# convert birthday months
if birthday > 1000000 and  birthday < 2000000:
    birthday_month = "January"
elif birthday > 2000000 and birthday < 3000000:
    birthday_month = "February"
elif birthday > 3000000 and birthday < 4000000:
    birthday_month = "March"
elif birthday > 4000000 and birthday < 5000000:
    birthday_month = "April"
elif birthday > 5000000 and  birthday < 6000000:
    birthday_month = "May"
elif birthday > 6000000 and birthday < 7000000:
    birthday_month = "June"
elif birthday > 7000000 and birthday < 8000000:
    birthday_month = "July"
elif birthday > 8000000 and birthday < 9000000:
    birthday_month = "August"
elif birthday > 9000000 and birthday < 10000000:
    birthday_month = "September"
elif birthday > 10000000 and birthday < 11000000:
    birthday_month = "October"
elif birthday > 11000000 and birthday < 12000000:
    birthday_month = "November"
elif birthday > 12000000 and birthday < 13000000:
    birthday_month = "December"

# labels for day
if day == 1 or day == 21 or day == 31 :
    sufx = ("st")
if day == 2 or day == 22 :
    sufx = ("nd")
if day == 3 or day == 23 :
    sufx = ("rd")
if day > 3 and day <= 20 :
    sufx = ("th")
if day > 23 and day <= 31 :
    sufx = ("th")

# show candidates birthday
print ("The contestant was born on ", birthday_month, " ", day, sufx, ", ", year, sep = "") 

# check to see if candidate is eligible
if start_year - year > 21 :
    print ("ELIGIBLE: The contestant will be 21 by the time taping begins")
elif start_year - year == 21 and start_month > month:
    print ("ELIGIBLE: The contestant will be 21 by the time taping begins")
elif start_year - year == 21 and start_month == month and day == start_day:
    print ("ELIGIBLE: The contestant will be 21 by the time taping begins")
elif start_year - year == 21 and start_month == month and day < start_day:
    print ("ELIGIBLE: The contestant will be 21 by the time taping begins")
else :
    print ("NOT ELIGIBLE: The contestant won't be 21 by the time taping begins")


