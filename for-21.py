# Дано целое число N (> 0). Используя один цикл, найти сумму
# 1 + 1/(1!) + 1/(2!) + 1/(3!) + . . . + 1/(N!)
# (выражение N! — N–факториал — обозначает произведение всех целых
# чисел от 1 до N: N! = 1·2·. . .·N). Полученное число является прибли-
# женным значением константы e = exp(1).
# Имамутдинов Артур Ринатович,05-804
import math

a = int(input())
res = 1
for i in range(1, a + 1):
    res += 1 / math.factorial(i)
print(res)