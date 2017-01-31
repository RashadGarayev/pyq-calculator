# -*-coding: utf-8 -*-
from __future__ import division
from __future__ import unicode_literals
from PyQt4.QtGui import*
from PyQt4.QtCore import*
import sys
class window(QWidget):
    def __init__(self, parent=None):
        super(window, self).__init__(parent)
        # ------Window setting-------------------
        self.setWindowTitle(u'Hesablama maşını')
        self.setWindowIcon(QIcon('icon.png'))
        self.setGeometry(400,400,220,220)
        self.setFixedSize(220,220)
        self.entry=QLineEdit(self)
        self.entry.move(5,5)
        self.entry.setAlignment(Qt.AlignRight)
        self.entry.resize(200,25)
        #--------------------------------------
        zero = QPushButton("0",self)
        zero.move(10,180)
        zero.resize(35,30)
        #--------------------------------------
        one = QPushButton("1",self)
        one.move(10,145)
        one.resize(35,30)
        #--------------------------------------
        two = QPushButton("2",self)
        two.move(50,145)
        two.resize(35,30)
        #--------------------------------------
        three = QPushButton("3",self)
        three.move(90,145)
        three.resize(35,30)
        #---------------------------------------
        four = QPushButton("4",self)
        four.move(10,110)
        four.resize(35,30)
        #-------------------------------------
        five = QPushButton("5",self)
        five.move(50,110)
        five.resize(35,30)
        #--------------------------------------
        six = QPushButton("6",self)
        six.move(90,110)
        six.resize(35,30)
        #--------------------------------------
        seven = QPushButton("7",self)
        seven.move(10,75)
        seven.resize(35,30)
        #--------------------------------------
        eight = QPushButton("8",self)
        eight.move(50,75)
        eight.resize(35,30)
        #--------------------------------------
        nine = QPushButton("9",self)
        nine.move(90,75)
        nine.resize(35,30)
        #---------------------------------------
        info = QPushButton("",self)
        info.move(50,180)
        info.resize(35,30)
        info.setIcon(QIcon('info.png'))
        info.setIconSize(QSize(35,30))
        #---------------------------------------
        point = QPushButton(".",self)
        point.move(90,180)
        point.resize(35,30)
        #--------------------------------------
        div = QPushButton("/",self)
        div.move(130,75)
        div.resize(35,30)
        #---------------------------------------
        mult = QPushButton("*",self)
        mult.move(130,110)
        mult.resize(35,30)
        #---------------------------------------
        minus = QPushButton("-",self)
        minus.move(130,145)
        minus.resize(35,30)
        #---------------------------------------
        plus = QPushButton("+",self)
        plus.move(130,180)
        plus.resize(35,30)
        #---------------------------------------
        procent = QPushButton(u"",self)
        procent.move(170,75)
        procent.resize(35,30)
        #----------------------------------------
        squared = QPushButton(u"x²",self)
        squared.move(170,110)
        squared.resize(35,30)
        squared.clicked.connect(self.kvad)
        #----------------------------------------
        equal = QPushButton("=",self)
        equal.move(170,145)
        equal.resize(35,65)
        equal.clicked.connect(self.equ)
        #---------------------------------------
        c = QPushButton("C",self)
        c.move(145,35)
        c.resize(60,30)
        c.clicked.connect(self.clean)
        #----------------------------------------
        q = QPushButton("QUIT",self)
        q.move(77,35)
        q.resize(60,30)
        q.clicked.connect(self.exiting)
        #----------------------------------------
        back = QPushButton("<--",self)
        back.move(10,35)
        back.setToolTip('Backspace')
        back.resize(60,30)
        back.pressed.connect(self.backsp)

        op=[q,div,mult,minus,plus]
        for v in op:
            v.clicked.connect(self.operator)
        #---------------------------------------------
        ops=[point]
        for i in ops:
            i.clicked.connect(self.oper)
        #-----------------------------------------------------------------------
        number = [zero, one, two, three, four, five, six, seven, eight, nine]
        for i in number:
            i.clicked.connect(self.clicin)
        #-------Window show-----------------------------------
        self.show()
    def oper(self):
        sender=self.sender()

        self.entry.setText(self.entry.text()+sender.text())
    def exiting(self):
        self.close()
    def clicin(self):
        sender=self.sender()
        float(sender.text())
        if False==False:
            self.entry.setText(self.entry.text()+sender.text())
        else:
            self.entry.setText(sender.text())
    def operator(self):
        sender=self.sender()
        i=sender.text()
        if False==False:

            self.entry.setText(self.entry.text()+i)
        else:

            self.entry.setText(str(i))
    def equ(self):
                i=self.entry.text()
                self.entry.setText(str(eval(str(i))))               
    def kvad(self):
        try:
            i=float(self.entry.text())
            v=pow(i,2)
            self.entry.setText(str(v))
        except OverflowError:
            self.entry.clear()
            self.entry.setText('Sorry, out of range')
        except ValueError:
            self.entry.clear()
    def backsp(self):
        self.entry.backspace()
    def clean(self):
        self.entry.clear()

if __name__ == '__main__':
    app = QApplication([])
    gui = window()
    app.exec_()
