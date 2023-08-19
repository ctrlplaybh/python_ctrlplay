#exercise1

def P_or_N(slacaraio):
    if slacaraio > 0:
        return "P"
    else:
        return "N"

print(P_or_N(0.01))

#exercise2

def reversenumbers(number):
    return str(number) [::-1]

print(reversenumbers(123456789))
