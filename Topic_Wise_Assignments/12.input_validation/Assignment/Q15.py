username = input("Enter username: ").strip()
password = input("Enter password: ")

while len(username) < 5 or " " in username or len(password) < 8 or password.strip() == "":
    print("Invalid username or password. Please try again.")
    username = input("Enter username: ").strip()
    password = input("Enter password: ")

print("Success!")