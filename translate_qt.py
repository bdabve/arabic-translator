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
import qtawesome as qta
from h_interface import Ui_MainWindow
from translator import Translator


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load the .ui file
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("AI Translator")

        # Connect the button click event
        self.ui.search_button.setIcon(qta.icon('fa.send', color='#ffffff'))
        self.ui.search_button.clicked.connect(self.translate)

        # Set dark style sheet
        with open('./style.qss', 'r') as f:
            style_sheet = f.read()
        self.setStyleSheet(style_sheet)

    def translate(self):
        search_text = self.ui.input_field.toPlainText()
        translate_to = self.ui.comboBoxTranslateTo.currentText()
        translator = Translator(translate_to)
        translation_result = translator.translate(search_text)
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
