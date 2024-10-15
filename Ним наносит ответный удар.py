import random
from PyQt6.QtWidgets import (QWidget, QPushButton, QLabel, QLCDNumber,
                             QVBoxLayout, QHBoxLayout)


class NimStrikesBack(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Ним наносит ответный удар')

        self.X = random.randint(20, 30)
        self.Y = random.randint(1, 10)
        self.Z = random.randint(1, 10)  # Сделаем Z положительным

        self.main_layout = QVBoxLayout()
        self.yz_layout = QHBoxLayout()
        self.motions_left_layout = QHBoxLayout()
        self.x_layout = QHBoxLayout()

        self.result_label = QLabel()

        self.btnp = QPushButton('+' + str(self.Y))
        self.btnp.clicked.connect(self.action_y)
        self.btnm = QPushButton('-' + str(self.Z))  # Изменяем текст на '-' перед Z
        self.btnm.clicked.connect(self.action_z)
        self.yz_layout.addWidget(self.btnp)
        self.yz_layout.addWidget(self.btnm)

        self.motions_left = QLabel('Осталось ходов')
        self.motions_left_cnt = QLCDNumber()
        self.motions_left_cnt.display(10)
        self.motions_left_layout.addWidget(self.motions_left)
        self.motions_left_layout.addWidget(self.motions_left_cnt)

        self.num_now = QLabel('Текущее число')
        self.x_ = QLCDNumber()
        self.x_.display(self.X)
        self.x_layout.addWidget(self.num_now)
        self.x_layout.addWidget(self.x_)

        self.main_layout.addWidget(self.result_label)
        self.main_layout.addLayout(self.yz_layout)
        self.main_layout.addLayout(self.motions_left_layout)
        self.main_layout.addLayout(self.x_layout)

        self.setLayout(self.main_layout)

    def action_y(self):
        if self.result_label.text():
            self.result_label.setText('')

        self.X += self.Y
        self.x_.display(self.X)
        self.motions_left_cnt.display(self.motions_left_cnt.value() - 1)

        if self.X == 0 or self.motions_left_cnt.value() == 0:
            self.restart_game()

    def action_z(self):
        if self.result_label.text():
            self.result_label.setText('')

        self.X -= self.Z  # Уменьшаем X на Z
        self.x_.display(self.X)
        self.motions_left_cnt.display(self.motions_left_cnt.value() - 1)

        if self.X == 0 or self.motions_left_cnt.value() == 0:
            self.restart_game()

    def restart_game(self):
        if self.X > 0:
            self.result_label.setText('Вы проиграли, начинаем новую игру')
        else:
            self.result_label.setText('Вы победили, начинаем новую игру')

        self.X = random.randint(20, 30)
        self.Y = random.randint(1, 10)
        self.Z = random.randint(1, 10)  # Снова делаем Z положительным

        self.btnp.setText('+' + str(self.Y))
        self.btnm.setText('-' + str(self.Z))  # Обновляем текст на '-' перед Z
        self.motions_left_cnt.display(10)
        self.x_.display(self.X)


# Запуск приложения
if __name__ == '__main__':
    from PyQt6.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    window = NimStrikesBack()
    window.show()
    sys.exit(app.exec())

