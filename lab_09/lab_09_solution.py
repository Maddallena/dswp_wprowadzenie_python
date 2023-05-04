class Point:

    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point({}, {})".format(self.x, self.y)

    def __mul__(self, other):
        return Point(self.x * other.x, self.y * other.y)

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x, self.y == other.y
        return False


x = Point(5, 6)
z = Point(5, 6)
# print(x==z)
# print(x)
# print(x*z)

class Polygon:
    def __init__(self, points: list = [Point]):
        self.points = []

    def add_point(self, point: Point):
        self.points.append(point)

    def __str__(self):
        points_str = ', '.join([str(x) for x in self.points])
        return f'Polygon[{points_str}]'

poli = Polygon()
poli.add_point(x)
poli.add_point(z)
print(poli)