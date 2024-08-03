from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


def win():
    victory_win = QMessageBox()
    victory_win.setText('Правильно')
    victory_win.exec_()

app = QApplication([])
main_win = QWidget()
main_win.resize(400,200)

btn1 = QPushButton("2005")
btn2 = QPushButton("2007")
btn3 = QPushButton("2015")
btn4 = QPushButton("2009")

question = QLabel('В якому році канал отримав" золоту кнопку "від YouTube')

layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()

layoutH1.addWidget(question,alignment = Qt.AlignCenter)
layoutH2.addWidget(btn1, alignment = Qt.AlignCenter)
layoutH2.addWidget(btn2, alignment = Qt.AlignCenter)
layoutH3.addWidget(btn3, alignment = Qt.AlignCenter)
layoutH3.addWidget(btn4, alignment = Qt.AlignCenter)

vertical1 = QVBoxLayout()

vertical1.addLayout(layoutH1)
vertical1.addLayout(layoutH2)
vertical1.addLayout(layoutH3)
main_win.setLayout(vertical1)

btn1.clicked.connect(win)

main_win.show()
app.exec_()