import math
from enum import Enum


class Colour(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 4
    BLACK = 5
    WHITE = 6


class Point:

    def __init__(self, x, y):
        self.set_x(x)
        self.set_y(y)

    def __del__(self):
        pass

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, value):
        self.__x = float(value)

    def set_y(self, value):
        self.__y = float(value)

    def distance_to(self, other_point):
        dx = self.__x - other_point.get_x()
        dy = self.__y - other_point.get_y()
        return math.sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return f"({self.__x}, {self.__y})"

    def __repr__(self):
        return f"Point({self.__x}, {self.__y})"


class Polynom:

    def __init__(self, colour, *points):
        self.set_colour(colour)
        self.__points = list(points)

    def __del__(self):
        pass

    def get_colour(self):
        return self.__colour

    def get_points(self):
        return self.__points

    def set_colour(self, value):
        if not isinstance(value, Colour):
            raise TypeError("Колір має бути екземпляром Colour")
        self.__colour = value

    def calculate_perimeter(self):
        perimeter = 0.0
        n = len(self.__points)

        if n >= 2:
            for i in range(n):
                p1 = self.__points[i]
                if i == n - 1:
                    p2 = self.__points[0]
                else:
                    p2 = self.__points[i + 1]

                perimeter += p1.distance_to(p2)

        return perimeter

    def get_longest_diagonal(self):
        if len(self.__points) < 3:
            return 0.0

        max_diagonal = 0.0
        for i in range(len(self.__points)):
            for j in range(i + 1, len(self.__points)):
                dist = self.__points[i].distance_to(self.__points[j])
                if dist > max_diagonal:
                    max_diagonal = dist

        return max_diagonal

    def sort_by_x(self):
        return sorted(self.__points, key=lambda point: point.get_x())

    def sort_by_y(self):
        return sorted(self.__points, key=lambda point: point.get_y())

    def __str__(self):
        points_str = ", ".join([str(p) for p in self.__points])
        return f"Поліном (Колір: {self.__colour.name}, Точки: [{points_str}])"

    def __repr__(self):
        return f"Polynom({self.__colour}, *{self.__points})"


if __name__ == "__main__":
    print("Створення точок")
    p1 = Point(4, 0)
    p2 = Point(0, 3)
    p3 = Point(0, 0)
    p4 = Point(4, 3)
    print(f"Створені точки: {p1}, {p2}, {p3}, {p4}\n")

    print("Створення Поліному")
    polygon = Polynom(Colour.BLUE, p1, p2, p3, p4)

    print("\nДемонстрація __str__ та __repr__")
    print(f"Виклик str(polygon): {str(polygon)}")
    print(f"Виклик repr(polygon): {repr(polygon)}\n")

    print("Обчислення")
    print(f"Периметр: {polygon.calculate_perimeter():.2f}")
    print(f"Найдовша діагональ: {polygon.get_longest_diagonal():.2f}\n")

    print("Сортування")
    print(f"Початковий список точок: {[str(p) for p in polygon.get_points()]}")

    sorted_x = polygon.sort_by_x()
    print(f"Сортування X: {[str(p) for p in sorted_x]}")

    sorted_y = polygon.sort_by_y()
    print(f"Сортування Y: {[str(p) for p in sorted_y]}")