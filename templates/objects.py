class Object:
    def __init__(self, name : str, coord: list):
        self._name = name
        self._coords = coord

class Point(Object):
    def __init__(self, name : str , point : list):
        super().__init__(name, point)

class Line(Object):
    def __init__(self, name : str, p1 : tuple, p2: tuple):
        coords = []
        coords.append(p1)
        coords.append(p2)
        super().__init__(name, coords)

class Wireframe(Object):
    def __init__(self, name : str , points : list):
        super().__init__(name, points)
        