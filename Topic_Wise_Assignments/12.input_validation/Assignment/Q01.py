marks = int(input("Enter your marks between 0-100: "))

while marks<0 or marks>100:
    marks=int(input("Enter valid marks: "))

print("Accepted Marks:", marks)