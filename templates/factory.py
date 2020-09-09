from .objects import Point, Line, Wireframe

class Factory():
    def create_point(self, name : str, coords : list):
        return Point(name, coords)
        