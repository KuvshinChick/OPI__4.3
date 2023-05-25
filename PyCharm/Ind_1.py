#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
    Составить программу с использованием иерархии классов.
Номер варианта необходимо получить у преподавателя.
В раздел программы, начинающийся после инструкции if __name__ = '__main__':
добавить код, демонстрирующий возможности разработанных классов.
    8. Создать класс Triangle с полями-сторонами.
Определить методы изменения сторон, вычисления углов,
периметра. Создать производный класс RightAngled (прямоугольный),
имеющий поле площади. Определить метод вычисления площади.

"""

import math


class Triangle:
    # конструктор класса, принимающий значения сторон a, b, c
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # метод для изменения значений сторон
    def set_sides(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # метод для вычисления углов
    def get_angles(self):
        alpha = math.degrees(math.acos((self.b ** 2 + self.c ** 2 - self.a ** 2)
                                       / (2 * self.b * self.c)))
        beta = math.degrees(math.acos((self.a ** 2 + self.c ** 2 - self.b ** 2)
                                      / (2 * self.a * self.c)))
        gamma = math.degrees(math.acos((self.a ** 2 + self.b ** 2 - self.c ** 2)
                                       / (2 * self.a * self.b)))
        return alpha, beta, gamma

    # метод для вычисления периметра
    def get_perimeter(self):
        return self.a + self.b + self.c


# производный класс RightAngled, наследуемый от класса Triangle
class RightAngled(Triangle):
    # конструктор класса, принимающий значения сторон a, b, c
    def __init__(self, a, b, c):
        # вызываем конструктор родительского класса, передаем ему значения сторон super().init(a, b, c)
        super().__init__(a, b, c)

        # определяем гипотенузу, выбирая максимальное значение из a, b, c
        if a > c and a > b:
            self.hypotenuse = a
        elif b > c and b > a:
            self.hypotenuse = b
        else:
            self.hypotenuse = c
        self.area = self.calc_area()

    # метод для вычисления площади
    def calc_area(self):
        if self.hypotenuse == self.a:
            return (self.b * self.c) / 2
        elif self.hypotenuse == self.b:
            return (self.a * self.c) / 2
        else:
            return (self.a * self.b) / 2


if __name__ == '__main__':
    triangle = Triangle(3, 4, 5)
    print(f"Углы треугольника: {triangle.get_angles()}")
    print(f"Периметр треугольника: {triangle.get_perimeter()}")

    triangle.set_sides(6, 8, 10)
    print(f"Углы треугольника: {triangle.get_angles()}")
    print(f"Периметр треугольника: {triangle.get_perimeter()}")

    right_angled_triangle = RightAngled(3, 4, 5)
    print(f"Углы прямоугольного треугольника: {right_angled_triangle.get_angles()}")
    print(f"Периметр прямоугольного треугольника: {right_angled_triangle.get_perimeter()}")
    print(f"Площадь прямоугольного треугольника: {right_angled_triangle.area}")
