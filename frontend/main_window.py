from PyQt5 import uic
from frontend import get_model_window

first_window, class_window = uic.loadUiType("frontend/GUI/first_window.ui")

class FirstWindow(first_window, class_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.get_model_button.clicked.connect(self.get_model)
        self.bd_button.clicked.connect(self.modify_bd)

    def get_model(self):
        self.hide()
        self.model_window = get_model_window.ModelWindow()
        self.model_window.show()

    def modify_bd(self):
        pass

