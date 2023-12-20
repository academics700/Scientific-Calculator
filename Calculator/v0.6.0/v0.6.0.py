# -*- coding: utf-8 -*-

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
                             QDesktopWidget, QGridLayout, QHBoxLayout, QAction,
                             qApp)
from PyQt5.QtGui import QIcon, QFont
from PyQt5 import QtGui

#creating widget subclass
class __widget__(QWidget):
    
    #initializing widget object
    def __init__(self):
        super().__init__()
        
        self.__init__widget()
    
    #defining ui elements
    def __init__widget(self):
        
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
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(self.label, 0, 0, 1, 4)
        
        #button text
        button_txt = ['1', '2', '3', '4',
                      '5', '6', '7', '8',
                      '9', '0', '=', '+',
                      '-', '*', '/', '.',
                      'Clear', 'Del']
        
        #grid position
        pos = [(6, 0), (6, 1), (6, 2), (5, 0),
               (5, 1), (5, 2), (4, 0), (4, 1),
               (4, 2), (7, 0), (7, 3), (6, 3),
               (5, 3), (4, 3), (7, 2), (7, 1),
               (3, 0, 1, 2), (3, 2, 1, 2)]
        
        #action
        action = [self.action1, self.action2, self.action3, self.action4,
                  self.action5, self.action6, self.action7, self.action8,
                  self.action9, self.action0, self.action_equal, self.action_plus,
                  self.action_minus, self.action_mul, self.action_div, self.action_point,
                  self.action_clear, self.action_del]
        
        tooltip_txt = ['', '', '', '', '', '', '', '', '', '', 'Answer', 'Addition',
                       'Subtraction', 'Multiplication', 'Division', 'Decimal Point',
                       'Clear Screen', 'Delete']
        
        #setting buttons and actions
        for i in range(len(button_txt)):
            
            txt = button_txt[i]
            btn = QPushButton(txt, self)
            btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            btn.clicked.connect(action[i])
            btn.setFont(QFont('',btn.rect().width() // 7))
            
            if tooltip_txt[i] != '':
                btn.setToolTip(tooltip_txt[i])
            
            #setting colour effect to = button
            if button_txt[i] == '=':
                c_effect = QGraphicsColorizeEffect()
                c_effect.setColor(Qt.blue)
                btn.setGraphicsEffect(c_effect)
            
            if len(pos[i]) == 2:
                x, y = pos[i]
                grid.addWidget(btn, x, y)
                
            else:
                x, y, rowspan, colspan = pos[i]
                grid.addWidget(btn, x, y, rowspan, colspan)
            
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
        
class __main__window__(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        #setting default window geometry
        self.setGeometry(100,100,360,400)
        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('Calculator.ico'))
        self.statusBar().showMessage('v 0.5.0')
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        e_act = self.exit_act()
        fileMenu.addAction(e_act)
        widget = __widget__()
        self.setCentralWidget(widget)
        self.hbox = QHBoxLayout()
        self.centralWidget().setLayout(self.hbox)
        self.show()
        
    def exit_act(self):
        exitAct = QAction(QIcon('quit.png'), 'Exit', self)
        exitAct.setShortcut('Alt+F4')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)
        return exitAct

#defining main function to run application        
def main():
    app = QApplication(sys.argv)
    win = __main__window__()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()