# Даны катеты прямоугольного треугольника a и b. Найти его гипотенузу c и периметр P:
# Имамутдинов Артур Ринатович,05-804
import math
a, b = input().split()
a, b = float(a), float(b)
c = math.sqrt(pow(a, 2) + pow(b, 2))
print("Гипотенуза: ", c , "  Периметр : ", a+b+c)