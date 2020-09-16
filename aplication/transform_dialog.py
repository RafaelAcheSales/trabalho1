from PyQt5 import QtCore, QtGui, QtWidgets


class TransformDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.numeric_validator = QtGui.QIntValidator(0, 1000)

        self.initUi()

    def initUi(self):
        self.resize(400, 300)
        self.setWindowTitle("Transform object")
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(75, 260, 171, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)

        self.name_lbl = QtWidgets.QLabel(self)
        self.name_lbl.setGeometry(QtCore.QRect(10, 10, 41, 16))

        self.tab_panel = QtWidgets.QTabWidget(self)
        self.tab_panel.setEnabled(True)
        self.tab_panel.setGeometry(QtCore.QRect(10, 50, 370, 200))

        # Add a point mechanism
        self.translate_tab = Translate()
        self.tab_panel.addTab(self.translate_tab, "Translate")

        # Add a line mechanism
        self.rotate_tab = Rotate()
        self.tab_panel.addTab(self.rotate_tab, "Rotate")

        # Add wireframe mechanism
        self.scale_tab = Scale()
        self.tab_panel.addTab(self.scale_tab, "Scale")

        self.tab_panel.setCurrentIndex(0)

    def new_dialog(self, obj):
        self.object = obj
        self.name_lbl.setText(obj.name)
        self.setVisible(True)

    def reset_values(self):
        """
        Reset texts on input
        """
        # Reset name
        self.name_input.setText('')

        # Reset inputs for line
        self.rotate_tab.reset_values()

        # Reset input for point
        self.translate_tab.reset_values()

        # Reset input for wireframe
        self.scale_tab.reset_values()

    def active_tab(self):
        """
        Get active tab from TabWidget
        """

        active_index = self.tab_panel.currentIndex()
        active_tab = self.tab_panel.currentWidget()
        active_tab_name = self.tab_panel.tabText(active_index)

        return active_tab_name, active_tab, self.object


class Rotate(QtWidgets.QWidget):
    """
    Tab for holding buttons and inputs for creating a line
    """

    def __init__(self):
        super().__init__()
        self.input_list = []
        self.numeric_validator = QtGui.QIntValidator(-1000, 1000)

        self.z_lbl_pt = QtWidgets.QLabel(self)
        self.z_lbl_pt.setGeometry(QtCore.QRect(160, 30, 21, 16))
        self.z_lbl_pt.setText("Z")
        self.input_list.append(self.z_lbl_pt)

        self.x_lbl_pt = QtWidgets.QLabel(self)
        self.x_lbl_pt.setGeometry(QtCore.QRect(20, 30, 21, 16))
        self.x_lbl_pt.setText("X")
        self.input_list.append(self.x_lbl_pt)

        self.x = QtWidgets.QLineEdit(self)
        self.x.setGeometry(QtCore.QRect(10, 50, 41, 23))
        self.x.setValidator(self.numeric_validator)
        self.x.setText("0")
        self.input_list.append(self.x)

        self.y = QtWidgets.QLineEdit(self)
        self.y.setGeometry(QtCore.QRect(80, 50, 41, 23))
        self.y.setValidator(self.numeric_validator)
        self.y.setText("0")
        self.input_list.append(self.y)

        self.z = QtWidgets.QLineEdit(self)
        self.z.setGeometry(QtCore.QRect(150, 50, 41, 23))
        self.z.setValidator(self.numeric_validator)
        self.z.setText("0")
        self.input_list.append(self.z)

        self.y_lbl_pt = QtWidgets.QLabel(self)
        self.y_lbl_pt.setGeometry(QtCore.QRect(90, 30, 21, 16))
        self.y_lbl_pt.setText("Y")
        self.input_list.append(self.y_lbl_pt)

        self.angle_input = QtWidgets.QLineEdit(self)
        self.angle_input.setGeometry(QtCore.QRect(220, 50, 41, 23))
        self.combo = QtWidgets.QComboBox(self)
        self.combo.addItem("CENTER")
        self.combo.addItem("POINT")
        self.combo.addItem("WORLD")
        self.combo.activated[str].connect(self.combo_changed)
        self.combo_changed("CENTER")
        

        self.angle_label = QtWidgets.QLabel(self)
        self.angle_label.setGeometry(QtCore.QRect(220, 30, 60, 18))
        self.angle_label.setText('Angle')

    def reset_values(self):
        """
        Reset inputs to empty value
        """

        self.angle_input.setText('')
    
    def combo_changed(self, text):
        for item in self.input_list:
                item.setVisible(text == "POINT")
            


class Translate(QtWidgets.QWidget):
    """
    Tab for holding buttons and inputs for creating a point
    """

    def __init__(self):
        super().__init__()

        self.numeric_validator = QtGui.QIntValidator(-1000, 1000)

        self.z_lbl_pt = QtWidgets.QLabel(self)
        self.z_lbl_pt.setGeometry(QtCore.QRect(160, 30, 21, 16))
        self.z_lbl_pt.setText("Z")

        self.x_lbl_pt = QtWidgets.QLabel(self)
        self.x_lbl_pt.setGeometry(QtCore.QRect(20, 30, 21, 16))
        self.x_lbl_pt.setText("X")

        self.x = QtWidgets.QLineEdit(self)
        self.x.setGeometry(QtCore.QRect(10, 50, 41, 23))
        self.x.setValidator(self.numeric_validator)

        self.y = QtWidgets.QLineEdit(self)
        self.y.setGeometry(QtCore.QRect(80, 50, 41, 23))
        self.y.setValidator(self.numeric_validator)

        self.z = QtWidgets.QLineEdit(self)
        self.z.setGeometry(QtCore.QRect(150, 50, 41, 23))
        self.z.setValidator(self.numeric_validator)

        self.y_lbl_pt = QtWidgets.QLabel(self)
        self.y_lbl_pt.setGeometry(QtCore.QRect(90, 30, 21, 16))
        self.y_lbl_pt.setText("Y")

    def reset_values(self):
        """
        Reset inputs to empty value
        """
        # Reset inputs for point
        self.x.setText('')
        self.y.setText('')
        self.z.setText('')


class Scale(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.numeric_validator = QtGui.QIntValidator(-1000, 1000)

        self.z_lbl_pt = QtWidgets.QLabel(self)
        self.z_lbl_pt.setGeometry(QtCore.QRect(160, 30, 21, 16))
        self.z_lbl_pt.setText("Z")

        self.x_lbl_pt = QtWidgets.QLabel(self)
        self.x_lbl_pt.setGeometry(QtCore.QRect(20, 30, 21, 16))
        self.x_lbl_pt.setText("X")

        self.sx = QtWidgets.QLineEdit(self)
        self.sx.setGeometry(QtCore.QRect(10, 50, 41, 23))
        self.sx.setValidator(self.numeric_validator)

        self.sy = QtWidgets.QLineEdit(self)
        self.sy.setGeometry(QtCore.QRect(80, 50, 41, 23))
        self.sy.setValidator(self.numeric_validator)

        self.sz = QtWidgets.QLineEdit(self)
        self.sz.setGeometry(QtCore.QRect(150, 50, 41, 23))
        self.sz.setValidator(self.numeric_validator)

        self.y_lbl_pt = QtWidgets.QLabel(self)
        self.y_lbl_pt.setGeometry(QtCore.QRect(90, 30, 21, 16))
        self.y_lbl_pt.setText("Y")

    

    def reset_values(self):
        """
        Reset inputs to empty value
        """

        self.x.clear()
        self.y.clear()
        self.z.clear()
        self.points_model.clear()
