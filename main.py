import sys
from PySide2.QtCore import QTimer
from PySide2.QtWidgets import QApplication
from aplication.main_window import MainWindow
from aplication.new_object import NewObjectDialog
from templates.factory import Factory

Factory = Factory()


class AppController:

    def __init__(self):
        # Initial window settings
        self.window_xmin = 0
        self.window_ymin = 0
        self.window_xmax = 512
        self.window_ymax = 512

        # Viewport values
        self.xvp_min = 0
        self.yvp_min = 0
        self.xvp_max = 512
        self.yvp_max = 512

        self.app = QApplication(sys.argv)
        self.main_window = MainWindow()
        self.objects_callbacks = {"Point": self.add_point, "Line": self.add_line, "Wireframe": self.add_wireframe}
        self.object_list = []
        self.create_obj_dialog()
        self.main_window.add_new_object.triggered.connect(
            self.dialog_handler)

        self.add_btn_handlers()
        self.main_window.show()

        timer = QTimer()
        timer.timeout.connect(lambda: None)
        timer.start(100)

        sys.exit(self.app.exec_())

    def create_obj_dialog(self):
        self.add_object_dialog = NewObjectDialog()
        self.add_object_dialog.show()
        self.add_object_dialog.setVisible(False)
        self.add_object_dialog.buttonBox.accepted.connect(self.on_new_object)

    def add_point(self, tab, name):
        point = []
        coords_tuple = (int(tab.x_coord_pt_input.text()), int(tab.y_coord_pt_input.text()),
                        int(tab.z_coord_pt_input.text()))
        point.append(coords_tuple)
        print("point added")
        created_point = Factory.create_point(tab, point)
        self.object_list.append(created_point)
        self.update_viewport()

    def add_line(self, tab, name):
        coords = []
        print("LINE ADDED")
        p1 = (int(tab.start_x_coord_line_input.text()),
              int(tab.start_y_coord_line_input.text()),
              int(tab.start_z_coord_line_input.text())
              )

        p2 = (int(tab.end_x_coord_line_input.text()),
              int(tab.end_y_coord_line_input.text()),
              int(tab.end_z_coord_line_input.text())
              )
        coords.append(p1)
        coords.append(p2)
        created_line = Factory.create_line(name, coords)
        self.object_list.append(created_line)
        self.update_viewport()

    def add_wireframe(self, tab, name):
        points = []
        for i, point in enumerate(tab.points_list):
            x, y, z = point
            point = (x, y)
            points.append(point)
        print(points)
        created_wireframe = Factory.create_wireframe(name, points)
        self.object_list.append(created_wireframe)
        self.update_viewport()

    def update_viewport(self):
        transformed_objects = []
        print(self.object_list)
        for obj in self.object_list:
            coords = obj.coords
            if len(coords) == 1:
                print("Ponto")
                transformed_objects.append(self.transform_point(coords[0]))
            else:
                print("wireframe")
                new_obj = []
                for p in coords:
                    new_obj.append(self.transform_point(p))
                transformed_objects.append(new_obj)
        self.main_window.viewport.draw(transformed_objects)

    def on_new_object(self):
        tab_name, tab_instance = self.add_object_dialog.active_tab()
        obj_name = self.add_object_dialog.name_input.text().strip()
        self.objects_callbacks[tab_name](tab_instance, obj_name)

    def dialog_handler(self):
        self.add_object_dialog.setVisible(True)

    def add_btn_handlers(self):
        self.main_window.zoom_in.clicked.connect(lambda: self.zoom_action(True))

        self.main_window.zoom_out.clicked.connect(lambda: self.zoom_action(False))

        self.main_window.move_up.clicked.connect(lambda: self.move_view("up"))

        self.main_window.move_down.clicked.connect(lambda: self.move_view("down"))

        self.main_window.move_left.clicked.connect(lambda: self.move_view("left"))

        self.main_window.move_right.clicked.connect(lambda: self.move_view("right"))

    def move_view(self, direction):
        print("move_view")
        print(direction)

    def zoom_action(self, direction):
        print("zoom")
        print(direction)

    def transform_point(self, p: list):
        print(p)
        xw = p[0]
        yw = p[1]

        xwmax: int = self.window_xmax
        ywmax: int = self.window_ymax
        xwmin: int = self.window_xmin
        ywmin: int = self.window_ymin

        xvpmax: int = self.xvp_max
        yvpmax: int = self.yvp_max
        xvpmin: int = self.xvp_min
        yvpmin: int = self.yvp_min

        xvp = ((xw - xwmin) / (xwmax - xwmin)) * (xvpmax - xvpmin) - self.xvp_min
        yvp = (1 - ((yw - ywmin) / (ywmax - ywmin))) * \
              (yvpmax - yvpmin) - self.yvp_min

        return xvp, yvp


if __name__ == "__main__":
    AppController()
