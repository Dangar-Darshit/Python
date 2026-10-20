score1 = int(input("Enter score 1 (0-100): "))
while not (0 <= score1 <= 100):
    print("Invalid score. Please try again.")
    score1 = int(input("Enter score 1 (0-100): "))

score2 = int(input("Enter score 2 (0-100): "))
while not (0 <= score2 <= 100):
    print("Invalid score. Please try again.")
    score2 = int(input("Enter score 2 (0-100): "))

score3 = int(input("Enter score 3 (0-100): "))
while not (0 <= score3 <= 100):
    print("Invalid score. Please try again.")
    score3 = int(input("Enter score 3 (0-100): "))

total = score1 + score2 + score3
average = total / 3

print("Total:", total)
print("Average:", average)