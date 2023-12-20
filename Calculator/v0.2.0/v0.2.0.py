'''
Author: @Anish Sarkar

Created: @05-20-2022
        22:09

Calculator v0.1.0
'''

#importing modules
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QLabel,
                             QPushButton, QGraphicsColorizeEffect, QSizePolicy, 
                             QDesktopWidget, QGridLayout)
from PyQt5.QtGui import QIcon, QFont

#creating widget subclass
class __widget__(QWidget):
    
    #initializing widget object
    def __init__(self):
        super().__init__()
        
        self.__init__widget()
        self.show()
    
    #defining ui elements
    def __init__widget(self):
        
        #setting default window geometry
        self.setGeometry(100,100,360,350)
        self.setWindowTitle('Calculator') 
        
        #setting grid layout
        grid = QGridLayout()
        grid.setSpacing(10)
        self.setLayout(grid)


        
        #setting label to display result
        self.label = QLabel(self)
        self.label.setWordWrap(True)
        self.label.setStyleSheet("QLabel"
								"{"
								"border : 4px solid black;"
								"background : white;"
								"}")
        self.label.setAlignment(Qt.AlignRight)
        self.label.setFont(QFont('Arial', 15))
        
        #setting buttons
        btn1 = QPushButton("1", self)
        btn2 = QPushButton("2", self)
        btn3 = QPushButton("3", self)
        btn4 = QPushButton("4", self)
        btn5 = QPushButton("5", self)
        btn6 = QPushButton("6", self)
        btn7 = QPushButton("7", self)
        btn8 = QPushButton("8", self)
        btn9 = QPushButton("9", self)
        btn0 = QPushButton("0", self)
        btn_equal = QPushButton("=", self)
        btn_plus = QPushButton("+", self)
        btn_minus = QPushButton("-", self)
        btn_mul = QPushButton("*", self)
        btn_div = QPushButton("/", self)
        btn_point = QPushButton(".", self)
        btn_clear = QPushButton("Clear", self)
        btn_del = QPushButton("Del", self)
        
        #setting button resize
        btn1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btn2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btn3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btn4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btn5.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btn6.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btn7.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btn8.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btn9.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btn0.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btn_equal.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btn_plus.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btn_minus.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btn_mul.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btn_div.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btn_point.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btn_clear.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btn_del.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        #aligning buttons to grid
        grid.addWidget(self.label, 0, 0, 1, 4)
        grid.addWidget(btn1, 4, 0)
        grid.addWidget(btn2, 4, 1)
        grid.addWidget(btn3, 4, 2)
        grid.addWidget(btn4, 5, 0)
        grid.addWidget(btn5, 5, 1)
        grid.addWidget(btn6, 5, 2)
        grid.addWidget(btn7, 6, 0)
        grid.addWidget(btn8, 6, 1)
        grid.addWidget(btn9, 6, 2)
        grid.addWidget(btn0, 7, 0)
        grid.addWidget(btn_equal, 7, 3)
        grid.addWidget(btn_plus, 6, 3)
        grid.addWidget(btn_minus, 5, 3)
        grid.addWidget(btn_mul, 4, 3)
        grid.addWidget(btn_div, 7, 2)
        grid.addWidget(btn_point, 7, 1)
        grid.addWidget(btn_del, 3, 2, 1, 2)
        grid.addWidget(btn_clear, 3, 0, 1, 2)
        
        #adding colour effect to = button
        c_effect = QGraphicsColorizeEffect()
        c_effect.setColor(Qt.blue)
        btn_equal.setGraphicsEffect(c_effect)

        #setting button actions
        btn_minus.clicked.connect(self.action_minus)
        btn_equal.clicked.connect(self.action_equal)
        btn0.clicked.connect(self.action0)
        btn1.clicked.connect(self.action1)
        btn2.clicked.connect(self.action2)
        btn3.clicked.connect(self.action3)
        btn4.clicked.connect(self.action4)
        btn5.clicked.connect(self.action5)
        btn6.clicked.connect(self.action6)
        btn7.clicked.connect(self.action7)
        btn8.clicked.connect(self.action8)
        btn9.clicked.connect(self.action9)
        btn_div.clicked.connect(self.action_div)
        btn_mul.clicked.connect(self.action_mul)
        btn_plus.clicked.connect(self.action_plus)
        btn_point.clicked.connect(self.action_point)
        btn_clear.clicked.connect(self.action_clear)
        btn_del.clicked.connect(self.action_del)

    #defining button actions
    def action_equal(self):

        equation = self.label.text()

        try:
            ans = eval(equation)

            self.label.setText(str(ans))

        except:
            self.label.setText("Wrong Input")

    def action_plus(self):
        text = self.label.text()
        self.label.setText(text + " + ")

    def action_minus(self):
        text = self.label.text()
        self.label.setText(text + " - ")

    def action_div(self):
        text = self.label.text()
        self.label.setText(text + " / ")

    def action_mul(self):
        text = self.label.text()
        self.label.setText(text + " * ")

    def action_point(self):
        text = self.label.text()
        self.label.setText(text + ".")

    def action0(self):
        text = self.label.text()
        self.label.setText(text + "0")

    def action1(self):
        text = self.label.text()
        self.label.setText(text + "1")

    def action2(self):
        text = self.label.text()
        self.label.setText(text + "2")

    def action3(self):
        text = self.label.text()
        self.label.setText(text + "3")

    def action4(self):
        text = self.label.text()
        self.label.setText(text + "4")

    def action5(self):
        text = self.label.text()
        self.label.setText(text + "5")

    def action6(self):
        text = self.label.text()
        self.label.setText(text + "6")

    def action7(self):
        text = self.label.text()
        self.label.setText(text + "7")

    def action8(self):
        text = self.label.text()
        self.label.setText(text + "8")

    def action9(self):
        text = self.label.text()
        self.label.setText(text + "9")

    def action_clear(self):
        self.label.setText("")

    def action_del(self):
        text = self.label.text()
        self.label.setText(text[:len(text)-1])

#defining main function to run application        
def main():
    app = QApplication(sys.argv)
    #win = __main__window__()
    win = __widget__()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()