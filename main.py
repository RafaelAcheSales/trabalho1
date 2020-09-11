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
        self.window_xmax = 900
        self.window_ymax = 600

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

    def add_point(self, tab):
        point = []
        coords_tuple = (int(tab.x_coord_pt_input.text()), int(tab.y_coord_pt_input.text()), int(tab.z_coord_pt_input.text()))
        point.append(coords_tuple)
        print(point)
        created_point = Factory.create_point("rafa", point)
        self.object_list.append(created_point)
        print(created_point)

    def add_line(self, tab):
        p1 = (int(tab.start_x_coord_line_input.text()),
            int(tab.start_y_coord_line_input.text()),
            int(tab.start_z_coord_line_input.text())
        )

        p2 = (int(tab.end_x_coord_line_input.text()),
            int(tab.end_y_coord_line_input.text()),
            int(tab.end_z_coord_line_input.text())
        )
        print(p1 + p2)

    def add_wireframe(self, tab):
        print("sim")

    def update_viewport(self):
        self.main_window.viewport.draw(transformed_objects)
    def on_new_object(self):
        tab_name, tab_instance = self.add_object_dialog.active_tab()
        self.objects_callbacks[tab_name](tab_instance)

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
        xw = p[0]
        yw = p[1]

        xwmax = self.window_xmax
        ywmax = self.window_ymax
        xwmin = self.window_xmin
        ywmin = self.window_ymin

        xvpmax = self.xvp_max
        yvpmax = self.yvp_max
        xvpmin = self.xvp_min
        yvpmin = self.yvp_min

        xvp = ((xw - xwmin)/(xwmax - xwmin)) * (xvpmax - xvpmin) - self.xvp_min
        yvp = (1 - ((yw - ywmin)/(ywmax - ywmin))) * \
            (yvpmax - yvpmin) - self.yvp_min

        return (xvp, yvp)



if __name__ == "__main__":
    AppController()
    
        
