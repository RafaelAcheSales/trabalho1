import numpy as np
import math

class ObjTransformator():
    def calculate_center(self, coords):
        xc = 0
        yc = 0
        for point in coords:
            xc += point[0]
            yc += point[1]
        xc /= len(coords)
        yc /= len(coords)
        return xc, yc

    def translate(self, coords, dx, dy):
        self.transform_matrix = np.array([[1, 0, 0,], [0, 1, 0], [dx, dy, 1]])
        return self.apply_transform(coords)
                
    def rotate(self, coords, angle, mode="CENTER", point=(0, 0)):
        angle = math.radians(angle)
        if mode == "CENTER":
            print("CENTER") 
            cx, cy = self.calculate_center(coords)
            new_coords = self.translate(coords, -cx, -cy)
            print(cx, cy)
        elif mode == "POINT":
            new_coords = self.translate(coords, point[0], point[1])
            cx , cy = point
        elif mode == "WORLD":
            self.transform_matrix = np.array([[math.cos(angle),-math.sin(angle) , 0,],
            [math.sin(angle), math.cos(angle), 0],
            [0, 0, 1]])
            return self.apply_transform(coords)
        self.transform_matrix = np.array([[math.cos(angle),-math.sin(angle) , 0,],
            [math.sin(angle), math.cos(angle), 0],
            [0, 0, 1]])
        return self.translate(self.apply_transform(new_coords), cx, cy)
        

    def scale(self, coords, sx, sy):
        cx, cy = self.calculate_center(coords)
        coords = self.translate(coords, -cx, -cy)
        self.transform_matrix = np.array([[sx, 0, 0,], [0, sy, 0], [0, 0, 1]])
        coords = self.apply_transform(coords)
        return self.translate(coords, cx, cy)

    def apply_transform(self, coords):
        print("apply")
        print(".............")
        print(self.transform_matrix)
        new_coords = []
        for point in coords:
            p = np.array([point[0], point[1], 1])
            new_coords.append(p.dot(self.transform_matrix))
        print(new_coords)
        return new_coords