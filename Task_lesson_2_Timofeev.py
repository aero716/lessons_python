# Семинар №2
# =================== Задача №10 ===================
n = [1, 0, 1, 0, 0]

def coin(n):
    count_top = 0
    count_bottom = 0
    for el in n:
        if (el == 0):
            count_top += 1
        elif (el == 1):
            count_bottom += 1
        else:
            print("error")
    return min(count_top, count_bottom)

print(f"Нужно перевернуть {coin(n)} монеты")


# =================== Задача №12 ===================
sum = 60
product = 500

def found_numbers(s, p):
    for i in range(1001):
        for j in range(1001):
            if (i * j == p and i + j == s):
                return i, j
    return "не найдено", "не найдено"

print(f"Числа: {found_numbers(sum, product)[0]}, {found_numbers(sum, product)[1]}")


# =================== Задача №14 ===================
N = 100
s = 0.
while 1:
    n = 2**s
    if(n <= N): 
        print(f"2^{s}: {n}")
        s += 1
    else:
        break