class Object:
    def __init__(self, name : str, coord: list):
        self.name = name
        self._coords = coord

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def coords(self):
        return self._coords

    @coords.setter
    def coords(self, coords):
        self._coords = coords


class Point(Object):
    def __init__(self, name : str , point : list):
        super().__init__(name, point)

class Line(Object):
    def __init__(self, name : str, points: list):
        super().__init__(name, points)

class Wireframe(Object):
    def __init__(self, name : str , points : list):
        super().__init__(name, points)
        