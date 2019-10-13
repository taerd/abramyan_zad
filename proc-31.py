# Описать функцию IsPalindrom(K), возвращающую TRUE, если целый
# параметр K (> 0) является палиндромом (то есть его запись читается оди-
# наково слева направо и справа налево), и FALSE в противном случае. С
# ее помощью найти количество палиндромов в наборе из 10 целых поло-
# жительных чисел. При описании функции можно использовать функции
# DigitCount и DigitN из заданий Proc29 и Proc30.
# Имамутдинов Артур Ринатович,05-804
def DigitCount(a):
    kol = 0
    while a != 0:
        a = int(a / 10)
        kol += 1
    return kol


def DigitN(a, n):
    kol = DigitCount(a)
    if (n <= kol and n >= 0):
        i = 0
        while i != n - 1:
            a = int(a / 10)
            i += 1
        return a % 10
    else:
        return -1


def IsPalindrom(a):
    kol = DigitCount(a)
    if (kol % 2 == 0):
        for i in range(1, int(kol / 2) + 1):
            if DigitN(a, i) != DigitN(a, kol - i + 1):
                return print("False")
        return print("True")
    else:
        for i in range(1, int((kol + 1) / 2)):
            if DigitN(a, i) != DigitN(a, kol - i + 1):
                return print("False")
        return print("true")


a = int(input())
IsPalindrom(a)
