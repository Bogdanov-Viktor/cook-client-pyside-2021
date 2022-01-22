import sys
from PySide6.QtWidgets import QApplication

from src.pages.AppWindow import AppWindow

if __name__ == '__main__':
    app = QApplication([])
    window = AppWindow()
    sys.exit(app.exec())
