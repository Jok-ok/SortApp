from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import (QTableWidget, QHeaderView,
                             QTableWidgetItem, QDesktopWidget,
                             QMainWindow, QPushButton)


class TableWindow:
    def __init__(self):
        self.start_window = None
        self.row = 1000
        self.col = 2

    def create_table(self, window, data):
        table = QTableWidget(window)
        table.setColumnCount(self.col)
        table.setRowCount(self.row)
        table.setHorizontalHeaderLabels(("Phrase", "Number"))
        table.setMinimumWidth(500)
        table.setMinimumHeight(800)
        table.setShowGrid(True)

        table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        table.verticalHeader().hide()

        for i, item in enumerate(data):
            for j, val in enumerate(item):
                table.setItem(i, j, QTableWidgetItem(str(val)))

        table.show()

    def create_table_window(self, back_window, data):
        self.start_window = back_window

        window = QMainWindow()

        window.setWindowTitle("Show Table")
        window.setFixedSize(QSize(500, 900))

        qt_rectangle = window.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        qt_rectangle.moveCenter(center_point)
        window.move(qt_rectangle.topLeft())

        btn_back = QPushButton(window)
        btn_back.move(390, 835)
        btn_back.setText("Меню")

        def back_btn_click():
            self.start_window.show()
            window.close()

        btn_back.clicked.connect(back_btn_click)

        btn_back.setFixedSize(QSize(100, 55))
        btn_back.setStyleSheet("background: #27AE61;"
                               "border-radius: 13%;"
                               "font-size: 25px;"
                               "color: #FFF")

        self.create_table(window, data)

        return window
