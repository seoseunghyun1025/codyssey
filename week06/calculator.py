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
        # 창 설정
        self.setWindowTitle('iPhone Style Calculator')
        self.setGeometry(300, 300, 400, 500)

        # 전체 배경을 검은색으로 설정
        self.setStyleSheet('background-color: black;')

        # 레이아웃 설정
        grid = QGridLayout()
        self.setLayout(grid)

        # 디스플레이 (출력 화면)
        self.result = QLineEdit(self)
        self.result.setReadOnly(True)  # 읽기 전용
        self.result.setAlignment(Qt.AlignRight)  # 오른쪽 정렬
        self.result.setStyleSheet(
            'font-size: 32px; background-color: black; color: white; border: none;'
        )
        grid.addWidget(self.result, 0, 0, 1, 4)

        # 계산기 버튼들
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

        # 버튼 배치
        for label, row, col, *span in buttons:
            button = QPushButton(label, self)
            button.setStyleSheet(
                'font-size: 24px; border-radius: 40px; background-color: #333333; color: white; width: 80px; height: 80px;'
            )
            if span:
                grid.addWidget(button, row, col, *span)
            else:
                grid.addWidget(button, row, col)

        # 버튼 색상 조정 (AC, ±, %, ÷, × 등)
        self.set_button_styles()

        self.show()

    def set_button_styles(self):
        # 특수 버튼 색상 설정 (주황색으로 변경)
        special_buttons = ['AC', '±', '%', '÷', '×', '-', '+']
        for button in self.findChildren(QPushButton):
            if (
                button.text() == 'AC'
                or button.text() == '±'
                or button.text() == '%'
            ):
                button.setStyleSheet(
                    'font-size: 24px; border-radius: 40px; background-color: #808080; color: white; width: 80px; height: 80px;'
                )  # 회색
            elif button.text() in ['÷', '×', '-', '+']:
                button.setStyleSheet(
                    'font-size: 24px; border-radius: 40px; background-color: #FF9500; color: white; width: 80px; height: 80px;'
                )  # 주황색
            elif button.text() == '=':
                button.setStyleSheet(
                    'font-size: 24px; border-radius: 40px; background-color: #FF9500; color: white; width: 80px; height: 80px;'
                )  # 오렌지색
            else:
                button.setStyleSheet(
                    'font-size: 24px; border-radius: 40px; background-color: #333333; color: white; width: 80px; height: 80px;'
                )


if __name__ == '__main__':
    app = QApplication([])
    calc = Calculator()
    app.exec_()
