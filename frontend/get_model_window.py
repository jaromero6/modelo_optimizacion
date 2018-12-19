from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from backend import backend_model

model_window, class_window = uic.loadUiType("frontend/GUI/model_window.ui")


class ModelWindow(model_window, class_window):

    save_signal = pyqtSignal(bool)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.backend = backend_model.BackendModel(self)
        self.save_button.clicked.connect(self.save_model)
        self.save_signal.connect(self.backend.save_model)


    def show_module(self, signal):
        """
        Recibe una tupla con el numero del modulo y los integrantes de ese
        modulo que estarán en dicho modulo y los muestra
        """
        work_module = signal[0]
        if signal[1]:
            workers = "Tecnicos:\n" + "\n".join(signal[1]) + "\n"
            boss = "Jefe: " + "\n".join(signal[2]) + "\n"
            text = boss + workers

        else:
            text = "No asignado"
        getattr(self, f"m_{work_module}").setText(text)
    def save_model(self):
        self.save_signal.emit(True)
