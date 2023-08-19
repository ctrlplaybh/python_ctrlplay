grades_1 = float(input())

grades_2 = float(input())

grades_3 = float(input())

half = (grades_1 + grades_2 + grades_3) / 3

print(round(half, 2))

if half > 10:
    print("F-, this half is not valid.")

elif half == 10:
    print("S")
elif half == 9.9 or half == 9.8 or half == 9.7 or half == 9.6 or half == 9.5:
    print("A++")

elif half == 9.4 or half == 9.3 or half == 9.2 or half == 9.1 or half == 9:
    print("A")

elif half == 8.9 or half == 8.8 or half ==  8.7 or half == 8.6 or half == 8.5:
    print("B+")

elif half == 8.4 or half == 8.3 or half == 8.2 or half == 8.1 or half == 8:
    print("B")

elif half == 7.9 or half == 7.8 or half == 7.7 or half == 7.6 or half == 7.5:
    print("B-")

elif half == 7.4 or half == 7.3 or half == 7.2 or half == 7.1 or half == 7 or half ==  6.9 or half == 6.8 or half == 6.7 or half == 6.6 or half == 6.5 or half == 6.4 or half == 6.3 or half == 6.2 or half == 6.1:
    print("C+")

elif half == 6 or half == 5.9 or half == 5.8 or half == 5.7 or half == 5.6 or half == 5.5 or half == 5.4 or half == 5.3 or half == 5.2 or half == 5.1 or half == 5 or half == 4.9 or half == 4.8 or half == 4.7 or half == 4.6:
    print("C")

elif half == 4.5 or half == 4.4 or half == 4.3 or half == 4.2 or half == 4.1:
    print("C-")

elif half == 4  or half == 3.9 or half == 3.8 or half == 3.7 or half == 3.6:
    print("D+")

elif half == 3.5 or half == 3.4 or half == 3.3 or half == 3.2 or half == 3.1:
    print("D")

elif half == 3 or half == 2.9 or half == 2.8 or half == 2.7 or half == 2.6 or half == 2.5:
    print("E")

elif half <= 2.4:
    print("F")