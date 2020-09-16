from PySide2 import QtWidgets, QtCore, QtGui
from templates.objects import Point, Line, Wireframe


class Viewport(QtWidgets.QLabel):

    def __init__(self, parent):
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
        for obj in self.objects:
            if type(obj) == tuple:
                x, y = obj
                qp.drawPoint(x, y)

            else:
                prev_p = obj[0]
                for p in obj[1:]:
                    xs, ys = prev_p
                    xe, ye = p
                    qp.drawLine(xs, ys, xe, ye)
                    prev_p = p

        qp.end()

    def point_inside_viewport(self, point: list):
        return point[0] >= self.current_base_x and \
            point[0] <= self.current_base_x + self.current_width and \
            point[1] >= self.current_base_y and \
            point[1] <= self.current_base_y + self.current_height
