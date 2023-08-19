age = int(input("Insert your age here: "))
info = input("Are you a teacher or a student? Y = Any of both; N = None: ")

if age <= 4 or age >= 60:
    tickets = "free, that means it's for 0"

elif 4 < age < 18:
    tickets = 20.0

elif 18 <= age < 60:
    tickets = 30.0

if info.upper() == "Y":
    print(f"The price of your ticket is {tickets / 2} dollars.")

else:
    print(f"The price of your ticket is {tickets} dollars.")