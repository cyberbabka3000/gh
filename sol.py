import math

print("Введите коэффициенты")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

D = b ** 2 - (4 * a * c)
print("D = ", D)

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print("Первый корень = ", (x1))
    print("Второй корень = ",(x2))
elif D == 0:
    x1 = -b / (2 * a)
    print("Первый корень = ", (x1))
elif D < 0:
    print("Корней нет")
else:
    print("Такого уравнения не может сущесвовать")