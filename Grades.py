marks = int(input("Enter your marks:"))

if(marks >= 90):
    garde = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"
elif(marks >= 60 and marks < 70):
    grade = "D"

print("Your grade is: ", grade)
