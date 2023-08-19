def count_vowels(string):
    summah = 0
    string = string.lower()

    print(f"Number of A vowels: {string.count('a')}")
    print(f"Number of E vowels: {string.count('e')}")
    print(f"Number of I vowels: {string.count('i')}")
    print(f"Number of O vowels: {string.count('o')}")
    print(f"Number of U vowels: {string.count('u')}")

    summah += string.count("a")
    summah += string.count("e")
    summah += string.count("i")
    summah += string.count("o")
    summah += string.count("u")

    return summah

print(count_vowels("Uau, que foda"))