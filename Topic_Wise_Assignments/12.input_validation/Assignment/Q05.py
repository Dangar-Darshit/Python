password = input("Enter a strong password: ")

while len(password)<8:
    password = input("Enter atleast 8 character password: ")
for i in password:
    if i == " ":
        password = input("Enter password without using spaces anywhere: ")

print("Success")