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
        self.current_value = ''
        self.pending_operator = ''
        self.last_operand = ''

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
        for button in self.findChildren(QPushButton):
            text = button.text()
            if text in ['AC', '±', '%']:
                button.setStyleSheet(
                    'font-size: 24px; border-radius: 40px; background-color: #808080; color: white; width: 80px; height: 80px;'
                )
            elif text in ['÷', '×', '-', '+', '=']:
                button.setStyleSheet(
                    'font-size: 24px; border-radius: 40px; background-color: #FF9500; color: white; width: 80px; height: 80px;'
                )

    def on_click(self):
        sender = self.sender()
        button_text = sender.text()
        current_text = self.result.text().replace(',', '')

        if button_text == 'AC':
            self.reset()
        elif button_text == '±':
            self.negative_positive()
        elif button_text == '%':
            self.percent()
        elif button_text in ['+', '-', '×', '÷']:
            self.current_value = current_text
            self.pending_operator = button_text
            self.result.clear()
        elif button_text == '=':
            self.last_operand = current_text
            result = self.equal()
            self.result.setText(result)
        else:
            # 숫자 및 소수점 입력 처리
            if button_text == '.':
                if '.' in current_text:
                    return
                elif current_text == '':
                    self.result.setText('0.')
                    return

            new_text = current_text + button_text
            self.result.setText(new_text)

    def reset(self):
        self.result.clear()
        self.current_value = ''
        self.pending_operator = ''
        self.last_operand = ''

    def negative_positive(self):
        current_text = self.result.text().replace(',', '')
        if not current_text:
            return
        if current_text.startswith('-'):
            self.result.setText(current_text[1:])
        else:
            self.result.setText('-' + current_text)

    def percent(self):
        current_text = self.result.text().replace(',', '')
        try:
            value = float(current_text)
            percent_value = value / 100
            self.result.setText(str(percent_value))
        except ValueError:
            pass

    def add(self, a, b):
        return str(float(a) + float(b))

    def subtract(self, a, b):
        return str(float(a) - float(b))

    def multiply(self, a, b):
        return str(float(a) * float(b))

    def divide(self, a, b):
        if float(b) == 0:
            return 'Error'
        return str(float(a) / float(b))

    def equal(self):
        if not self.current_value or not self.result.text():
            return self.result.text()

        a = self.current_value
        b = self.result.text().replace(',', '')
        op = self.pending_operator

        try:
            if op == '+':
                result = self.add(a, b)
            elif op == '-':
                result = self.subtract(a, b)
            elif op == '×':
                result = self.multiply(a, b)
            elif op == '÷':
                result = self.divide(a, b)
            else:
                return self.result.text()
        except Exception:
            return 'Error'

        # 소수점 6자리 이내로 반올림
        try:
            result_float = float(result)
            if result_float.is_integer():
                result = str(int(result_float))
            else:
                result = str(round(result_float, 6))
        except:
            pass

        self.current_value = ''
        self.pending_operator = ''
        self.last_operand = ''
        return result


if __name__ == '__main__':
    app = QApplication([])
    calc = Calculator()
    app.exec_()
