age = int(input("Enter your age: "))

while 0 > age or age > 120:
    print("Error!!!")
    age = int(input("Enter valid age: "))
print("Your age is accepted")