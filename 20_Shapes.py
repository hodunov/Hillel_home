"""
Реализовать класс фигуры. На основе фигуры реализовать класс треугольника, квадрата и прямоугольника с методами
подсчета площади и периметра. Методы должны возвращать значение, а не принтить

"""
from math import sqrt


class Shape(object):
    """
    Generic Shape object
    """
    def area(self):
        """
        Shape area
        """
        pass

    def perimeter(self):
        """
        Shape perimeter
        """
        pass


class Square(Shape):
    """
    Basic square class
    """
    def __init__(self, side_length):
        self.side = side_length

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return self.side * 4


class Rectangle(Shape):
    """
    Basic rectangle class
    """
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


class Triangle(Shape):
    """
    Basic triangle class
    """
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area(self):
        semi_perimeter = (self.side_a + self.side_b + self.side_c) * 0.5
        return sqrt(semi_perimeter * (semi_perimeter - self.side_a) *
                    (semi_perimeter - self.side_b) * (semi_perimeter - self.side_c))

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c


def main():
    """
    Displays inheritance methods
    """
    rect = Rectangle(8, 7)
    print("Rectangle(8, 7)")
    print("  Area: " + str(rect.area()))
    print("  Perimeter: " + str(rect.perimeter()))

    square = Square(10)
    print("Square(10)")
    print("  Area: " + str(square.area()))
    print("  Perimeter: " + str(square.perimeter()))

    triangle = Triangle(3, 4, 5)
    print("Triangle(3, 4, 5)")
    print("  Area: " + str(triangle.area()))
    print("  Perimeter: " + str(triangle.perimeter()))


if __name__ == '__main__':
    main()
