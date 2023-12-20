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
                             QPushButton, QGraphicsColorizeEffect)
from PyQt5.QtGui import QIcon, QFont

#creating main window subclass
class __main__window__(QMainWindow):
    
    #initializing the object
    def __init__(self):
        super().__init__()
        
        self.initialize_UI()
        self.show()
    
    #defining components
    def initialize_UI(self):
        
        #setting window properties
        self.setGeometry(100,100,360,350)
        self.setWindowTitle('Calculator')
        
        #setting label to display result
        self.label = QLabel(self)
        self.label.setGeometry(5, 5, 350, 70)
        self.label.setWordWrap(True)
        self.label.setStyleSheet("QLabel" #setting label style
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
        btn6 = QPushButton("5", self)
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
        
        #setting button position and dimensions
        btn1.setGeometry(5, 150, 80, 40)
        btn2.setGeometry(95, 150, 80, 40)
        btn3.setGeometry(185, 150, 80, 40)
        btn4.setGeometry(5, 200, 80, 40)
        btn5.setGeometry(95, 200, 80, 40)
        btn6.setGeometry(185, 200, 80, 40)
        btn7.setGeometry(5, 250, 80, 40)
        btn8.setGeometry(95, 250, 80, 40)
        btn9.setGeometry(185, 250, 80, 40)
        btn0.setGeometry(5, 300, 80, 40)
        btn_equal.setGeometry(275, 300, 80, 40)
        btn_plus.setGeometry(275, 250, 80, 40)
        btn_minus.setGeometry(275, 200, 80, 40)
        btn_mul.setGeometry(275, 150, 80, 40)
        btn_div.setGeometry(185, 300, 80, 40)
        btn_point.setGeometry(95, 300, 80, 40)
        btn_clear.setGeometry(5, 100, 200, 40)
        btn_del.setGeometry(210, 100, 145, 40)
        
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
    win = __main__window__()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()