#Q1-Python Program that asks the user for their name and prints the name
name = input("Enter your name: ")
print(f"User's name is: {name}")

#Q2-Python Program that asks the user for their city and prints the city
city = input("Enter your city name: ")
print(f"Your city name is: {city}")

#Q3-Take a user's name and age using two separate input() statements and print both values.
name , age = input("Enter your name and age: ").split()
print(f"Your name is {name} and your age is {age}") 

#Q4-What type of value does input() return by default?
# The input() function in Python returns a value of type string by default.

#Q5-Write a program that takes a value using input() and displays its type using type().
value = input("Enter a value: ")
print(f"The Datatype of the entered value is: {type(value)}")

#Q6-Take first name and last name separately and display them together.
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(f"Your full name is: {first_name} {last_name}")

#Q7-Take three pieces of information:
# name
# city
# college
# Store each in a separate variable and display them.
name = input("Enter your name: ")
city = input("Enter your city: ")
college = input("Enter your college name: ")
print(f"Your name is: {name}")
print(f"Your city is: {city}")
print(f"Your college name is: {college}")

#Q8-Write a program that takes two names on the same line and stores them in two variables using .split().
names = input("Enter two names of your choice: ").split()
print(f"First name is: {names[0]}")
print(f"Second name is: {names[1]}")

#Q9-Suppose the user enters:
# Python Programming
# using one input() statement with .split().
# What values will the two variables receive?
# The two variables will receive "Python" and "Programming" respectively.

#Q10-Write a program that takes three words from one line and displays them separately.
words = input("Enter three words: ").split()
print(f"First word: {words[0]}")
print(f"Second word: {words[1]}")
print(f"Third word: {words[2]}")

#Q11-Convert the string: "25" into an integer.
string_value = "25"
integer_value = int(string_value)

#Q12-Convert the string: "25.5" into a floating-point number.
string_value = "25.5"
float_value = float(string_value)

#Q13-Convert the integer: 100 into a string.
integer_value = 100
string_value = str(integer_value)

#Q14-Take an integer from the user and print its type after conversion.
user_input = input("Enter any number: ")
converted_value = int(user_input)
print(f"The Datatype of the entered value after conversion is: {type(converted_value)}")

#Q15-Take a floating-point number from the user and print its type after conversion.
user_input = input("Enter any floating-point number: ")
converted_value = float(user_input)
print(f"The Datatype of the entered value after conversion is: {type(converted_value)}")

#Q16-Why does this produce string concatenation instead of numeric addition?
# a = input()
# b = input()
# print(a + b)
# Because the input() function returns values as strings by default. When you use the + operator on strings, it performs string concatenation instead of numeric addition. To perform numeric addition, you need to convert the input values to integers or floats before adding them.

#Q17-Correct the following program so that it performs numeric addition:
# a = input("Enter first number: ")
# b = input("Enter second number: ")
# print(a + b)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a + b)

#Q18-Create variables:
# name = "Rahul"
# age = 20
# Use an f-string to display:
# My name is Rahul and I am 20 years old.
name = "Rahul"
age = 20
print(f"My name is {name} and I am {age} years old.")

#Q19-Create: a = 10 b = 20 Use an f-string to display their sum.
A = 10
B = 20
print(f"The sum of {A} and {B} is: {A + B}")

#Q20-Take a user's name and age and display them in one sentence using an f-string.
user_name = input("Enter your name: ")
user_age = input("Enter your age: ")
print(f"My name is {user_name} and I am {user_age} years old.")

#Q21-Take the price of a product as a floating-point value and display it using exactly two decimal places.
price = float(input("Enter the price of the product: "))
print(f"The price of the product is: {price:.2f}")

#Q22-What is the purpose of: :.2f inside an f-string?
# The purpose of :.2f inside an f-string is to format a floating-point number to display exactly two decimal places. The .2 specifies that two digits should be shown after the decimal point, and the f indicates that the value is a floating-point number. This is useful for displaying prices, measurements, or any other numerical values where a specific number of decimal places is required.

#Q23-Write a program that takes:
# product name
# price
# quantity
# and displays all three values using f-strings.
product_name = input("Enter the product name: ")
price = float(input("Enter the price of the product: "))
quantity = int(input("Enter the quantity of the product: "))
print(f"I have purchased {quantity} units of {product_name} at a price of {price:.2f} each.")

#Q24-What will this display? print("A", "B", "C")
# This will display: A B C

#Q25-Rewrite the following so that the values are separated by -: print("2026", "08", "19")
print("2026", "08", "19", sep="-")

#26-Write two print() statements that produce: Hello World  on the same line using end.
print("Hello", end=" ")
print("World")

#27-Write a program that takes two integers from the user and displays:
# First number: <first>
# Second number: <second>
# Sum: <sum>
# Use f-strings for the output.
first_number = int(input("Enter the first integer: "))
second_number = int(input("Enter the second integer: "))
sum_of_numbers = first_number + second_number
print(f"First number: {first_number}")
print(f"Second number: {second_number}")
print(f"Sum: {sum_of_numbers}")

#Q28-Write a program that takes the price and quantity of a product and calculates the total cost.
# Display:
# Price: ...
# Quantity: ...
# Total: ...
# Use appropriate type conversion and an f-string.
price = float(input("Enter the price of the product: "))
quantity = int(input("Enter the quantity of the product: "))
total_cost = price * quantity
print(f"Price: {price:.2f}")
print(f"Quantity: {quantity}")
print(f"Total: {total_cost:.2f}")

#Q29-Write a program that takes a student's:
# name
# age
# marks
# where age is an integer and marks is a floating-point value.
#Display all information using a clear formatted message.
student_name = input("Enter the student's name: ")
student_age = int(input("Enter the student's age: "))
student_marks = float(input("Enter the student's marks: "))
print(f"Student's Name: {student_name}")
print(f"Student's Age: {student_age}")
print(f"Student's Marks: {student_marks:.2f}")

#Q30-Create a small "Student Information" program that:
# 1.Takes the student's name.
# 2. Takes the student's age as an integer.
# 3. Takes the student's height as a floating-point number.
# 4. Takes the name of the city.
# 5. Displays all information using f-strings.
# 6. Displays the height with exactly two decimal places.
student_name = input("Enter the student's name: ")
student_age = int(input("Enter the student's age: "))
student_height = float(input("Enter the student's height: "))
city_name = input("Enter the name of the city: ")
print(f"Student's Name: {student_name}")
print(f"Student's Age: {student_age}")
print(f"Student's Height: {student_height:.2f}")
print(f"City: {city_name}")