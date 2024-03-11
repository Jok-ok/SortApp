from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QDesktopWidget, QMainWindow


def loading_window():
    window = QMainWindow()

    window.setWindowTitle("Обработка...")
    window.setFixedSize(QSize(500, 10))
    qt_rectangle = window.frameGeometry()
    center_point = QDesktopWidget().availableGeometry().center()
    qt_rectangle.moveCenter(center_point)
    window.move(qt_rectangle.topLeft())

    return window
