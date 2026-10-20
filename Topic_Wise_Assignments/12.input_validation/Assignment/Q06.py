temp = int(input("Enter a temperature: "))

while temp < -20 or temp > 45:
    temp = int(input("Enter a valid temperature: "))

print("Success")