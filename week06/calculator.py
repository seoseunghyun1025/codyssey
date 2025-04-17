from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QGridLayout,
    QPushButton,
    QLineEdit,
)
from PyQt5.QtCore import Qt


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('iPhone Style Calculator')
        self.setGeometry(300, 300, 400, 500)

        self.setStyleSheet('background-color: black;')

        grid = QGridLayout()
        self.setLayout(grid)

        self.result = QLineEdit(self)
        self.result.setReadOnly(True)
        self.result.setAlignment(Qt.AlignRight)
        self.result.setStyleSheet(
            'font-size: 32px; background-color: black; color: white; border: none;'
        )
        grid.addWidget(self.result, 0, 0, 1, 4)

        buttons = [
            ('AC', 1, 0),
            ('±', 1, 1),
            ('%', 1, 2),
            ('÷', 1, 3),
            ('7', 2, 0),
            ('8', 2, 1),
            ('9', 2, 2),
            ('×', 2, 3),
            ('4', 3, 0),
            ('5', 3, 1),
            ('6', 3, 2),
            ('-', 3, 3),
            ('1', 4, 0),
            ('2', 4, 1),
            ('3', 4, 2),
            ('+', 4, 3),
            ('0', 5, 0, 1, 2),
            ('.', 5, 2),
            ('=', 5, 3),
        ]

        for label, row, col, *span in buttons:
            button = QPushButton(label, self)
            button.setStyleSheet(
                'font-size: 24px; border-radius: 40px; background-color: #333333; color: white; width: 80px; height: 80px;'
            )
            button.clicked.connect(self.on_click)
            if span:
                grid.addWidget(button, row, col, *span)
            else:
                grid.addWidget(button, row, col)

        self.set_button_styles()

        self.show()

    def set_button_styles(self):
        special_buttons = ['AC', '±', '%', '÷', '×', '-', '+']
        for button in self.findChildren(QPushButton):
            if (
                button.text() == 'AC'
                or button.text() == '±'
                or button.text() == '%'
            ):
                button.setStyleSheet(
                    'font-size: 24px; border-radius: 40px; background-color: #808080; color: white; width: 80px; height: 80px;'
                )
            elif button.text() in ['÷', '×', '-', '+']:
                button.setStyleSheet(
                    'font-size: 24px; border-radius: 40px; background-color: #FF9500; color: white; width: 80px; height: 80px;'
                )
            elif button.text() == '=':
                button.setStyleSheet(
                    'font-size: 24px; border-radius: 40px; background-color: #FF9500; color: white; width: 80px; height: 80px;'
                )
            else:
                button.setStyleSheet(
                    'font-size: 24px; border-radius: 40px; background-color: #333333; color: white; width: 80px; height: 80px;'
                )

    def on_click(self):
        sender = self.sender()
        button_text = sender.text()

        if button_text == 'AC':
            self.result.clear()
        else:
            current_text = self.result.text()

            if button_text not in '0123456789':
                self.result.setText(current_text + button_text)
            else:
                current_text += button_text
                try:
                    formatted_text = "{:,}".format(
                        int(current_text.replace(',', ''))
                    )
                    self.result.setText(formatted_text)
                except ValueError:
                    self.result.setText(current_text)


if __name__ == '__main__':
    app = QApplication([])
    calc = Calculator()
    app.exec_()
