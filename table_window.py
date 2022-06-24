from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *


row = 1000
col = 2


def create_table(window, data):
    global row, col

    table = QTableWidget(window)
    table.setColumnCount(col)
    table.setRowCount(row)
    table.setHorizontalHeaderLabels(("Phrase", "Number"))
    table.setMinimumWidth(500)
    table.setMinimumHeight(800)
    table.setShowGrid(True)

    table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
    table.verticalHeader().hide()

    for i, row in enumerate(data):
        for j, val in enumerate(row):
            table.setItem(i, j, QTableWidgetItem(str(val)))

    table.show()


def TableWindow(data):
    window = QMainWindow()

    window.setWindowTitle("Show Table")
    window.setFixedSize(QSize(500, 800))

    qtRectangle = window.frameGeometry()
    centerPoint = QDesktopWidget().availableGeometry().center()
    qtRectangle.moveCenter(centerPoint)
    window.move(qtRectangle.topLeft())

    create_table(window, data)

    return window
