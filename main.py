from PyQt5.QtWidgets import QApplication
from frontend import main_window
import sys


def hook(type, value, traceback):
    print(type)
    print(traceback)


if __name__ == "__main__":
    sys.__excepthook__ = hook
    app = QApplication(sys.argv)
    window = main_window.FirstWindow()
    window.show()
    sys.exit(app.exec())