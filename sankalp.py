# Get the student's name and marks as input
student_name = input("Enter the student's name: ")
marks = float(input("Enter the student's marks: "))

# Calculate the grade based on the provided rules
if 100 >= marks >= 75:
    grade = "A"
elif 75 > marks >= 65:
    grade = "B"
elif 65 > marks >= 55:
    grade = "C"
elif 55 > marks >= 35:
    grade = "S"
elif 35 > marks >= 0:
    grade = "F"
else:
    print("Invalid marks entered. Marks should be between 0 and 100.")
    exit()

# Print the grade of the student
print(f"Grade for {student_name}: {grade}")

