from PySide2 import QtWidgets, QtCore, QtGui

from .viewport import Viewport


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.items_model = QtGui.QStandardItemModel()
        self.main_menu = QtWidgets.QGroupBox(self)
        self.window_menu_label = QtWidgets.QLabel(self.main_menu)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.zoom_lbl = QtWidgets.QLabel(self.main_menu)
        self.zoom_in = QtWidgets.QPushButton(self.main_menu)
        self.zoom_out = QtWidgets.QPushButton(self.main_menu)
        self.degrees_lbl = QtWidgets.QLabel(self.main_menu)
        self.degrees_input = QtWidgets.QLineEdit(self.main_menu)
        self.degrees_unit_lbl = QtWidgets.QLabel(self.main_menu)
        self.step_label = QtWidgets.QLabel(self.main_menu)
        self.step_percent_label = QtWidgets.QLabel(self.main_menu)
        self.step_input = QtWidgets.QLineEdit(self.main_menu)
        self.projection_lbl = QtWidgets.QLabel(self.main_menu)
        self.add_new_object = QtWidgets.QAction(self)
        self.set_window_btn = QtWidgets.QPushButton(self.main_menu)
        self.rotate_lbl = QtWidgets.QLabel(self.main_menu)
        self.rotate_x_btn = QtWidgets.QPushButton(self.main_menu)
        self.rotate_y_btn = QtWidgets.QPushButton(self.main_menu)
        self.rotate_z_btn = QtWidgets.QPushButton(self.main_menu)
        self.parallel_radio_btn = QtWidgets.QRadioButton(self.main_menu)
        self.perspective_radio_btn = QtWidgets.QRadioButton(self.main_menu)
        self.viewport = Viewport(self)
        self.posx = 0
        self.posy = 0
        self.width = 800
        self.height = 600
        self.title = "Sistema Gráfico Iterativo"
        self.setObjectName('MainWindow')
        self.createWindow()

    def createWindow(self):
        self.setGeometry(self.posx, self.posy, self.width, self.height)
        self.setWindowTitle(self.title)
        self.window_menu_label.setGeometry(QtCore.QRect(10, 180, 110, 15))
        self.window_menu_label.setText("Window Menu")
        self.main_menu.setTitle("Tools")
        self.main_menu.setGeometry(QtCore.QRect(5, 20, 180, 600))
        self.add_transform_buttons()
        self.add_object_list()

        self.step_label.setGeometry(QtCore.QRect(10, 200, 30, 15))
        self.step_label.setText("Step:")
        self.zoom_in.setGeometry(QtCore.QRect(70, 420, 30, 20))
        self.zoom_in.setText("+")
        self.zoom_out.setGeometry(QtCore.QRect(20, 420, 30, 25))
        self.zoom_out.setText("-")

        self.step_percent_label.setGeometry(QtCore.QRect(100, 200, 20, 15))
        self.step_percent_label.setText("%")
        self.degrees_unit_lbl.setGeometry(QtCore.QRect(120, 330, 15, 15))
        self.degrees_unit_lbl.setText("º")
        self.degrees_lbl.setGeometry(QtCore.QRect(10, 330, 55, 15))
        self.degrees_lbl.setText("Angle")

        self.degrees_input.setText('0')
        self.degrees_input.setGeometry(QtCore.QRect(70, 330, 40, 25))
        self.degrees_input.setValidator(QtGui.QIntValidator(0, 360))
        self.step_input.setText('1')
        self.step_input.setGeometry(QtCore.QRect(50, 200, 40, 25))
        self.step_input.setValidator(QtGui.QIntValidator(0, 99))

        self.zoom_lbl.setGeometry(QtCore.QRect(30, 400, 55, 15))
        self.zoom_lbl.setText("Zoom")
        self.projection_lbl.setGeometry(QtCore.QRect(10, 490, 80, 15))
        self.projection_lbl.setText("Projection")
        self.set_window_btn.setGeometry(QtCore.QRect(20, 450, 80, 25))
        self.set_window_btn.setText("Set Window")

        self.parallel_radio_btn.toggle()
        self.parallel_radio_btn.setGeometry(QtCore.QRect(10, 510, 99, 20))
        self.parallel_radio_btn.setText("Parallel")
        self.perspective_radio_btn.setGeometry(QtCore.QRect(10, 530, 99, 20))
        self.perspective_radio_btn.setText("Perspective")

        self.rotate_lbl.setGeometry(QtCore.QRect(10, 300, 55, 15))
        self.rotate_lbl.setText("Rotate")
        self.rotate_x_btn.setGeometry(QtCore.QRect(20, 370, 30, 25))
        self.rotate_x_btn.setText("X")
        self.rotate_y_btn.setGeometry(QtCore.QRect(60, 370, 30, 25))
        self.rotate_y_btn.setText("Y")
        self.rotate_z_btn.setGeometry(QtCore.QRect(100, 370, 30, 25))
        self.rotate_z_btn.setText("Z")

        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menuFile.setTitle("File")
        self.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.add_new_object)
        self.add_new_object.setText("Add object")

        # Canvas
        self.viewport.setGeometry(QtCore.QRect(168, 23, 512, 512))
        self.show()

    def add_transform_buttons(self):
        self.move_up = QtWidgets.QPushButton(self.main_menu)
        self.move_up.setGeometry(QtCore.QRect(30, 227, 40, 25))
        self.move_up.setText("Up")

        self.move_right = QtWidgets.QPushButton(self.main_menu)
        self.move_right.setGeometry(QtCore.QRect(52, 250, 40, 25))
        self.move_right.setText("Right")

        self.move_left = QtWidgets.QPushButton(self.main_menu)
        self.move_left.setGeometry(QtCore.QRect(10, 250, 40, 25))
        self.move_left.setText("Left")

        self.move_down = QtWidgets.QPushButton(self.main_menu)
        self.move_down.setGeometry(QtCore.QRect(30, 273, 40, 25))
        self.move_down.setText("Down")

    def add_object_list(self):
        # object list
        self.object_list = QtWidgets.QListView(self.main_menu)
        self.object_list.setGeometry(QtCore.QRect(10, 50, 150, 120))
        self.object_list.setModel(self.items_model)

        # object label
        self.objects_lbl = QtWidgets.QLabel(self.main_menu)
        self.objects_lbl.setGeometry(QtCore.QRect(10, 30, 55, 15))
        self.objects_lbl.setText("Objects")
