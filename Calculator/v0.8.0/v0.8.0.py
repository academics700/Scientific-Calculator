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
                             qApp, QMenu)
from PyQt5.QtGui import QIcon, QFont
from PyQt5 import QtGui

#creating widget subclass
class __widget__(QWidget):
    
    #initializing widget object
    def __init__(self, index):
        super().__init__()
        
        self.__init__widget(index)
    
    #defining ui elements
    def __init__widget(self, index):
        
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
        
        font = ['Aller', 'Times New Roman', 'Calibri', 'Arial',
                'Adam Warren pro']
        
        #setting buttons and actions
        for i in range(len(button_txt)):
            
            txt = button_txt[i]
            btn = QPushButton(txt, self)
            btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            btn.clicked.connect(action[i])
            btn.setFont(QFont(font[index],btn.rect().width() // 7))
            
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
        index = 0
        self.setGeometry(100,100,360,400)
        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('Calculator.ico'))
        self.statusbar = self.statusBar()
        self.statusBar().showMessage('v 0.8.0')
        self.center()
        self.menu_bar()
        self.call_widget(index)
        self.show()
        
    def call_widget(self, index):
        widget = __widget__(index)
        self.setCentralWidget(widget)
        self.hbox = QHBoxLayout()
        self.centralWidget().setLayout(self.hbox)
        
    def menu_bar(self):
        menubar = self.menuBar()
        self.file_menu(menubar)
        self.view_menu(menubar)
        
        
    def file_menu(self, menubar):
        fileMenu = menubar.addMenu('&File')
        quit_act = self.exit_act()
        fileMenu.addAction(quit_act)
        
    def view_menu(self, menubar):
        viewMenu = menubar.addMenu('&View')
        self.view_stat_act(viewMenu)
        self.view_button_menu(viewMenu)
    
    def view_button_menu(self, viewMenu):
        button_menu = QMenu('Buttons', self)
        font_menu = QMenu('Font', self)
        button_menu.addMenu(font_menu)

        font_fcn = [self.__aller__(), self.__timesNewRoman__(),
                    self.__calibri__(), self.__arial__(),
                    self.__adamWarrenPro__()]
        
        for i in range(len(font_fcn)):
            font = font_fcn[i]
            font_menu.addAction(font)

        viewMenu.addMenu(button_menu)
        
    def view_stat_act(self, viewMenu):
        viewStatAct = QAction('Statusbar', self, checkable=True)
        viewStatAct.setStatusTip('View Statusbar')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggle_statusbar_Menu)
        viewMenu.addAction(viewStatAct)
        
    def toggle_statusbar_Menu(self, state):

        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()
            
    def __aller__(self):
        Aller = QAction('Aller', self)
        Aller.triggered.connect(self.aller_font)
        return Aller
    
    def __timesNewRoman__(self):
        Times_New_Roman = QAction('Times New Roman', self)
        Times_New_Roman.triggered.connect(self.times_new_roman_font)
        return Times_New_Roman
    
    def __calibri__(self):
        Calibri = QAction('Calibri', self)
        Calibri.triggered.connect(self.calibri_font)
        return Calibri
    
    def __arial__(self):
        Calibri = QAction('Arial', self)
        Calibri.triggered.connect(self.arial_font)
        return Calibri
    
    def __adamWarrenPro__(self):
        Calibri = QAction('Adam Warren Pro', self)
        Calibri.triggered.connect(self.adam_warren_pro_font)
        return Calibri
            
    def aller_font(self):
        index = 0
        self.call_widget(index)
        
    def times_new_roman_font(self):
        index = 1
        self.call_widget(index)
        
    def calibri_font(self):
        index = 2
        self.call_widget(index)
        
    def arial_font(self):
        index = 3
        self.call_widget(index)
        
    def adam_warren_pro_font(self):
        index = 4
        self.call_widget(index)
        
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def exit_act(self):
        exitAct = QAction(QIcon('quit.png'), 'Exit', self)
        exitAct.setShortcut('Alt+F4')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)
        
        return exitAct
    
    def contextMenuEvent(self, event):
        cmenu = QMenu(self)
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAct:
            qApp.quit()

#defining main function to run application        
def main():
    app = QApplication(sys.argv)
    win = __main__window__()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()