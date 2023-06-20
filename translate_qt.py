#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# author        : el3arbi bdabve@gmail.com with ChatGPT as assistant
# created       : 20-June-2023
#
# description   :
# usage         :
# ----------------------------------------------------------------------------

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from h_interface import Ui_MainWindow
from translator import translate


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load the .ui file
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("My Application")
        self.setGeometry(200, 200, 400, 300)

        # Connect the button click event
        self.ui.search_button.clicked.connect(self.search)

        # Set dark style sheet
        self.setStyleSheet("""
QMainWindow {
    background-color: #2C2C2C;
}

QLabel {
    color: #FFFFFF;
    font-family: Monaco;
    font-size: 12px;
    padding: 10px;
    height: 30px;
}

/* LINE EDIT */
QLineEdit {
    background-color: #404040;
    color: #FFFFFF;
    border: 1px solid #999999;
    border-radius: 5px;
    padding: 8px;
    height: 30px;
    font-family: Monaco;
}

/* PUSH BUTTON */
QPushButton {
    background-color: #3C3C3C;
    color: #FFFFFF;
    border: none;
    padding: 8px;
    border-radius: 5px;
    height: 30px;
    font-family: Monaco;
}

QPushButton:hover {
    background-color: #4C4C4C;
}

QPushButton:pressed {
    background-color: #2C2C2C;
}

/* LIST WIDGET */
QListWidget {
    background-color: #404040;
    color: #FFFFFF;
    border: 1px solid #999999;
    border-radius: 5px;
    padding: 8px;
    font-family: Monaco;
}

QListWidget::item:selected {
    background-color: #666666;
}

/* VERTICAL SCROLL BAR */
QScrollBar:vertical {
    background-color: #404040;
    width: 12px;
    margin: 16px 0 16px 0;
    border-radius: 6px;
}

QScrollBar::handle:vertical {
    background-color: #666666;
    min-height: 20px;
    border-radius: 6px;
}

QScrollBar::handle:vertical:hover {
    background-color: #888888;
}

QScrollBar::add-line:vertical {
    background-color: #404040;
    height: 16px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
    border-radius: 6px;
}

QScrollBar::sub-line:vertical {
    background-color: #404040;
    height: 16px;
    subcontrol-position: top;
    subcontrol-origin: margin;
    border-radius: 6px;
}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    background-color: #2C2C2C;
    border-radius: 6px;
}

/* Horizontal SCROLL BAR */
QScrollBar:horizontal {
    background-color: #404040;
    height: 12px;
    margin: 0 16px 0 16px;
    border-radius: 6px;
}

QScrollBar::handle:horizontal {
    background-color: #666666;
    min-width: 20px;
    border-radius: 6px;
}

QScrollBar::handle:horizontal:hover {
    background-color: #888888;
}

QScrollBar::add-line:horizontal {
    background-color: #404040;
    width: 16px;
    subcontrol-position: right;
    subcontrol-origin: margin;
    border-radius: 6px;
}

QScrollBar::sub-line:horizontal {
    background-color: #404040;
    width: 16px;
    subcontrol-position: left;
    subcontrol-origin: margin;
    border-radius: 6px;
}

QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
    background-color: #2C2C2C;
    border-radius: 6px;
}
        """)

    def search(self):
        search_text = self.ui.input_field.text()
        translation_result = translate(search_text)
        self.ui.list_widget.clear()
        if isinstance(translation_result, dict):
            for key, value in translation_result.items():
                self.ui.list_widget.addItem(f"{key}: {value}")
        elif isinstance(translation_result, list):
            for line in translation_result:
                self.ui.errorLabel.setText(f'{line}')
        else:
            self.ui.list_widget.addItem(str(translation_result))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
