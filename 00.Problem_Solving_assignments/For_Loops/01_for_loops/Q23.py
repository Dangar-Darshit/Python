junior = 0
mid = 0
senior = 0
executive = 0
total = 0

for i in range(8):
    salary = int(input("Enter salary: "))
    total = total + salary

    if salary < 25000:
        print("Junior")
        junior = junior + 1
    elif salary <= 50000:
        print("Mid")
        mid = mid + 1
    elif salary <= 100000:
        print("Senior")
        senior = senior + 1
    else:
        print("Executive")
        executive = executive + 1

print("Average:", total / 8)
print(junior, mid, senior, executive)