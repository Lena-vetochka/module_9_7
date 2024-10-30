"""
Напишите 2 функции:
Функция, которая складывает 3 числа (sum_three)
Функция декоратор (is_prime), которая распечатывает "Простое",
если результат 1ой функции будет простым числом и "Составное" в противном случае.
"""

def is_prime(func):
    def wrapper(*args):
        n = func(*args)
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                print('Составное')
                return n
            print('Простое')
            return n
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a+b+c


result = sum_three(2, 3, 6)
print(result)

