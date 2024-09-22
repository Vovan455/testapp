from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, 
                                QRadioButton)
app = QApplication([])
win = QWidget()

win.setWindowTitle("число")
win.resize(400,200)

question = QLabel("Як звуть третього призедента Укр")
answer_1 = QRadioButton("Кравчук")
answer_2 = QRadioButton("Кучма")
answer_3 = QRadioButton("Ющенко")
answer_4 = QRadioButton("Грушевський")

main_layout = QVBoxLayout()

main_layout.addWidget(question)

h_line_1 = QHBoxLayout()
h_line_1.addWidget(answer_1)
h_line_1.addWidget(answer_2)

main_layout.addLayout(h_line_1)

h_line_2 = QHBoxLayout()
h_line_2.addWidget(answer_3)
h_line_2.addWidget(answer_4)
main_layout.addLayout(h_line_2)

def show_winner():
    message_box = QMessageBox()
    message_box.setText("правельно")
    message_box.exec()

def show_lose():
    message_box = QMessageBox()
    message_box.setText("не правельно")
    message_box.exec()
    
answer_1.clicked.connect(show_lose)
answer_2.clicked.connect(show_lose)
answer_3.clicked.connect(show_winner)
answer_4.clicked.connect(show_lose)    


win.setLayout(main_layout)
win.show()
app.exec()
