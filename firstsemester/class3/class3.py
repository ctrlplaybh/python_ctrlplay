#Lists
#How to create a list in Python?

birthday_guests_list = ["Silas", "Gabriel", "Lucas", "Pedro", "Rodrigo"]

print(birthday_guests_list)

print("My birthday in 2022 had", str(len(birthday_guests_list)), "guests.")

#Adding items to the list

birthday_guests_list.append("Cida")

print(birthday_guests_list)

birthday_guests_list.append("Eliete")

print(birthday_guests_list)

#Adding items to the list in a specific position

birthday_guests_list.insert(0, "THE SACRED MIDDLE FINGER OF FUCK")

print(birthday_guests_list)

#Removing an item from the list

birthday_guests_list.pop(0)

print(birthday_guests_list)

#Organizing the lists
#sort()

print(birthday_guests_list)

birthday_guests_list.sort()

print(birthday_guests_list)

birthday_guests_list.sort(reverse=True)

print(birthday_guests_list)

#Exercise 1

places_list = ["United States", "UK (England)", "Portugal", "Super Mario Land (Hollywood)", "Disneyland", "Spain"]

print(places_list)

print(sorted(places_list))

print(places_list[::-1])