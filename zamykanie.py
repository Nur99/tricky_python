# -*- coding: utf-8 -*- at

# Все в Python объекты. И даже функции. Это значит, что у функций есть
#     атрибуты
#     методы

# От остальных объектов функции отличаются тем, что их можно вызвать*. 
# Объекты, которые можно вызвать, называют Callable-объектами. У них есть метод __call__().


# Функция как объект
# Как у любого объекта в python, у функции есть:
#     идентификатор,
#     тип.


def one():
    x = [1, 2]
    def pr():
        print(x)
        print(id(x))

    return pr

print(id(one), type(one))

a = one()
b = one()
ax = a.__closure__[0].cell_contents
bx = b.__closure__[0].cell_contents
print(id(ax), id(bx))



# Вложенная функция — функция, которая определена внутри другой функции.
# При работе с вложенными функциями надо учитывать области видимости.


# (built-in) — область системных имен
# global — область модуля
def outer():
    # enclosed — область функции-обёртки 
    def inner():
        # local — область внутри функции
        pass


def factorial(x):
    """Функция вычисляет факториал целого числа"""
    def calc_factorial(y): return y * calc_factorial(y-1) if y!=0 else 1
    if x<0:
        return -1
    return calc_factorial(x)


# Замыкание — вложенная функция, которая запоминает значения окружения где она была вызвана. 

def gen_mul(a):
    def inner(b):
        return a*b
    return inner

double = gen_mul(2)
print(double(3))

# Проблема с late binding
powers = []
for i in (1,2):
    def inner(x):
        return x**i
    powers.append(inner)
    
# Хотим получить список степеней 5-ки
for p in powers:
    print(p(5))
# 25
# 25

# Решение проблемы late binding через обёртку (здесь make_inner)
powers = []
for i in (1,2):
    def make_inner(j):
        def inner(x):
            return x**j
        return inner
    powers.append(make_inner(i))
    
for p in powers:
    print(p(5))
# 5
# 25

# Решение проблемы late binding через стандарное знаечение аргумента функции
powers = []
for i in (1,2):
    def inner(x, i=i):
        return x**i
    powers.append(inner)
    
for p in powers:
    print(p(5))
# 5
# 25
