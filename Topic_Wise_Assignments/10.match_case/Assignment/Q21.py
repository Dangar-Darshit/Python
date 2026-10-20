temp = int(input("Convert to:- \n1 → Celsius to Fahrenheit\n2 → Fahrenheit to Celsius\n Enter choice-> "))
c = int(input("Enter Temperatue: "))
match temp:
    case 1:
        print("C->F",(c*1.8)+32)
    case 2:
        print("F->C",(c-32)/1.8)