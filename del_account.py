import sqlite3
import sys

from PyQt5.QtWidgets import QPushButton, QApplication, QLabel, QWidget


class Delete(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(310, 345, 480, 110)
        self.setWindowTitle('Удаление аккаунта')

        self.warning_txt = QLabel(self)
        self.warning_txt.resize(3000, 20)
        self.warning_txt.move(10, 10)
        self.warning_txt.setText('Вы точно хотите удалить аккаунт?')

        self.notice_txt = QLabel(self)
        self.notice_txt.resize(3000, 20)
        self.notice_txt.move(10, 40)
        self.notice_txt.setText('При удалении аккаунта вы потеряете все свои данные и их нельзя будет восстановить!')

        self.delete_btn = QPushButton('Удалить', self)
        self.delete_btn.resize(60, 30)
        self.delete_btn.move(340, 70)
        self.delete_btn.clicked.connect(self.delete)

        self.delete_btn = QPushButton('Отмена', self)
        self.delete_btn.resize(50, 30)
        self.delete_btn.move(420, 70)
        self.delete_btn.clicked.connect(self.cancellation)

    def delete(self):
        con = sqlite3.connect("users.sql")
        cur = con.cursor()
        self.username = ''
        name = cur.execute("""SELECT user FROM information WHERE choice = ''""")
        for i in name:
            self.username += i[0]

        cur.execute("""DELETE FROM information WHERE user = ?""", (self.username,))
        cur.execute("""DELETE FROM users_data WHERE name = ?""", (self.username,))

        con.commit()
        con.close()
        self.close()

    def cancellation(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Delete()
    ex.show()
    sys.exit(app.exec())