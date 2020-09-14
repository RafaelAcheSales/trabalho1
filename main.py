import sys
from PySide2.QtCore import QTimer
from PySide2.QtWidgets import QApplication
from aplication.main_window import MainWindow
from aplication.new_object import NewObjectDialog
from templates.factory import Factory
from aplication.list_object import ListObject

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
        self.object_list.append(Factory.create_line("rafa", [(0, 20, 200), (300, 90, 0)]))
        self.update_viewport()
        sys.exit(self.app.exec_())

    def create_obj_dialog(self):
        self.add_object_dialog = NewObjectDialog()
        self.add_object_dialog.show()
        self.add_object_dialog.setVisible(False)
        self.add_object_dialog.buttonBox.accepted.connect(self.on_new_object)

    def on_new_object(self):
        tab_name, tab_instance = self.add_object_dialog.active_tab()
        obj_name = self.add_object_dialog.name_input.text().strip()
        object = self.objects_callbacks[tab_name](tab_instance, obj_name)
        item = ListObject(object)
        self.main_window.items_model.appendRow(item)
        self.update_viewport()

    def add_point(self, tab, name):
        point = []
        coords_tuple = (int(tab.x_coord_pt_input.text()), int(tab.y_coord_pt_input.text()), int(tab.z_coord_pt_input.text()))
        point.append(coords_tuple)
        print("point added")
        created_point = Factory.create_point(name, point)
        self.object_list.append(created_point)
        print(created_point)
        return created_point

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
        return created_line

    def add_wireframe(self, tab, name):
        points = []
        for i, point in enumerate(tab.points_list):
            x, y, z = point
            point = (x,  y)
            points.append(point)
        print(points)
        created_wireframe = Factory.create_wireframe(name, points)
        self.object_list.append(created_wireframe)
        return created_wireframe
        

    def update_viewport(self):
        transformed_objects = []
        for obj in self.object_list:
            coords = obj.coords
            if len(coords) == 1 :
                print("Ponto")
                transformed_objects.append(self.transform_point(coords[0]))
            else:
                print("wireframe")
                new_obj = []
                for p in coords:
                    new_obj.append(self.transform_point(p))
                transformed_objects.append(new_obj)
        self.main_window.viewport.draw(transformed_objects)


    def dialog_handler(self):
        self.add_object_dialog.setVisible(True)
        
    def add_btn_handlers(self):
        self.main_window.zoom_in.clicked.connect(lambda: self.zoom_action(True))

        self.main_window.zoom_out.clicked.connect(lambda: self.zoom_action(False))

        self.main_window.move_up.clicked.connect(lambda: self.move_view("down"))

        self.main_window.move_down.clicked.connect(lambda: self.move_view("up"))

        self.main_window.move_left.clicked.connect(lambda: self.move_view("right"))

        self.main_window.move_right.clicked.connect(lambda: self.move_view("left"))


    def move_view(self, direction):
        step = int(self.main_window.step_input.text())
        window_size_x = self.window_xmax - self.window_xmin
        window_size_y = self.window_ymax - self.window_ymin
        offsetx = window_size_x * step/100
        offsety = window_size_y * step/100

        if direction == 'up':
            self.yvp_max += offsety
            self.yvp_min += offsety

        elif direction == 'down':
            self.yvp_max -= offsety
            self.yvp_min -= offsety

        elif direction == 'right':
            self.xvp_max -= offsetx
            self.xvp_min -= offsetx

        elif direction == 'left':
            self.xvp_max += offsetx
            self.xvp_min += offsetx

        self.update_viewport()

    def zoom_action(self, direction):
        step = int(self.main_window.step_input.text())
        if direction:
            self.window_xmax *= (1 - step/100)
            self.window_ymax *= (1 - step/100)

        else:
            self.window_xmax *= (1 + step/100)
            self.window_ymax *= (1 + step/100)

        # Update objects on viewport
        self.update_viewport()

    def transform_point(self, p: list):
        print(p)
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
    
        
