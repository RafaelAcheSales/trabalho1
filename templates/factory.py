from .objects import Point, Line, Wireframe


class Factory():
    def create_point(self, name: str, coords: list):
        return Point(name, coords)

    def create_line(self, name: str, coords: list):
        return Line(name, coords)

    def create_wireframe(self, name: str, coords: list):
        return Wireframe(name, coords)
