import pandas as pd
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import (QMainWindow, QPushButton,
                             QDesktopWidget, QFileDialog)
from sort_window import SortWindow


class StartWindow:
    def __init__(self):
        self.sort_window = None

    @staticmethod
    def get_data_from_xlsx(filepath):
        excel_data = pd.read_excel(filepath, header=None)
        return pd.DataFrame(excel_data)

    def choose_file(self, window):
        file_dialog = QFileDialog()
        file_dialog.setNameFilters(["XLSX files (*.xlsx)"])
        file_dialog.selectNameFilter("XLSX files (*.xlsx)")

        filepath = file_dialog.getOpenFileName()[0]

        if filepath and filepath.split(".")[-1] == "xlsx":
            data_frame = self.get_data_from_xlsx(filepath)
            self.sort_window = SortWindow()
            self.sort_window = self.sort_window.create_sort_window(window,
                                                                   data_frame)
            self.sort_window.show()
            window.close()

    def create_start_window(self):
        window = QMainWindow()

        window.setWindowTitle("Super sort app")
        window.setFixedSize(QSize(500, 300))
        qt_rectangle = window.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        qt_rectangle.moveCenter(center_point)
        window.move(qt_rectangle.topLeft())

        btn = QPushButton(window)
        btn.move(100, 110)
        btn.setText("+      Выбрать файл")

        def btn_click():
            self.choose_file(window)

        btn.clicked.connect(btn_click)

        btn.setFixedSize(QSize(300, 75))
        btn.setStyleSheet("background: #27AE61;"
                          "border-radius: 13%;"
                          "font-size: 25px;"
                          "color: #FFF")

        return window
