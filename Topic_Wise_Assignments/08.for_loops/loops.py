# # Python For Loop Assignment
# # Questions 1 to 20


# # Q1. Print "Hello" five times
# print("Q1")
# for i in range(5):
#     print("Hello")


# # Q2. Print numbers from 0 to 9
# print("\nQ2")
# for i in range(10):
#     print(i, end=" ")


# # Q3. Print numbers from 1 to 10
# print("\n\nQ3")
# for i in range(1, 11):
#     print(i, end=" ")


# # Q4. Print numbers from 10 to 1
# print("\n\nQ4")
# for i in range(10, 0, -1):
#     print(i, end=" ")


# # Q5. Print numbers from 5 to 50 with step 5
# print("\n\nQ5")
# for i in range(5, 51, 5):
#     print(i, end=" ")


# # Q6. Print even numbers from 2 to 20
# print("\n\nQ6")
# for i in range(2, 21, 2):
#     print(i, end=" ")


# # Q7. Print odd numbers from 1 to 19
# print("\n\nQ7")
# for i in range(1, 20, 2):
#     print(i, end=" ")


# # Q8. Print 3, 6, 9, 12, 15, 18
# print("\n\nQ8")
# for i in range(3, 19, 3):
#     print(i, end=" ")


# # Q9. Print numbers from 20 down to 2
# print("\n\nQ9")
# for i in range(20, 1, -2):
#     print(i, end=" ")


# # Q10. Print numbers from 1 to n
# print("\n\nQ10")
# n = int(input("Enter n: "))

# for i in range(1, n + 1):
#     print(i, end=" ")


# # Q11. Print even numbers from 1 to n
# print("\n\nQ11")
# n = int(input("Enter n: "))

# for i in range(1, n + 1):
#     if i % 2 == 0:
#         print(i, end=" ")


# # Q12. Print odd numbers from 1 to n
# print("\n\nQ12")
# n = int(input("Enter n: "))

# for i in range(1, n + 1):
#     if i % 2 != 0:
#         print(i, end=" ")


# # Q13. Print numbers divisible by 3
# print("\n\nQ13")
# n = int(input("Enter n: "))

# for i in range(1, n + 1):
#     if i % 3 == 0:
#         print(i, end=" ")


# # Q14. Print numbers divisible by both 2 and 3
# print("\n\nQ14")
# n = int(input("Enter n: "))

# for i in range(1, n + 1):
#     if i % 2 == 0 and i % 3 == 0:
#         print(i, end=" ")


# # Q15. Count even numbers from 1 to n
# print("\n\nQ15")
# n = int(input("Enter n: "))
# count = 0

# for i in range(1, n + 1):
#     if i % 2 == 0:
#         count = count + 1

# print("Number of even numbers:", count)


# # Q16. Calculate 1 + 2 + 3 + ... + n
# print("\nQ16")
# n = int(input("Enter n: "))
# total = 0

# for i in range(1, n + 1):
#     total = total + i

# print("Sum:", total)


# # Q17. Calculate sum of even numbers from 1 to n
# print("\nQ17")
# n = int(input("Enter n: "))
# total = 0

# for i in range(1, n + 1):
#     if i % 2 == 0:
#         total = total + i

# print("Sum of even numbers:", total)


# # Q18. Calculate sum of odd numbers from 1 to n
# print("\nQ18")
# n = int(input("Enter n: "))
# total = 0

# for i in range(1, n + 1):
#     if i % 2 != 0:
#         total = total + i

# print("Sum of odd numbers:", total)


# # Q19. Print multiplication table from 1 to 10
# print("\nQ19")
# n = int(input("Enter a number: "))

# for i in range(1, 11):
#     print(n, "x", i, "=", n * i)


# # Q20. Calculate 1 × 2 × 3 × ... × n
# print("\nQ20")
# n = int(input("Enter n: "))
# result = 1

# for i in range(1, n + 1):
#     result = result * i

# print("Product:", result)

# #Q21
# print("\nQ21")
# string = input("Enter a word: ")

# for i in string:
#     print(i)

# #Q22
# print("\nQ22")
# string = input("Enter a word: ")

# for i in string:
#     print(i, end=" ")

# #Q23
# print("\nQ23")
# string = input("Enter a word: ")
# count=0
# for i in string:
#     count = count + 1
# print(count)


# #Q24
# print("\nQ24")
# string = input("Enter a word: ")
# count=0

# for i in string:
#     if i == "a":
#         count = count + 1
# print(count)

#Q25
# print("\nQ25")
# string = input("Enter a word: ")
# count=0

# for i in string:
#     if "A" <= i <= "Z":
#         count = count + 1
# print(count)


#Q26
# print("\nQ26")
# for i in range(3):
#     for i in range(3):
#         print("*", end=" ")
#     print()

#Q27
# print("\nQ27")
# for i in range(4):
#     for i in range(5):
#         print("*", end=" ")
#     print()

#Q28
# print("\nQ28")
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*", end=" ")
#     print()


#Q29
# print("\nQ29")
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print()

# Q30
print("\nQ30")
for j in range(1,11):
    for i in range(1,11):
        print(f"{i}x{j}={i*j}|", end=" ")
    print()


#Practice
# print("\nPractice")
# n = int(input("Enter any number:"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print()