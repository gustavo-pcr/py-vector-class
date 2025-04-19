import math


class Vector:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.coord_x = round(coord_x, 2)
        self.coord_y = round(coord_y, 2)

    def __add__(self, other: object) -> object:
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(
            self.coord_x + other.coord_x,
            self.coord_y + other.coord_y,
        )

    def __sub__(self, other: object) -> object:
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(
            self.coord_x - other.coord_x,
            self.coord_y - other.coord_y,
        )

    def __mul__(self, other: object) -> object:
        if isinstance(other, (int, float)):
            return Vector(
                round(self.coord_x * other, 2),
                round(self.coord_y * other, 2),
            )
        if isinstance(other, Vector):
            return round(
                self.coord_x * other.coord_x + self.coord_y * other.coord_y, 4
            )
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> "Vector":
        delta_x = end_point[0] - start_point[0]
        delta_y = end_point[1] - start_point[1]
        return cls(delta_x, delta_y)

    def get_length(self) -> float:
        return math.sqrt(self.coord_x ** 2 + self.coord_y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(
            round(self.coord_x / length, 2),
            round(self.coord_y / length, 2),
        )

    def angle_between(self, other_vector: "Vector") -> int:
        dot_product = (
            self.coord_x * other_vector.coord_x
            + self.coord_y * other_vector.coord_y
        )
        self_length = self.get_length()
        other_length = other_vector.get_length()

        if self_length == 0 or other_length == 0:
            raise ValueError("Cannot calculate angle with zero-length vector.")

        cosine_angle = dot_product / (self_length * other_length)
        angle = math.degrees(math.acos(max(-1, min(1, cosine_angle))))
        return round(angle)

    def get_angle(self) -> int:
        vertical_axis = Vector(0, 1)
        return self.angle_between(vertical_axis)

    def rotate(self, degrees_to_rotate: int) -> "Vector":
        radians = math.radians(degrees_to_rotate)
        rotated_x = (
            self.coord_x * math.cos(radians)
            - self.coord_y * math.sin(radians)
        )
        rotated_y = (
            self.coord_x * math.sin(radians)
            + self.coord_y * math.cos(radians)
        )
        return Vector(round(rotated_x, 2), round(rotated_y, 2))

    def __repr__(self) -> str:
        return f"Vector({self.coord_x}, {self.coord_y})"
