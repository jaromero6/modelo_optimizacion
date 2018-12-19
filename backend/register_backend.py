from PyQt5.QtCore import QObject, pyqtSignal
from backend import db_functions

class User(QObject):

    information_signal = pyqtSignal(str)

    def __init__(self,bd_type, parent):
        super().__init__()
        self.bd_type = bd_type
        self.information_signal.connect(parent.show_warning)

    def save_information(self, signal):
        modules_list = []
        for i in range(1,36):
            modules_list.append(str(int(i in signal[1])))
        if not db_functions.add_new_person(f"backend/bd/{self.bd_type}_bd.csv",
                                         signal[
            0], ",".join(modules_list)):
            self.information_signal.emit("El usuario ya existe")
        else:
            self.information_signal.emit("Usuario agregado exitosamente")








