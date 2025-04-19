import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: object) -> object:
        return Vector(self.x + self.y, other.x + other.y)

    def __sub__(self, other: object) -> object:
        return Vector(self.x - self.y, other.x - other.y)

    def __mul__(self, other: object) -> object:
        if isinstance(other, int) or isinstance(other, float):
            return Vector(self.x * other, self.y * other)
        return round(self.x * other.x, self.y * other.y, 4)

    @classmethods
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple) -> "Vector":
        x = end_point[0] - start_point[0]
        y = end_point[1] - start_point[1]
        return cls(x, y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(round(self.x / length, 2), round(self.y / length, 2))

    def angle_between(self, other: "Vector") -> int:
        dot = self.x * other.x + self.y * other.y
        len_self = self.get_length()
        len_other = other.get_length()

    def get_angle(self) -> int:
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        x_new = self.x * math.cos(radians) - self.y * math.sin(radians)
        y_new = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(round(x_new, 2), round(y_new, 2))

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"
