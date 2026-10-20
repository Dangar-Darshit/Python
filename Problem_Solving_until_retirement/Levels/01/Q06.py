marks = int(input("Enter your marks: "))
if 0 <= marks <= 100:
    if marks >= 90:
        print("A")
    elif marks >= 80:
        print("B")
    elif marks >= 70:
        print("C")
    elif marks >= 60:
        print("D")
    elif marks >= 35:
        print("E")
    elif marks >= 0:
        print("F")
else:
    print("Enter valid marks")