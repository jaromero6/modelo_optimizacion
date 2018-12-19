from PyQt5 import uic
from frontend import change_bd_window


class SelectChange(*uic.loadUiType("frontend/GUI/select_change.ui")):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.add_person.clicked.connect(self.add_person_bd)
        self.add_boss.clicked.connect(self.add_boss_bd)
        self.delete_person.clicked.connect(self.delete_person_bd)
        self.delete_boss.clicked.connect(self.delete_boss_bd)
        self.back_button.clicked.connect(self.back)

    def add_person_bd(self):
        self.hide()
        self.register_window = change_bd_window.AddWindow("persons", self)
        self.register_window.show()

    def add_boss_bd(self):
        self.hide()
        self.register_window = change_bd_window.AddWindow("boss", self)
        self.register_window.show()

    def delete_person_bd(self):
        pass

    def delete_boss_bd(self):
        pass

    def back(self):
        self.hide()
        self.parent.show()
