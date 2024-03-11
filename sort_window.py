from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (QMainWindow, QPushButton,
                             QDesktopWidget, QComboBox,
                             QLabel, QSlider,
                             QRadioButton, QCheckBox)
import logic
from loading_window import loading_window
from table_window import TableWindow


class SortWindow:
    def __init__(self):
        self.start_window = None
        self.table_window = None
        self.word_count = 1
        self.sort_type = "max"
        self.column_index = 0
        self.is_nearby = True

    @staticmethod
    def get_column_names(data_frame):
        names = []
        header_row = data_frame.loc[0]

        for number in data_frame.keys():
            names.append(chr(number + 65) + ") " + str(header_row[number]))

        return names

    def set_word_count(self, count):
        self.word_count = count

    def set_max_sort_type(self, status):
        if status:
            self.sort_type = "max"

    def set_min_sort_type(self, status):
        if status:
            self.sort_type = "min"

    def set_is_nearby(self, status):
        self.is_nearby = status

    def get_phrases(self, data_frame):
        df_without_header = logic.delete_header_row(data_frame)
        client_sentences = logic.get_grouped_sentences(df_without_header,
                                                       self.column_index)

        if self.is_nearby:
            phrases = logic.get_nearby_phrases(client_sentences,
                                               self.word_count)
        else:
            phrases = logic.get_outlying_phrases(client_sentences,
                                                 self.word_count)

        phrase_count = logic.get_phrase_count_dict(phrases)
        sorted_phrases = logic.sort_phrases(phrase_count, self.sort_type)

        return sorted_phrases

    @staticmethod
    def set_label_value(label, value):
        label.setText(str(value))

    def create_sort_window(self, back_window, data_frame):
        self.start_window = back_window

        window = QMainWindow()

        window.setWindowTitle("Super sort app")
        window.setFixedSize(QSize(1000, 650))
        qt_rectangle = window.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        qt_rectangle.moveCenter(center_point)
        window.move(qt_rectangle.topLeft())

        column_text = QLabel(window)
        column_text.setText("Выберете колонку")
        column_text.move(310, 30)
        column_text.setStyleSheet("font-size: 25px")
        column_text.adjustSize()

        column_names = self.get_column_names(data_frame)

        combo = QComboBox(window)
        combo.setFixedSize(QSize(350, 65))
        combo.move(310, 80)
        combo.setStyleSheet("QComboBox"
                            "{"
                            "border: 3px solid #27AE61;"
                            "border-radius: 13px;"
                            "font-size: 22px;"
                            "padding-left: 10px;"
                            "}"
                            "QComboBox::drop-down { "
                            "border: none"
                            "}"
                            "QComboBox QAbstractItemView { "
                            "font-size: 22px;"
                            "border: 3px solid #27AE61;"
                            "selection-background-color: #27AE61;"
                            "}"
                            "QComboBox QAbstractItemView::item { "
                            "border-radius: 13px;"
                            "padding: 20px;"
                            "min-height: 50px"
                            "}"
                            )

        combo.addItems(column_names)

        def set_column_index():
            self.column_index = combo.currentIndex()

        if len(column_names) > 7:
            combo.setCurrentIndex(7)
            set_column_index()

        combo.currentTextChanged.connect(set_column_index)

        sld_text = QLabel(window)
        sld_text.setText("Количество слов")
        sld_text.move(310, 200)
        sld_text.setStyleSheet("font-size: 25px")
        sld_text.adjustSize()

        sld = QSlider(Qt.Horizontal, window)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setFixedSize(QSize(350, 40))
        sld.setRange(1, 6)
        sld.setValue(1)
        sld.move(310, 250)
        sld.setStyleSheet("QSlider::handle:horizontal {"
                          "border-radius: 15px;"
                          "width: 30px;"
                          "margin-top: -15px;"
                          "background: #27AE61;"
                          "}")

        sld_value_text = QLabel(window)
        sld_value_text.setText("1")
        sld_value_text.move(680, 250)
        sld_value_text.setStyleSheet("font-size: 22px")
        sld_value_text.adjustSize()

        def change_word_count(count):
            self.set_label_value(sld_value_text, count)
            self.set_word_count(count)

        sld.valueChanged[int].connect(change_word_count)

        radiobutton_text = QLabel(window)
        radiobutton_text.setText("Cортировать по")
        radiobutton_text.move(310, 350)
        radiobutton_text.setStyleSheet("font-size: 25px")
        radiobutton_text.adjustSize()

        radiobutton_max = QRadioButton("Max", window)
        radiobutton_max.value = "Max"
        radiobutton_max.setChecked(True)
        radiobutton_max.move(310, 400)
        radiobutton_max.setStyleSheet(
            "QRadioButton {"
            "font-size: 22px"
            "}"
            "QRadioButton::indicator:unchecked {"
            "border: 3px solid #27AE61;"
            "min-width: 30;"
            "min-height: 30"
            "}"
            "QRadioButton::indicator:checked"
            "{"
            "background: #27AE61;"
            "min-width: 30;"
            "min-height: 30"
            "}")
        radiobutton_max.toggled.connect(self.set_max_sort_type)

        radiobutton_min = QRadioButton("Min", window)
        radiobutton_min.value = "Min"
        radiobutton_min.move(520, 400)
        radiobutton_min.setStyleSheet(
            "QRadioButton {"
            "font-size: 22px"
            "}"
            "QRadioButton::indicator:unchecked {"
            "border: 3px solid #27AE61;"
            "min-width: 30;"
            "min-height: 30"
            "}"
            "QRadioButton::indicator:checked"
            "{"
            "background: #27AE61;"
            "min-width: 30;"
            "min-height: 30"
            "}")
        radiobutton_min.toggled.connect(self.set_min_sort_type)

        checkbox = QCheckBox('Рядом стоящие', window)

        checkbox.move(310, 470)
        checkbox.setFixedSize(QSize(300, 30))

        checkbox.setStyleSheet(
            "QCheckBox {"
            "font-size: 22px"
            "}"
            "QCheckBox::indicator:unchecked {"
            "border: 3px solid #27AE61;"
            "min-width: 30;"
            "min-height: 30"
            "}"
            "QCheckBox::indicator:checked"
            "{"
            "background: #27AE61;"
            "min-width: 30;"
            "min-height: 30"
            "}")

        checkbox.setChecked(True)

        checkbox.toggled.connect(self.set_is_nearby)

        btn_search = QPushButton(window)
        btn_search.move(450, 540)
        btn_search.setText("Поиск")

        def search_btn_click():
            window.close()
            loading = loading_window()
            loading.show()

            phrases = self.get_phrases(data_frame)

            self.table_window = TableWindow().create_table_window(
                back_window, phrases[:1000])
            self.table_window.show()

        btn_search.clicked.connect(search_btn_click)

        btn_search.setFixedSize(QSize(100, 55))
        btn_search.setStyleSheet("background: #27AE61;"
                                 "border-radius: 13%;"
                                 "font-size: 25px;"
                                 "color: #FFF")

        btn_back = QPushButton(window)
        btn_back.move(870, 540)
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

        return window
