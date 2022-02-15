from random import randint

plus = []
minus = []
flag = True
while flag:
    try:
        amount = int(input("задайте количество примеров:"))
        flag = False
    except:
        print("введите число!")

print("Примеры на вычитание: \n")
while len(plus) <= amount:
    first = randint(10, 99)
    second = randint (10, 99)
    if first - second > 0:
        prim = str(first) + " - " + str (second) + " = "
        plus.append(prim)

print(*plus, sep = "\n")

print("\nПримеры на сложение: \n")

while len(minus) <= amount:
    first = randint(10, 99)
    second = randint (10, 99)
    if first + second < 100:
        prim = str(first) + " + " + str(second) + " = "
        minus.append(prim)

print(*minus, sep = "\n")
