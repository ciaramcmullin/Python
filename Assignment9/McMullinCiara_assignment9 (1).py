# Ciara McMullin
# assignment 9
# intro to programming

# part1
filename = input("Enter a class file to grade: ")
answerkey = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
answer_key_split = answerkey.split(",")
try:
    myfile = open(filename, "r")
except:
    print("Something went wrong!")
else:
    alldata = myfile.read()

    myfile.close()

    print("Successfully opened", filename)
# part 2
# accumlators and lists
    students = 0
    unusable = 0
    valid = []
    answer = 0
    total = 0
    grades = []
    names = []
    seen = []
    unique = []
    unordered = []
    curved = []
    
# turn the data into list
    splitdata = alldata.split("\n")

# create for loop to get total number of students
    for line in splitdata:
        students += 1
# create two for loops to see usable and unusable lines       
    for i in splitdata:
        answer = 0
        i = i.split(",")
        for choice in i:
            if choice == "A" or choice == "B" or choice == "C" or choice == "D" or choice == "":
                answer += 1
        if answer == 25:
            valid.append(i)

        else:
           unusable += 1
# get test scores
    for i in valid:
        names.append(i[0])
        del i[0]
        score = 0
        for n in range(25):
            if i[n] == answer_key_split[n]:
                score += 4
            elif i[n] == "":
                score += 0
            elif i[n] != answer_key_split[n] and i[n] != "":
                score -= 1
        total += score
        grades.append(score)
        unordered.append(score)
# get mean
    usable = students - unusable
    mean = (total / (usable))


# get medium value
    grades.sort()
    if (usable % 2 != 0):
        median = grades[(len(grades)) // 2]
    else:
        half = (len(grades)) // 2
        median = (grades[half - 1] + grades[half + 1]) // 2
        
# get mode
    for i in grades:
        saw = 0
        if i in unique:
            location = unique.index(i)
            saw = seen[location] + 1
            seen[location] = saw
        else:
            saw += 1
            unique.append(i)
            seen.append(saw)
    max_of_seen = max(seen)
    locate = seen.index(max_of_seen)
    mode = unique[locate]
# get range
    range_ = max(grades) - min(grades)

# output results
    print ("Grade summary: ")
    print("Total students: ", (usable))
    print ("Unusable lines in the file: ", unusable)
    print ("Highest score: ", max(grades))
    print ("Lowest score: ", min(grades))
    print ("Mean score: ", format(mean, ".2f"))
    print ("Median score: ", median)
    print ("Mode: ", mode)
    print ("Range: ", range_)

# part 4
# get file name
    if filename == "class1.txt":
        name = "class1_grades.txt"
    elif filename == "class2.txt":
        name = "class2_grades.txt"
    elif filename == "class3.txt":
        name = "class3_grades.txt"
    elif filename == "class4.txt":
        name = "class4_grades.txt"
    elif filename == "class5txt":
        name = "class5_grades.txt"
    elif filename == "class6.txt":
        name = "class6_grades.txt"
    elif filename == "class7.txt":
        name = "class7_grades.txt"
    elif filename == "class8.txt":
        name = "class8_grades.txt"

# open new text   
    file_grades = open(name, 'w')
# output grades
    for i in range(usable):
        output = (str(names[i]) + "," + format((unordered[i]),".2f"))
        
        file_grades.write(str(output))
        file_grades.write("\n")
    file_grades.close()

# part 5 extra credit
    curve = input("Would you like to curve the exam? 'y' or 'n': ")
    if curve == "y":
        while True:
            desired = input("Enter a desired mean (i.e. 75.0 to raise the mean score to 75.0): ")
            if float(desired) < float(mean):
                print("Invalid curve, try again.")
            else:
                break
        print ("Done! Check your grade file!")
# open new text   
        file_grades = open(name, 'w')
# curve the grades
        curve = int(desired) - int(mean)
        for i in unordered:
            i += int(curve)
            curved.append(i)
# output grades
        
        for i in range(usable):
            output = (str(names[i]) + "," + str(unordered[i]) + "," + str(curved[i]))
        
            file_grades.write(str(output))
            file_grades.write("\n")
        file_grades.close()



            
        
    
    



          

