fail = 0
Pass = 0
good = 0
excellent = 0

for i in range(10):
    marks = int(input("Enter marks: "))
    if marks < 35:
        print("Fail")
        fail = fail + 1
    elif marks < 50:
        print("Pass")
        Pass = Pass + 1
    elif marks < 75:
        print("Good")
        good = good + 1
    else:
        print("Excellent")
        excellent = excellent + 1

print("Fail:", fail)
print("Pass:", Pass)
print("Good:", good)
print("Excellent:", excellent)