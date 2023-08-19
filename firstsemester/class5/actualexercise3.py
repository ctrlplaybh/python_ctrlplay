user = str(input("Insert your user here: "))
password = str(input("Insert your password here: "))

while user == password:
    print("Incorrect data, the name cannot be the same as the password, insert again, please.")
    user = str(input("Insert your user here again, differrent than the password: "))
    password = str(input("insert your password here again, different than the user: "))