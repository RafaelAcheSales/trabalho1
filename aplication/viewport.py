from PySide2 import QtWidgets, QtCore, QtGui
from templates.objects import Point, Line, Wireframe


class Viewport(QtWidgets.QLabel):

    def __init__(self, parent):
        print(parent)
        print(type(parent))
        super(Viewport, self).__init__(parent)

        # Object style sheet
        stylesheet = '''
            QLabel {
                background-color: white;
                border: 1px solid black
            }
        '''
        self.setStyleSheet(stylesheet)

        # Variable to hold objects to be drew
        self.objects = []

    def draw(self, objects):
        self.objects = objects
        self.update()

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        pen = QtGui.QPen()
        pen.setWidth(3)
        pen.setColor(QtGui.QColor(0, 0, 0))
        qp.setPen(pen)
        print(self.objects)
        for obj in self.objects:
            # In case it is a point
            if len(obj) == 2:
                x, y = obj
                qp.drawPoint(x, y)

            else:
                # In case is a multiple point object
                prev_p = obj[0]
                for p in obj[1:]:
                    xs, ys = prev_p
                    xe, ye = p
                    print(xs, ys, xe, ye)
                    qp.drawLine(xs, ys, xe, ye)
                    prev_p = p

        qp.end()

    def point_inside_viewport(self, point: list):
        """
        Check if point is inside current viewport

        Parameters
        --------
        point: Point3D

        Return
        --------
        True/False
        """
        return point[0] >= self.current_base_x and \
            point[0] <= self.current_base_x + self.current_width and \
            point[1] >= self.current_base_y and \
            point[1] <= self.current_base_y + self.current_height
