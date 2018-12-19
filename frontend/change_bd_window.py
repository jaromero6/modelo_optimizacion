from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from backend import register_backend


class AddWindow(*uic.loadUiType("frontend/GUI/register_window.ui")):

    information_signal = pyqtSignal(tuple)

    def __init__(self, bd_type, parent):
        super().__init__()
        self.setupUi(self)
        self.backend = register_backend.User(bd_type, self)
        self.parent = parent
        self.back_button.clicked.connect(self.back)
        self.save_button.clicked.connect(self.save)
        self.information_signal.connect(self.backend.save_information)

    def back(self):
        self.hide()
        self.parent.show()

    def get_modules(self):
        modules_selected = set()
        for i in range(1, 36):
            if getattr(self, f"checkBox_{i}").isChecked():
                modules_selected.add(i)
        return modules_selected

    def save(self):
        self.save_button.hide()
        self.back_button.hide()
        if self.name_input.text():
            modules_selected = self.get_modules()
            if modules_selected:
                self.information_signal.emit((self.name_input.text(),
                                              modules_selected))
            else:
                self.show_warning("Debe seleccionar módulos disponibles")
        else:
            self.show_warning("Debe rellenar con un nombre")


    def show_warning(self, message):
        self.warning_message.setText(message)
        self.back_button.show()
        self.save_button.show()


