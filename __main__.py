# ИМЯ ФАЙЛА ДОЛЖНО БЫТЬ __main__.py

from abc import ABC, abstractmethod
import math


# Абстрактный класс "Геометрическая фигура"
class GeometricFigure(ABC):
    @abstractmethod
    def area(self):
        pass


# Класс "Цвет фигуры"
class FigureColor:
    def __init__(self, color: str):
        self.color = color

    def __str__(self):
        return self.color


# Класс "Прямоугольник"
class Rectangle(GeometricFigure):
    figure_name = "Прямоугольник"

    def __init__(self, width: float, height: float, color: str):
        self.width = width
        self.height = height
        self.color = FigureColor(color)

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return "{} (цвет: {}, ширина: {}, высота: {}, площадь: {:.2f})".format(
            self.figure_name, self.color, self.width, self.height, self.area())

    @classmethod
    def get_figure_name(cls):
        return cls.figure_name


# Класс "Круг"
class Circle(GeometricFigure):
    figure_name = "Круг"

    def __init__(self, radius: float, color: str):
        self.radius = radius
        self.color = FigureColor(color)

    def area(self):
        return math.pi * self.radius ** 2

    def __repr__(self):
        return "{} (цвет: {}, радиус: {}, площадь: {:.2f})".format(
            self.figure_name, self.color, self.radius, self.area())

    @classmethod
    def get_figure_name(cls):
        return cls.figure_name


# Класс "Квадрат"
class Square(Rectangle):
    figure_name = "Квадрат"

    def __init__(self, side: float, color: str):
        super().__init__(side, side, color)

    @classmethod
    def get_figure_name(cls):
        return cls.figure_name


if __name__ == "__main__":
    import numpy as np  # Установка внешнего пакета (numpy)

    N = 23

    rectangle = Rectangle(N, N, "синий")
    circle = Circle(N, "зеленый")
    square = Square(N, "красный")

    print(rectangle)
    print(circle)
    print(square)

    print("Случайное число из numpy:", np.random.randint(1, 100))
