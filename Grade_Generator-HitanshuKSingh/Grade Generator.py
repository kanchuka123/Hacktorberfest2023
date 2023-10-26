#Program to generate a Grade according to the Marks.

#Take input from user
marks=int(input("Enter the marks :"))

#Perform the Operations and Print Accordingly
if 100>=marks>=75:
    print("Grade A")
elif 75>marks>=65:
    print("Grade B")
elif 65>marks>=55:
    print("Grade C")
elif 55>marks>=35:
    print("Grade S")
elif 35>marks>=0:
    print("Grade F")
