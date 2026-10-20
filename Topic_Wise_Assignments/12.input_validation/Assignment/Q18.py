while True:
    month = int(input("Enter month (1-12): "))
    if 1 <= month <= 12:
        break
    print("Invalid month. Please try again.")

while True:
    day = int(input("Enter day (1-31): "))
    if 1 <= day <= 31:
        break
    print("Invalid day. Please try again.")

print("Month:", month)
print("Day:", day)