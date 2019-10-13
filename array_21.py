# Дан массив размера N и целые числа K и L (1 ≤ K ≤ L ≤ N).
# Найти среднее арифметическое элементов массива с номерами от K до L
# включительно.
# Имамутдинов Артур Ринатович,05-804
print("Вводите элементы массива : ")
lst = input().split()
n = len(lst)
lst = list(map(int, lst))
print("Введите k и l : ")
k, l = map(int, input().split())
if (k > 0) & (l > 0) & (k <= n) & (l <= n) & (k <= l):
    c = 0
    for i in range(k, l + 1):
        c += lst[i]
    c = float(c / (l - k + 1))
    print(c)
else:
    print("Не удалось")