#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
    В следующих заданиях требуется реализовать абстрактный базовый класс,
определив в нем абстрактные методы и свойства. Эти методы определяются
в производных классах. В базовых классах должны быть объявлены абстрактные
методы ввода/вывода, которые реализуются в производных классах.
Вызывающая программа должна продемонстрировать все варианты вызова переопределенных
абстрактных методов. Написать функцию вывода, получающую параметры базового
класса по ссылке и демонстрирующую виртуальный вызов. Номер варианта необходимо получить у преподавателя.

    8. Создать абстрактный базовый класс Function (функция) с виртуальными методами
вычисления значения функции в заданной точке и вывода результата на экран.
Определить производные классы Ellipse (эллипс), Hyperbola (гипербола) с собственными
функциями вычисления у в зависимости от входного параметра x. Уравнение эллипса
x^2/a^2 + y^2/b^2 = 1; гиперболы: x^2/a^2 - y^2/b^2 = 1.
"""

from abc import ABC, abstractmethod
from math import sqrt


# Определим абстрактный базовый класс Function с методами calculate() и printResult()
class Function(ABC):
    @abstractmethod
    def calculate(self, x: float) -> float:
        pass

    @abstractmethod
    def print_result(self):
        pass


# Определим класс Ellipse, который будет реализовывать вычисление эллипса
class Ellipse(Function):
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b
        self.result = 0.0

    def calculate(self, x: float) -> float:
        # Формула для вычисления эллипса
        self.result = sqrt(self.b * self.b * (1 - (x * x) / (self.a * self.a)))
        return self.result

    def print_result(self):
        # Вывод результата вычисления функции
        print(f"Результат вычисления функции (эллипс): {self.result}")


# Определим класс Hyperbola, который будет реализовывать вычисление гиперболы
class Hyperbola(Function):
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b
        self.result = 0.0

    def calculate(self, x: float) -> float:
        # Вычисляем значение выражения под корнем для гиперболы
        value = (x * x) / (self.a * self.a) - 1
        # Проверяем, не меньше ли выражение под корнем нуля
        if value < 0:
            # Если меньше, то результат вычисления будет нулем
            self.result = 0.0
        else:
            # Иначе вычисляем корень из выражения
            self.result = sqrt(self.b * self.b * value)
        return self.result

    def print_result(self):
        # Вывод результата вычисления функции
        print(f"Результат вычисления функции (гипербола): {self.result}")


# Определим функцию printResult(), которая печатает результат вычисления функции
def print_result(function: Function, x: float):
    result = function.calculate(x)
    function.print_result()


if __name__ == '__main__':
    ellipse = Ellipse(3, 2)
    hyperbola = Hyperbola(3, 2)
    hyperbola_1 = Hyperbola(1, 1)

    print_result(ellipse, 1.5)
    print_result(hyperbola, 2.5)
    print_result(hyperbola_1, 3)
