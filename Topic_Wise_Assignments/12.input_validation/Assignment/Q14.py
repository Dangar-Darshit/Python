marks = int(input("Enter marks between 0 and 100: "))

while marks < 0 or marks > 100:
    print("Invalid marks. Please enter a value between 0 and 100.")
    marks = int(input("Enter marks between 0 and 100: "))

if marks >= 75:
    print("Distinction")
elif marks >= 60:
    print("First Class")
elif marks >= 35:
    print("Pass")
else:
    print("Fail")