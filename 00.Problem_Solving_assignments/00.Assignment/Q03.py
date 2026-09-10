# Take two numbers.
# Print:
# The larger number
# Both are equal if both numbers are the same
# Constraint
# Do not use max().

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

if first_number > second_number:
    print(f"The larger number is: {first_number}")
elif second_number > first_number:
    print(f"The larger number is: {second_number}")
elif first_number == second_number:
    print("Both numbers are equal.")
else:
    print("Invalid input.")