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
                             qApp, QMenu, QShortcut, QFrame, QComboBox, QGroupBox,
                             QRadioButton)
from PyQt5.QtGui import QIcon, QFont, QKeySequence
from PyQt5 import QtGui
from math import (sin, sqrt, cos, tan, asin, acos, atan, pi, factorial, log10,
                  log, comb, perm, ceil, floor, gamma, fabs)

'''action = [self.action_pi, self.action_fac, self.action_inv,
          self.action_log, self.action_ln, self.action_nCr,
          self.action_nPr, self.action_x_root, self.action_ceil,
          self.action_floor, self.action_gamma, self.action_mod]'''

eval_txt = ''
Ans = 0
sqrt_counter = 0
neg_count = 0
font_index = 0
theme_index = 0
groupbox_index = 0
groupbox = ''
_quit = 0

#creating widget subclass
class __widget__(QWidget):
    
    #initializing widget object
    def __init__(self):
        super().__init__()
        
        self.__init__widget()
    
    #defining ui elements
    def __init__widget(self):
        
        global sqrt_button, font_index, theme_index
        
        #setting grid layout
        grid = QGridLayout()
        grid.setSpacing(3)
        self.setLayout(grid)
        
        #setting label to display result
        self.label = QLabel(self)
        self.label.setWordWrap(True)
        self.label.setAlignment(Qt.AlignRight)
        self.label.setFont(QFont('Arial', 15))
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label.setText('\n')
        grid.addWidget(self.label, 0, 0, 1, 30)
        
        self.shortcut1 = QShortcut(QKeySequence('1'), self)
        self.shortcut2 = QShortcut(QKeySequence('2'), self)
        self.shortcut3 = QShortcut(QKeySequence('3'), self)
        self.shortcut4 = QShortcut(QKeySequence('4'), self)
        self.shortcut5 = QShortcut(QKeySequence('5'), self)
        self.shortcut6 = QShortcut(QKeySequence('6'), self)
        self.shortcut7 = QShortcut(QKeySequence('7'), self)
        self.shortcut8 = QShortcut(QKeySequence('8'), self)
        self.shortcut9 = QShortcut(QKeySequence('9'), self)
        self.shortcut0 = QShortcut(QKeySequence('0'), self)
        self.shortcut_plus = QShortcut(QKeySequence('+'), self)
        self.shortcut_minus = QShortcut(QKeySequence('-'), self)
        self.shortcut_mul = QShortcut(QKeySequence('*'), self)
        self.shortcut_div = QShortcut(QKeySequence('/'), self)
        self.shortcut_equal1 = QShortcut(QKeySequence('='), self)
        self.shortcut_equal2 = QShortcut(QKeySequence('Enter'), self)
        self.shortcut_del1 = QShortcut(QKeySequence('Backspace'), self)
        self.shortcut_del2 = QShortcut(QKeySequence('Delete'), self)
        self.shortcut_point = QShortcut(QKeySequence('.'), self)
        self.shortcut_neg = QShortcut(QKeySequence('Shift+-'), self)
        self.shortcut_leftbrac = QShortcut(QKeySequence('('), self)
        self.shortcut_rightbrac = QShortcut(QKeySequence(')'), self)
        self.shortcut_ans = QShortcut(QKeySequence('a'), self)
        self.shortcut_e = QShortcut(QKeySequence('e'), self)
        self.shortcut_clear = QShortcut(QKeySequence('c'), self)
        
        self.shortcut1.activated.connect(self.action1)
        self.shortcut2.activated.connect(self.action2)
        self.shortcut3.activated.connect(self.action3)
        self.shortcut4.activated.connect(self.action4)
        self.shortcut5.activated.connect(self.action5)
        self.shortcut6.activated.connect(self.action6)
        self.shortcut7.activated.connect(self.action7)
        self.shortcut8.activated.connect(self.action8)
        self.shortcut9.activated.connect(self.action9)
        self.shortcut0.activated.connect(self.action0)
        self.shortcut_plus.activated.connect(self.action_plus)
        self.shortcut_minus.activated.connect(self.action_minus)
        self.shortcut_mul.activated.connect(self.action_mul)
        self.shortcut_div.activated.connect(self.action_div)
        self.shortcut_equal1.activated.connect(self.action_equal)
        self.shortcut_equal2.activated.connect(self.action_equal)
        self.shortcut_del1.activated.connect(self.action_del)
        self.shortcut_del2.activated.connect(self.action_del)
        self.shortcut_point.activated.connect(self.action_point)
        self.shortcut_neg.activated.connect(self.action_neg)
        self.shortcut_leftbrac.activated.connect(self.action_leftbrac)
        self.shortcut_rightbrac.activated.connect(self.action_rightbrac)
        self.shortcut_ans.activated.connect(self.action_ans)
        self.shortcut_e.activated.connect(self.action_e)
        self.shortcut_clear.activated.connect(self.action_clear)
        
        #button text
        button_txt = ['1', '2', '3', '4',
                      '5', '6', '7', '8',
                      '9', '0', '=', '+',
                      '-', '\u00d7', '\u00f7', '.',
                      'C', 'Del', 'a\u00b2', 'a\u02e3',
                      '\u221ax', '(-)', 'e', '(',
                      ')', 'Ans', 'TRIGONOMETRY', 'FUNCTIONS', 
                      'MORE']
        
        button_fontSize_index = [1, 1, 1, 1,
                                 1, 1, 1, 1,
                                 1, 1, 2, 2,
                                 2, 2, 2, 1,
                                 2, 2, 3, 3,
                                 3, 3, 1, 3,
                                 3, 2, 4, 4,
                                 4]
        
        #grid position
        pos = [(7, 0, 1, 6), (7, 6, 1, 6), (7, 12, 1, 6), (6, 0, 1, 6),
               (6, 6, 1, 6), (6, 12, 1, 6), (5, 0, 1, 6), (5, 6, 1, 6),
               (5, 12, 1, 6), (8, 6, 1, 6), (8, 24, 1, 6), (7, 18, 1, 6),
               (7, 24, 1, 6), (6, 18, 1, 6), (6, 24, 1, 6), (8, 0, 1, 6),
               (5, 24, 1, 6), (5, 18, 1, 6), (4, 0, 1, 5), (4, 5, 1, 5),
               (4, 10, 1, 5), (4, 15, 1, 5), (8, 12, 1, 6), (4, 20, 1, 5),
               (4, 25, 1, 5), (8, 18, 1, 6), (3, 0, 1, 15), (3, 15, 1, 10),
               (3, 25, 1, 5)]
        
        #action
        action = [self.action1, self.action2, self.action3, self.action4,
                  self.action5, self.action6, self.action7, self.action8,
                  self.action9, self.action0, self.action_equal, self.action_plus,
                  self.action_minus, self.action_mul, self.action_div, self.action_point,
                  self.action_clear, self.action_del, self.action_square,
                  self.action_power, self.action_sqrt, self.action_neg,
                  self.action_e, self.action_leftbrac, self.action_rightbrac,
                  self.action_ans, self.action_trigo, self.action_function,
                  self.action_more]
        
        tooltip_txt = ['', '', '', '', '', '', '', '', '', '', 'Answer', 'Addition',
                       'Subtraction', 'Multiplication', 'Division', 'Decimal Point',
                       'Reset', 'Delete', 'Square', 'Power',
                       'Square Root', 'Returns Negative Value', 'Constant e', 'Left Bracket',
                       'Right Bracket', 'Stores Previous Ans', 'Trigonometry', 'Functions',
                       'More']
        
        font = ['Abel', 'Times New Roman', 'Calibri', 'Arial',
                'Adam Warren pro', 'Brush Script MT']
        
        row_stretch = [(8, 2), (7, 2), (6, 2),
                       (5, 2), (4, 1), (0, 3),
                       (3, 1)]
        
        classic_equal = "QPushButton \
                          { \
                          border : 0px solid #D3D3D3; \
                          background-color : #00FFFF; \
                          color : black; \
                          border-radius : 8px; \
                          } \
                          QPushButton::hover \
                          { \
                          background-color : #96DED1; \
                          } \
                          QPushButton::pressed \
                          { \
                          background-color : #B6D0E2; \
                          }"
        
        dusk_equal = "QPushButton \
                          { \
                          border : 0px solid #D3D3D3; \
                          background-color : #C6DE41; \
                          color : #071C21; \
                          border-radius : 8px; \
                          } \
                          QPushButton::hover \
                          { \
                          background-color : #2D6E7E; \
                          } \
                          QPushButton::pressed \
                          { \
                          background-color : #C6DE41; \
                          }"
        
        shift_light = "QPushButton \
                          { \
                          border : 0px solid #D3D3D3; \
                          background-color : #f0f0f0; \
                          color : black; \
                          border-radius : 8px; \
                          } \
                          QPushButton::hover \
                          { \
                          background-color : #E5E4E2; \
                          } \
                          QPushButton::pressed \
                          { \
                          background-color : #D3D3D3; \
                          }"
                              
        shift_dark = "QPushButton \
                          { \
                          border : 0px solid #D3D3D3; \
                          background-color : #121212; \
                          color : white; \
                          border-radius : 8px; \
                          } \
                          QPushButton::hover \
                          { \
                          background-color : #2e2e2e; \
                          } \
                          QPushButton::pressed \
                          { \
                          background-color : #363636; \
                          }"
        
        shift_dusk = "QPushButton \
                          { \
                          border : 0px solid #D3D3D3; \
                          background-color : #071C21; \
                          color : #C6DE41; \
                          border-radius : 8px; \
                          } \
                          QPushButton::hover \
                          { \
                          background-color : #2D6E7E; \
                          } \
                          QPushButton::pressed \
                          { \
                          background-color : #071C21; \
                          }"
        
        equal_ss = [classic_equal, classic_equal, dusk_equal]
        shift_ss = [shift_light, shift_dark, shift_dusk]
               
        for row, stretch in row_stretch:
            grid.setRowStretch(row, stretch)
        
        #setting buttons and actions
        for i in range(len(button_txt)):
            
            txt = button_txt[i]
            btn = QPushButton(txt, self)    
            btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            btn.clicked.connect(action[i])
            
            if button_fontSize_index[i] == 1:
                btn.setFont(QFont(font[font_index], btn.rect().width() // 6))
                
            if button_fontSize_index[i] == 2:
                btn.setFont(QFont(font[3], btn.rect().width() // 9))
                
            if button_fontSize_index[i] == 3:
                btn.setFont(QFont(font[3], btn.rect().width() // 10))
                
            if button_fontSize_index[i] == 4:
                btn.setFont(QFont(font[0], btn.rect().width() // 10))
            
            x, y, rowspan, colspan = pos[i]
            grid.addWidget(btn, x, y, rowspan, colspan)
            
            if button_txt[i] == '\u221ax':
                sqrt_button = btn
            
            if tooltip_txt[i] != '':
                btn.setToolTip(tooltip_txt[i])
            
            #setting colour effect to = button
            if button_txt[i] == '=':
                btn.setStyleSheet(equal_ss[theme_index])
                
            if button_txt[i] == 'MORE' or button_txt[i] == 'TRIGONOMETRY' or button_txt[i] == 'FUNCTIONS':
                btn.setStyleSheet(shift_ss[theme_index])

    #defining button actions

    def action_equal(self):
        global eval_txt, Ans
        equation = eval_txt

        try:
            ans = eval(equation)
            Ans = ans
            self.label.setText('\n'+str(ans))
            eval_txt = str(ans)

        except:
            eval_txt = ''
            self.label.setText("\nInvalid Input")

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
        self.label.setText(text + " \u00f7 ")

    def action_mul(self):
        global eval_txt
        add_txt = '*'
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText(text + " \u00d7 ")

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
        self.label.setText("\n")

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
        add_txt = '**('
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText(text + "^")
        
    def action_sqrt(self):
        global eval_txt
        add_txt = 'sqrt('
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText(text + "\u221a(")
        
    def action_neg(self):
        add_txt = '*(-1)'
        global eval_txt, neg_count
        neg_count += 1
        eval_txt += add_txt
        text = self.label.text()
        if neg_count == 1:
            self.label.setText("-" + text)
        if neg_count == 2:
            neg_count = 0
            self.label.setText(text[1:])
        
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
        
    def action_ans(self):
        global eval_txt, Ans
        add_txt = str(Ans)
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText(text + "Ans")
        
    def action_more(self):
        x = 0
        
    def action_trigo(self):
        global groupbox_index, groupbox, theme_index
        
        classic_light = "QWidget \
            { \
             background : #f5f5f5; \
                 border : 0px; \
                     border-radius : 5px; \
                         font-style : italic; \
            QGroupBox \
                { \
                 background : #f0f0f0; \
                     border : 0px; \
                         border-radius : 5px; \
                     } \
                 } \
                QPushButton \
                    { \
                     border : 0px solid #D3D3D3; \
                         background : white; \
                             border-radius : 8px; \
                                 } \
                    QPushButton::hover \
                        { \
                         background-color : #E5E4E2; \
                             } \
                    QPushButton::pressed \
                        { \
                         background-color : #D3D3D3; \
                             }"
                            
        classic_dark = ("QWidget \
            { \
             background : #171717; \
                color : white; \
                    font-style : italic; \
                 } \
                QPushButton \
                    { \
                     border : 0px solid #363636; \
                         background : #1e1e1e; \
                             border-radius : 8px; \
                                 } \
                    QPushButton::hover \
                        { \
                         background-color : #2e2e2e; \
                             } \
                    QPushButton::pressed \
                        { \
                         background-color : #363636; \
                             }")
                            
        dusk = ("QWidget \
            { \
             background : #121C26; \
                color : #C6DE41; \
                    font-style : italic; \
                 } \
                QPushButton \
                    { \
                     border : 0px solid #153B44; \
                         background : #153B44; \
                             border-radius : 8px; \
                                 } \
                    QPushButton::hover \
                        { \
                         background-color : #2D6E7E; \
                             } \
                    QPushButton::pressed \
                        { \
                         background-color : #153B44; \
                             }")
        
        style_sheet = [classic_light, classic_dark, dusk]
        
        groupbox_index = 1
        self.groupbox = QGroupBox("")
        self.groupbox.setGeometry(100, 100, 100, 100)
        self.groupbox.setMinimumSize(300, 200)
        self.center(self.groupbox)
        self.groupbox.setWindowFlag(Qt.FramelessWindowHint)
        self.groupbox.setAttribute(Qt.WA_TranslucentBackground)
        self.groupbox.setStyleSheet(style_sheet[theme_index])
        if groupbox_index == 1:
            self.groupbox.show()

        grid = QGridLayout()
        grid.setSpacing(3)
        self.groupbox.setLayout(grid)
        
        button_txt = ['sin', 'cos', 'tan', 'cosec', 'sec', 'cot',
                      'sin\u207b\u00b9', 'cos\u207b\u00b9', 'tan\u207b\u00b9',
                      'cosec\u207b\u00b9', 'sec\u207b\u00b9', 'cot\u207b\u00b9']
        action = [self.action_sin, self.action_cos, self.action_tan,
                  self.action_cosec, self.action_sec, self.action_cot,
                  self.action_asin, self.action_acos, self.action_atan,
                  self.action_acosec, self.action_asec, self.action_acot]
        
        font = ['Abel', 'Times New Roman', 'Calibri', 'Arial',
                'Adam Warren pro', 'Brush Script MT']
        
        pos = [(0, 0, 1, 1), (0, 1, 1, 1), (0, 2, 1, 1),
               (1, 0, 1, 1), (1, 1, 1, 1), (1, 2, 1, 1),
               (2, 0, 1, 1), (2, 1, 1, 1), (2, 2, 1, 1),
               (3, 0, 1, 1), (3, 1, 1, 1), (3, 2, 1, 1)]
        
        button_fontSize_index = [2, 2, 2, 2, 2, 2,
                                 2, 2, 2, 2, 2, 2]
        
        for i in range(len(button_txt)):
            
            txt = button_txt[i]
            btn = QPushButton(txt, self)    
            btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            btn.clicked.connect(action[i])
            
            if button_fontSize_index[i] == 1:
                btn.setFont(QFont(font[font_index], btn.rect().width() // 6))
                
            if button_fontSize_index[i] == 2:
                btn.setFont(QFont(font[3], btn.rect().width() // 9))
                
            if button_fontSize_index[i] == 3:
                btn.setFont(QFont(font[0], btn.rect().width() // 10))
            
            x, y, rowspan, colspan = pos[i]
            grid.addWidget(btn, x, y, rowspan, colspan)
            
        groupbox = self.groupbox
                
    def groupbox_visible(self):
        global groupbox_index, groupbox
        
        if groupbox_index == 1:
            groupbox.show()

        if groupbox_index == 2:
            groupbox.hide()

        
    def action_function(self):
        global groupbox_index, groupbox, theme_index
        
        classic_light = "QWidget \
            { \
             background : #f5f5f5; \
                 border : 0px; \
                     border-radius : 5px; \
            QGroupBox \
                { \
                 background : #f0f0f0; \
                     border : 0px; \
                         border-radius : 5px; \
                     } \
                 } \
                QPushButton \
                    { \
                     border : 0px solid #D3D3D3; \
                         background : white; \
                             border-radius : 8px; \
                                 } \
                    QPushButton::hover \
                        { \
                         background-color : #E5E4E2; \
                             } \
                    QPushButton::pressed \
                        { \
                         background-color : #D3D3D3; \
                             }"
                            
        classic_dark = ("QWidget \
            { \
             background : #171717; \
                color : white; \
                 } \
                QPushButton \
                    { \
                     border : 0px solid #363636; \
                         background : #1e1e1e; \
                             border-radius : 8px; \
                                 } \
                    QPushButton::hover \
                        { \
                         background-color : #2e2e2e; \
                             } \
                    QPushButton::pressed \
                        { \
                         background-color : #363636; \
                             }")
                            
        dusk = ("QWidget \
            { \
             background : #121C26; \
                color : #C6DE41; \
                 } \
                QPushButton \
                    { \
                     border : 0px solid #153B44; \
                         background : #153B44; \
                             border-radius : 8px; \
                                 } \
                    QPushButton::hover \
                        { \
                         background-color : #2D6E7E; \
                             } \
                    QPushButton::pressed \
                        { \
                         background-color : #153B44; \
                             }")
        
        style_sheet = [classic_light, classic_dark, dusk]
        
        groupbox_index = 1
        self.groupbox = QGroupBox("")
        self.groupbox.setGeometry(100, 100, 100, 100)
        self.groupbox.setMinimumSize(300, 200)
        self.center(self.groupbox)
        self.groupbox.setWindowFlag(Qt.FramelessWindowHint)
        self.groupbox.setAttribute(Qt.WA_TranslucentBackground)
        self.groupbox.setStyleSheet(style_sheet[theme_index])
        if groupbox_index == 1:
            self.groupbox.show()
            
        #self.groupbox.setCheckable(True)
        #layout.addWidget(groupbox)

        grid = QGridLayout()
        grid.setSpacing(3)
        self.groupbox.setLayout(grid)
        
        button_txt = ['\u03c0', 'x!', 'x\u207b\u00b9',
                      'log(x)', 'ln(x)', '\u207fC\u1d63',
                      '\u207fP\u1d63', '\u1d43\u221a', '\u2308x\u2309',
                      '\u230ax\u230b', '\u0393x', '|x|']
        
        action = [self.action_pi, self.action_fac, self.action_inv,
                  self.action_log, self.action_ln, self.action_nCr,
                  self.action_nPr, self.action_x_root, self.action_ceil,
                  self.action_floor, self.action_gamma, self.action_mod]
        
        font = ['Abel', 'Times New Roman', 'Calibri', 'Arial',
                'Adam Warren pro', 'Brush Script MT']
        
        pos = [(0, 0, 1, 1), (0, 1, 1, 1), (0, 2, 1, 1),
               (1, 0, 1, 1), (1, 1, 1, 1), (1, 2, 1, 1),
               (2, 0, 1, 1), (2, 1, 1, 1), (2, 2, 1, 1),
               (3, 0, 1, 1), (3, 1, 1, 1), (3, 2, 1, 1)]
        
        button_fontSize_index = [2, 2, 2, 2, 2, 2,
                                 2, 2, 2, 2, 2, 2]
        
        for i in range(len(button_txt)):
            
            txt = button_txt[i]
            btn = QPushButton(txt, self)    
            btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            btn.clicked.connect(action[i])
            
            if button_fontSize_index[i] == 1:
                btn.setFont(QFont(font[font_index], btn.rect().width() // 6))
                
            if button_fontSize_index[i] == 2:
                btn.setFont(QFont(font[3], btn.rect().width() // 9))
                
            if button_fontSize_index[i] == 3:
                btn.setFont(QFont(font[0], btn.rect().width() // 10))
            
            x, y, rowspan, colspan = pos[i]
            grid.addWidget(btn, x, y, rowspan, colspan)
            
        groupbox = self.groupbox
        
    def action_sin(self):
        global eval_txt, groupbox_index
        groupbox_index = 2
        add_txt = 'sin('
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText(text + "sin(")
        self.groupbox_visible()
        
    def action_cos(self):
        global eval_txt, groupbox_index
        groupbox_index = 2
        add_txt = 'cos('
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText(text + "cos(")
        self.groupbox_visible()
        
    def action_tan(self):
        global eval_txt, groupbox_index
        groupbox_index = 2
        add_txt = 'tan('
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText(text + "tan(")
        self.groupbox_visible()
        
    def action_cosec(self):
        global eval_txt, groupbox_index
        groupbox_index = 2
        add_txt = '1/sin('
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText(text + "cosec(")
        self.groupbox_visible()
        
    def action_sec(self):
        global eval_txt, groupbox_index
        groupbox_index = 2
        add_txt = '1/cos('
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText(text + "sec(")
        self.groupbox_visible()
        
    def action_cot(self):
        global eval_txt, groupbox_index
        groupbox_index = 2
        add_txt = '1/tan(('
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText(text + "cot(")
        self.groupbox_visible()
        
    def action_asin(self):
        global eval_txt, groupbox_index
        groupbox_index = 2
        add_txt = 'asin('
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText(text + "sin\u207b\u00b9(")
        self.groupbox_visible()
        
    def action_acos(self):
        global eval_txt, groupbox_index
        groupbox_index = 2
        add_txt = 'acos('
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText(text + "cos\u207b\u00b9(")
        self.groupbox_visible()
        
    def action_atan(self):
        global eval_txt, groupbox_index
        groupbox_index = 2
        add_txt = 'atan('
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText(text + "tan\u207b\u00b9(")
        self.groupbox_visible()
        
    def action_acosec(self):
        global eval_txt, groupbox_index
        groupbox_index = 2
        add_txt = 'asin(1/('
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText(text + "cosec\u207b\u00b9((")
        self.groupbox_visible()
        
    def action_asec(self):
        global eval_txt, groupbox_index
        groupbox_index = 2
        add_txt = 'acos(1/('
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText(text + "sec((\u207b\u00b9")
        self.groupbox_visible()
        
    def action_acot(self):
        global eval_txt, groupbox_index
        groupbox_index = 2
        add_txt = 'atan(1/('
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText(text + "cot((\u207b\u00b9")
        self.groupbox_visible()
        
    def action_pi(self):
        global eval_txt, groupbox_index
        groupbox_index = 2
        add_txt = 'pi'
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText(text + "\u03c0")
        self.groupbox_visible()
                
    def action_fac(self):
        global eval_txt, groupbox_index
        groupbox_index = 2
        add_txt = 'factorial('
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText(text + "fac(")
        self.groupbox_visible()
        
    def action_inv(self):
        global eval_txt, groupbox_index
        groupbox_index = 2
        add_txt = '1/('
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText(text + "1/(")
        self.groupbox_visible() 
        
    def action_log(self):
        global eval_txt, groupbox_index
        groupbox_index = 2
        add_txt = 'log10('
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText(text + "log(")
        self.groupbox_visible()
        
    def action_ln(self):
        global eval_txt, groupbox_index
        groupbox_index = 2
        add_txt = 'log('
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText(text + "ln(")
        self.groupbox_visible()
    
    def action_nCr(self):
        x = 0
        '''global eval_txt, groupbox_index
        groupbox_index = 2
        add_txt = 'comb('
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText(text + "ln(")
        self.groupbox_visible()'''
        
    def action_nPr(self):
        x = 0
        
    def action_x_root(self):
        global eval_txt, groupbox_index
        groupbox_index = 2
        add_txt = '**(1.0/'
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText(text + "^(1/)")
        self.groupbox_visible()
        
    def action_ceil(self):
        global eval_txt, groupbox_index
        groupbox_index = 2
        add_txt = 'ceil('
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText(text + "\u2308(")
        self.groupbox_visible()
        
    def action_floor(self):
        global eval_txt, groupbox_index
        groupbox_index = 2
        add_txt = 'floor('
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText(text + "\u230a(")
        self.groupbox_visible()
        
    def action_gamma(self):
        global eval_txt, groupbox_index
        groupbox_index = 2
        add_txt = 'gamma('
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText(text + "\u0393(")
        self.groupbox_visible()
        
    def action_mod(self):
        global eval_txt, groupbox_index
        groupbox_index = 2
        add_txt = 'abs('
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText(text + "|(")
        self.groupbox_visible()
        
    def action_fac(self):
        global eval_txt, groupbox_index
        groupbox_index = 2
        add_txt = 'factorial('
        eval_txt += add_txt
        text = self.label.text()
        self.label.setText(text + "fac(")
        self.groupbox_visible() 
        
    def center(self, groupbox):
        qr = groupbox.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        groupbox.move(qr.topLeft())
        
class __main__window__(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        #setting default window geometry
        self.setGeometry(100, 100, 100, 500)
        self.setMinimumSize(400, 400)
        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('Calculator.ico'))
        self.statusbar = self.statusBar()
        self.statusBar().showMessage('v 1.0.0')
        self.center()
        self.menu_bar()
        self.call_widget()
        self.show()
        
    def call_widget(self):
        widget = __widget__()
        global theme_index
        
        classic_light = "QWidget \
            { \
             background : #f0f0f0; \
                 } \
                QPushButton \
                    { \
                     border : 0px solid #D3D3D3; \
                         background : white; \
                             border-radius : 8px; \
                                 } \
                    QPushButton::hover \
                        { \
                         background-color : #E5E4E2; \
                             } \
                    QPushButton::pressed \
                        { \
                         background-color : #D3D3D3; \
                             } \
                QLabel \
                    { \
                     color : black; \
                         font-size : 25pt; \
                             } \
                QMenu \
                    { \
                     min-width : 80px; \
                         background-color : white; \
                             } \
                    QMenu::item \
                        { \
                         min-width : 60px; \
                             margin : 5; \
                                 padding : 5; \
                                     } \
                    QMenu::item:selected \
                        { \
                         color : black; \
                             background-color : #E5E4E2; \
                                 border : 0px solid black; \
                                     border-radius : 5px; \
                                         } \
                    QMenu::item:pressed \
                        { \
                         background-color : #D3D3D3; \
                             } \
                    QMenuBar::item:selected \
                        { \
                         border : 0px solid black; \
                             border-radius : 5px; \
                                 background-color : #E5E4E2; \
                                     } \
                    QMenuBar::item:pressed \
                        { \
                         background-color : white; \
                             }"
                            
        classic_dark = ("QWidget \
            { \
             background : #121212; \
                color : white; \
                 } \
                QPushButton \
                    { \
                     border : 0px solid #363636; \
                         background : #1e1e1e; \
                             border-radius : 8px; \
                                 } \
                    QPushButton::hover \
                        { \
                         background-color : #2e2e2e; \
                             } \
                    QPushButton::pressed \
                        { \
                         background-color : #363636; \
                             } \
                QLabel \
                    { \
                     color : white; \
                         font-size : 25pt; \
                             } \
                QMenu \
                    { \
                     min-width : 80px; \
                         background-color : #1e1e1e; \
                             } \
                    QMenu::item \
                        { \
                         min-width : 60px; \
                             margin : 5; \
                                 padding : 5; \
                                     } \
                    QMenu::item:selected \
                        { \
                         color : white; \
                             background-color : #2e2e2e; \
                                 border : 0px solid white; \
                                     border-radius : 5px; \
                                         } \
                    QMenu::item:pressed \
                        { \
                         background-color : #363636; \
                             } \
                    QMenuBar::item:selected \
                        { \
                         border : 0px solid white; \
                             border-radius : 5px; \
                                 background-color : #2e2e2e; \
                                     } \
                    QMenuBar::item:pressed \
                        { \
                         background-color : #1e1e1e; \
                             }")
                            
        dusk = ("QWidget \
            { \
             background : #071C21; \
                color : #C6DE41; \
                 } \
                QPushButton \
                    { \
                     border : 0px solid #153B44; \
                         background : #153B44; \
                             border-radius : 8px; \
                                 } \
                    QPushButton::hover \
                        { \
                         background-color : #2D6E7E; \
                             } \
                    QPushButton::pressed \
                        { \
                         background-color : #153B44; \
                             } \
                QLabel \
                    { \
                     color : #C6DE41; \
                         font-size : 25pt; \
                             } \
                QMenu \
                    { \
                     min-width : 80px; \
                         background-color : #153B44; \
                             } \
                    QMenu::item \
                        { \
                         min-width : 60px; \
                             margin : 5; \
                                 padding : 5; \
                                     } \
                    QMenu::item:selected \
                        { \
                         color : #C6DE41; \
                             background-color : #2D6E7E; \
                                 border : 0px solid #C6DE41; \
                                     border-radius : 5px; \
                                         } \
                    QMenu::item:pressed \
                        { \
                         background-color : #153B44; \
                             } \
                    QMenuBar::item:selected \
                        { \
                         border : 0px solid #C6DE41; \
                             border-radius : 5px; \
                                 background-color : #2D6E7E; \
                                     } \
                    QMenuBar::item:pressed \
                        { \
                         background-color : #153B44; \
                             }")
        
        style_sheet = [classic_light, classic_dark, dusk]
        
        '''QWidget{background : green; border : 2px solid black; border-radius : 8px;}"
        "QMainWindow{background : blue; border : 2px solid black; border-radius : 8px;}"
        "QApplication{background : green; border : 2px solid black; border-radius : 8px;}"
        "QMenu{background : red; border : 2px solid black; border-radius : 8px;}"
        "QMenu::item:selected{background : green; border : 2px solid black; border-radius : 8px;}"
        "QGui{background : green; border : 2px solid black; border-radius : 8px;}"
        "QFrame{background : green; border : 2px solid black; border-radius : 8px;}"
        "QComboBox{background : green; border : 2px solid black; border-radius : 8px;}"
        "Qlabel{background : green; border : 2px solid black; border-radius : 8px;}"
        "QGroupBox{background : green; border : 2px solid black; border-radius : 8px;}"
        "QMenuBar::item{background : green; border : 2px solid black; border-radius : 8px;}'''
        
        self.setCentralWidget(widget)
        self.setStyleSheet(style_sheet[theme_index])
        self.hbox = QHBoxLayout()
        self.centralWidget().setLayout(self.hbox)
       
        
    def menu_bar(self):
        menubar = self.menuBar()
        self.file_menu(menubar)
        self.view_menu(menubar)
        return menubar
        
        
    def file_menu(self, menubar):
        fileMenu = menubar.addMenu('&File')
        quit_act = self.exit_act()
        fileMenu.addAction(quit_act)
        
    def view_menu(self, menubar):
        viewMenu = menubar.addMenu('&View')
        self.view_stat_act(viewMenu)
        self.view_button_menu(viewMenu)
        self.view_display_menu(viewMenu)
    
    def view_button_menu(self, viewMenu):
        button_menu = QMenu('Buttons', self)
        font_menu = QMenu('Font', self)
        button_menu.addMenu(font_menu)
        icon = ['abel.png', 'times_new_roman.png', 'calibri.png',
                'arial.png', 'adam_warren_pro.png', 'brush_script.png']

        font_fcn = [self.__Abel__(icon[0]), self.__timesNewRoman__(icon[1]),
                    self.__calibri__(icon[2]), self.__arial__(icon[3]),
                    self.__adamWarrenPro__(icon[4]), self.__brushScriptMT__(icon[5])]
        
        for i in range(len(font_fcn)):
            font = font_fcn[i]
            font_menu.addAction(font)

        viewMenu.addMenu(button_menu)
        
    def view_display_menu(self, viewMenu):
        display_menu = QMenu('Themes', self)

        theme_fcn = [self.__classicLight__(), self.__classicDark__(), self.__dusk__()]
        
        for i in range(len(theme_fcn)):
            theme = theme_fcn[i]
            display_menu.addAction(theme)

        viewMenu.addMenu(display_menu)
        
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
            
    def __classicLight__(self):
        light = QAction(QIcon('light_theme.png'), 'Classic Light', self)
        light.triggered.connect(self.theme_light)
        return light
        
    def theme_light(self):
        global theme_index
        theme_index = 0
        self.call_widget()
        
    def __classicDark__(self):
        dark = QAction(QIcon('dark_theme.png'), 'Classic Dark', self)
        dark.triggered.connect(self.theme_dark)
        return dark
        
    def theme_dark(self):
        global theme_index
        theme_index = 1
        self.call_widget()
        
    def __dusk__(self):
        dark = QAction(QIcon('dusk_theme.png'), 'Dusk', self)
        dark.triggered.connect(self.theme_dusk)
        return dark
        
    def theme_dusk(self):
        global theme_index
        theme_index = 2
        self.call_widget()

    def __Abel__(self, icon):
        Abel = QAction(QIcon(icon), 'Abel', self)
        Abel.triggered.connect(self.Abel_font)
        return Abel
    
    def __timesNewRoman__(self, icon):
        Times_New_Roman = QAction(QIcon(icon), 'Times New Roman', self)
        Times_New_Roman.triggered.connect(self.times_new_roman_font)
        return Times_New_Roman
    
    def __calibri__(self, icon):
        Calibri = QAction(QIcon(icon), 'Calibri', self)
        Calibri.triggered.connect(self.calibri_font)
        return Calibri
    
    def __arial__(self, icon):
        Calibri = QAction(QIcon(icon), 'Arial', self)
        Calibri.triggered.connect(self.arial_font)
        return Calibri
    
    def __adamWarrenPro__(self, icon):
        Calibri = QAction(QIcon(icon), 'Adam Warren Pro', self)
        Calibri.triggered.connect(self.adam_warren_pro_font)
        return Calibri
    
    def __brushScriptMT__(self, icon):
        brush_script = QAction(QIcon(icon), 'Brush Script MT', self)
        brush_script.triggered.connect(self.brush_script_font)
        return brush_script
            
    def Abel_font(self):
        global font_index
        font_index = 0
        self.call_widget()
        
    def times_new_roman_font(self):
        global font_index
        font_index = 1
        self.call_widget()
        
    def calibri_font(self):
        global font_index
        font_index = 2
        self.call_widget()
        
    def arial_font(self):
        global font_index
        font_index = 3
        self.call_widget()
        
    def adam_warren_pro_font(self):
        global font_index
        font_index = 4
        self.call_widget()
        
    def brush_script_font(self):
        global font_index
        font_index = 5
        self.call_widget()
        
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
        global theme_index
        cmenu = QMenu()
        dark = "QMenu \
                            { \
                             min-width : 80px; \
                                 background-color : #1e1e1e; \
                                     color: white; \
                                     } \
                            QMenu::item \
                            { \
                             min-width : 60px; \
                                 margin : 5; \
                                     padding : 5; \
                                         } \
                                QMenu::item:selected \
                            { \
                             color : white; \
                                 background-color : #2e2e2e; \
                                     border : 0px solid black; \
                                         border-radius : 5px; \
                                             } \
                                QMenu::item:pressed \
                                    { \
                                     background-color : #363636; \
                                         }"
                                        
        light = "QMenu \
                            { \
                             min-width : 80px; \
                                 background-color : white; \
                                     color : black; \
                                     } \
                            QMenu::item \
                            { \
                             min-width : 60px; \
                                 margin : 5; \
                                     padding : 5; \
                                         } \
                                QMenu::item:selected \
                            { \
                             color : black; \
                                 background-color : #E5E4E2; \
                                     border : 0px solid black; \
                                         border-radius : 5px; \
                                             } \
                                QMenu::item:pressed \
                                    { \
                                     background-color : #D3D3D3; \
                                         }"
        
        dusk = "QMenu \
                            { \
                             min-width : 80px; \
                                 background-color : #153B44; \
                                     color : #c6de41; \
                                     } \
                            QMenu::item \
                            { \
                             min-width : 60px; \
                                 margin : 5; \
                                     padding : 5; \
                                         } \
                                QMenu::item:selected \
                            { \
                             color : #c6de41; \
                                 background-color : #2d6e7e; \
                                     border : 0px solid black; \
                                         border-radius : 5px; \
                                             } \
                                QMenu::item:pressed \
                                    { \
                                     background-color : #153b44; \
                                         }"
        
        cmenu_ss = [light, dark, dusk]
        cmenu.setStyleSheet(cmenu_ss[theme_index])
        quitAct = cmenu.addAction(QIcon('quit.png'), "Quit")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAct:
            qApp.quit()


#defining main function to run application        
def main():
    app = QApplication(sys.argv)
    win = __main__window__()
    '''win.setStyleSheet("QWidget{background : green; border : 2px solid black; border-radius : 8px;}"
                      "QMainWindow{background : blue; border : 2px solid black; border-radius : 8px;}"
                      "QApplication{background : green; border : 2px solid black; border-radius : 8px;}"
                      "QMenu{background : red; border : 2px solid black; border-radius : 8px;}"
                      "QMenu::item:selected{background : green; border : 2px solid black; border-radius : 8px;}"
                      "QGui{background : green; border : 2px solid black; border-radius : 8px;}"
                      "QFrame{background : green; border : 2px solid black; border-radius : 8px;}"
                      "QComboBox{background : green; border : 2px solid black; border-radius : 8px;}"
                      "Qlabel{background : green; border : 2px solid black; border-radius : 8px;}"
                      "QGroupBox{background : green; border : 2px solid black; border-radius : 8px;}"
                      "QMenuBar::item{background : green; border : 2px solid black; border-radius : 8px;}"
                      )'''
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()