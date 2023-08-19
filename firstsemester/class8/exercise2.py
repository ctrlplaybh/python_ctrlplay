def calculate_half(list):
    summah = sum(list)
    half = summah / len(list)

    if half >= 6:
        print("Approved!")

    else:
        print("Failed!")

    return round(half, 3)

print(calculate_half([1]))

