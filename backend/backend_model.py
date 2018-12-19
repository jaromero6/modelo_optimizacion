from PyQt5.QtCore import pyqtSignal, QObject
from backend import model, db_functions



class BackendModel(QObject):

    module_signal = pyqtSignal(tuple)

    def __init__(self, parent):
        super().__init__()
        # Se conecta la señal del modulo con el frontend
        self.module_signal.connect(parent.show_module)
        self.model = model.modelo
        self.worker_modules = {"person": dict(zip([i for i in range(
            35)],[[] for i in range(35)])), "boss": dict(zip([i for i in range(
            35)],[[] for i in range(35)]))}
        self.model.optimize()
        self.get_results()

    def get_results(self):
        """
        Obtiene el resultado del modelo y manda una señal con los
        trabajadores asignados al frontend
        """
        basic_variables = map(lambda x: x.VarName.split(","), filter(lambda
                                                                   var:var.X,
                                             self.model.getVars()))
        for i in basic_variables:
            self.worker_modules[i[0]][int(i[2])].append(i[1])
        for i in self.worker_modules["person"]:
            self.module_signal.emit((i, self.worker_modules["person"][i],
                                     self.worker_modules[
                "boss"][i]))

    def save_model(self):
        db_functions.save_bd(self.worker_modules)





