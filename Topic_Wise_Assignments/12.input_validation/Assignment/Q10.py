pin = 2468

p = int(input("Enter your pin: "))

for i in range(3):
    if p == pin:
        print("Correct pin")
        break
    else:
        p = int(input("Enter your pin again: "))
else:
    print("wait for 5 minutes and then try again")