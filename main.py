import sys
from PySide2.QtWidgets import QApplication
from aplication.main_window import Janela



class AppController:
    def __init__(self):
        app = QApplication(sys.argv)

        self.window = Janela()
        self.window.add_new_object.triggered.connect(
            self.new_obj_handler)

        self.add_btn_handlers()
        

        sys.exit(app.exec_())
    
    def new_obj_handler(self):
        print("new obj")
        
    def add_btn_handlers(self):
        self.window.zoom_in.clicked.connect(lambda: self.zoom_action(True))

        self.window.zoom_out.clicked.connect(lambda: self.zoom_action(False))

        self.window.move_up.clicked.connect(lambda: self.move_view("up"))

        self.window.move_down.clicked.connect(lambda: self.move_view("down"))

        self.window.move_left.clicked.connect(lambda: self.move_view("left"))

        self.window.move_right.clicked.connect(lambda: self.move_view("right"))


    def move_view(self, direction):
        print("move_view")
        print(direction)

    def zoom_action(self, direction):
        print("zoom")
        print(direction)


        


if __name__ == "__main__":
    AppController()
    
        
