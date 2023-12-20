# -*- coding: utf-8 -*-

'''
Author: @Anish Sarkar

Created: @05-20-2022
        22:09

Calculator v0.9.0
''' 

#importing modules
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QLabel,
                             QPushButton, QGraphicsColorizeEffect, QSizePolicy, 
                             QDesktopWidget, QGridLayout, QHBoxLayout, QAction,
                             qApp, QMenu, QShortcut)
from PyQt5.QtGui import QIcon, QFont, QKeySequence
from PyQt5 import QtGui

eval_txt=''
sqrt_button=''
Ans=0
sqrt_counter = 0

#creating widget subclass
class __widget__(QWidget):
    
    #initializing widget object
    def __init__(self, index):
        super().__init__()
        
        self.__init__widget(index)
    
    #defining ui elements
    def __init__widget(self, index):
        
        global sqrt_button
        
        #setting grid layout
        grid = QGridLayout()
        grid.setSpacing(1)
        self.setLayout(grid)
        
        #setting label to display result
        self.label = QLabel(self)
        self.label.setWordWrap(True)
        self.label.setStyleSheet("QLabel"
								"{"
								"border : 4px solid black;"
                                "border-radius: 10px;"
								"background : white;"
								"}")
        self.label.setAlignment(Qt.AlignRight)
        self.label.setFont(QFont('Arial', 15))
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        grid.addWidget(self.label, 0, 0, 1, 30)
        
        #button text
        button_txt = ['1', '2', '3', '4',
                      '5', '6', '7', '8',
                      '9', '0', '=', '+',
                      '-', '*', '/', '.',
                      'C', 'Del', 'a\u00b2', 'a\u02e3',
                      '\u221ax', '(-)', 'e', '(',
                      ')', 'Ans']
        
        #grid position
        pos = [(6, 0, 1, 6), (6, 6, 1, 6), (6, 12, 1, 6), (5, 0, 1, 6),
               (5, 6, 1, 6), (5, 12, 1, 6), (4, 0, 1, 6), (4, 6, 1, 6),
               (4, 12, 1, 6), (7, 0, 1, 6), (7, 24, 1, 6), (6, 18, 1, 6),
               (6, 24, 1, 6), (5, 18, 1, 6), (5, 24, 1, 6), (7, 6, 1, 6),
               (4, 24, 1, 6), (4, 18, 1, 6), (3, 0, 1, 5), (3, 5, 1, 5),
               (3, 10, 1, 5), (3, 15, 1, 5), (7, 12, 1, 6), (3, 20, 1, 5),
               (3, 25, 1, 5), (7, 18, 1, 6)]
        
        #action
        action = [self.action1, self.action2, self.action3, self.action4,
                  self.action5, self.action6, self.action7, self.action8,
                  self.action9, self.action0, self.action_equal, self.action_plus,
                  self.action_minus, self.action_mul, self.action_div, self.action_point,
                  self.action_clear, self.action_del, self.action_square,
                  self.action_power, self.action_sqrt, self.action_neg,
                  self.action_e, self.action_leftbrac, self.action_rightbrac,
                  self.actin_ans]
        
        tooltip_txt = ['', '', '', '', '', '', '', '', '', '', 'Answer', 'Addition',
                       'Subtraction', 'Multiplication', 'Division', 'Decimal Point',
                       'Clear Screen', 'Delete', 'a<sup>2</sup>', 'a^x',
                       'sqrt(x)', '(-)', 'e', '(',
                       ')', 'Ans']
        
        font = ['Aller', 'Times New Roman', 'Calibri', 'Arial',
                'Adam Warren pro']
        
        row_stretch = [(7, 2), (6, 2), (5, 2),
                       (4, 2), (3, 1), (0, 2)]
        
        for row, stretch in row_stretch:
            grid.setRowStretch(row, stretch)
        
        #setting buttons and actions
        for i in range(len(button_txt)):
            
            txt = button_txt[i]
            btn = QPushButton(txt, self)    
            btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            btn.clicked.connect(action[i])
            btn.setFont(QFont(font[index],btn.rect().width() // 8))
            btn.setStyleSheet("QPushButton {border: 1px solid #D3D3D3;"
                                          "background: white;"
                                          "border-radius: 8px;}")
            
            x, y, rowspan, colspan = pos[i]
            grid.addWidget(btn, x, y, rowspan, colspan)
            
            if button_txt[i] == '\u221ax':
                sqrt_button = btn
            
            if tooltip_txt[i] != '':
                btn.setToolTip(tooltip_txt[i])
            
            #setting colour effect to = button
            if button_txt[i] == '=':
                btn.setStyleSheet("QPushButton {border: 1px solid #D3D3D3;"
                                  "background: white;"
                                  "color: blue;"
                                  "border-radius: 8px;}")
            else:
                btn.setStyleSheet("QPushButton {border: 1px solid #D3D3D3;"
                                              "background: white;"
                                              "border-radius: 8px;}")

    #defining button actions

    def action_equal(self):
        global eval_txt, Ans
        equation = eval_txt

        try:
            ans = eval(equation)
            Ans = ans
            self.label.setText(str(ans))
            eval_txt = str(ans)

        except:
            self.label.setText("Wrong Input")

    def action_plus(self):
        global eval_txt
        add_txt = '+'
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText(text + " + ")

    def action_minus(self):
        global eval_txt
        add_txt = '-'
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText(text + " - ")

    def action_div(self):
        global eval_txt
        add_txt = '/'
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText(text + " / ")

    def action_mul(self):
        global eval_txt
        add_txt = '*'
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText(text + " * ")

    def action_point(self):
        global eval_txt
        add_txt = '.'
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText(text + ".")

    def action0(self):
        global eval_txt
        add_txt = '0'
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText(text + "0")

    def action1(self):
        global eval_txt, sqrt_counter
        add_txt = '1'
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText(text + "1")

    def action2(self):
        global eval_txt
        add_txt = '2'
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText(text + "2")

    def action3(self):
        global eval_txt
        add_txt = '3'
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText(text + "3")

    def action4(self):
        global eval_txt
        add_txt = '4'
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText(text + "4")

    def action5(self):
        global eval_txt
        add_txt = '5'
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText(text + "5")

    def action6(self):
        global eval_txt
        add_txt = '6'
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText(text + "6")

    def action7(self):
        global eval_txt
        add_txt = '7'
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText(text + "7")

    def action8(self):
        global eval_txt, sqrt_counter
        add_txt = '8'
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText(text + "8")

    def action9(self):
        global eval_txt, sqrt_counter
        add_txt = '9'
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText(text + "9")

    def action_clear(self):
        global eval_txt
        eval_txt=''
        self.label.setText("")

    def action_del(self):
        global eval_txt
        eval_txt=eval_txt[:len(eval_txt)-1]
        text = self.label.text()
        self.label.setText(text[:len(text)-1])
        
    def action_square(self):
        global eval_txt
        add_txt = '**(2)'
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText(text + "^2")
        
    def action_power(self):
        global eval_txt
        add_txt = '**'
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText(text + "^")
        
    def action_sqrt(self):
        global eval_txt, sqrt_counter, sqrt_button
        add_txt1 = '('
        add_txt2 = ')**(0.5)'
        sqrt_counter+=1
        text = self.label.text()
        if sqrt_counter == 1:
            self.label.setText(text + "\u221a")
            sqrt_button.setStyleSheet('QPushButton {color: red;}')
            eval_txt+=add_txt1
        if sqrt_counter == 2:
            sqrt_counter = 0
            sqrt_button.setStyleSheet('QPushButton {color: black;}')
            eval_txt+=add_txt2
            self.label.setText(text)
        
    def action_neg(self):
        add_txt = '*(-1)'
        global eval_txt
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText("-" + text)
        
    def action_e(self):
        global eval_txt
        add_txt = '2.718281828459045'
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText(text + "e")
        
    def action_leftbrac(self):
        global eval_txt
        add_txt = '('
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText(text + "(")
        
    def action_rightbrac(self):
        global eval_txt
        add_txt = ')'
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText(text + ")")
        
    def actin_ans(self):
        global eval_txt, Ans
        add_txt = str(Ans)
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText(text + "Ans")
        

        
class __main__window__(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        #setting default window geometry
        index = 0
        self.setGeometry(100, 100, 100, 500)
        self.setMinimumSize(400, 400)
        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('Calculator.ico'))
        self.statusbar = self.statusBar()
        self.statusBar().showMessage('v 0.9.0')
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