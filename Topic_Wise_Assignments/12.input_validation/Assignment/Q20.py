while True:
    count = int(input("How many numbers (1-20)? "))
    if 1 <= count <= 20:
        break
    print("Invalid count. Please try again.")

total = 0
for i in range(count):
    value = int(input(f"Enter number {i + 1}: "))
    total += value

average = total / count
print("Average:", average)