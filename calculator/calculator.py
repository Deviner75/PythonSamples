from PySide.QtCore import *
from PySide.QtGui import *
import calculator_uis as ui
import re
from math import sqrt

class calculatorClass(QMainWindow, ui.Ui_Calculator):
    def __init__(self):
        super(calculatorClass, self).__init__()
        self.setupUi(self)

        #variable
        self.fieldList = ''
        self.labelList = ''
        self.temp = 0
        self.prcntSqr_temp = 0
        self.history = []

        #connects
        self.clear_btn.clicked.connect(self.clear)
        self.gClear_btn.clicked.connect(self.clear)
        self.minus_btn.clicked.connect(lambda: self.action('-'))
        self.plus_btn.clicked.connect(lambda: self.action('+'))
        self.mult_btn.clicked.connect(lambda: self.action('*'))
        self.divide_btn.clicked.connect(lambda: self.action('/'))
        self.backspace_btn.clicked.connect(self.backspace)
        self.dot_btn.clicked.connect(self.dot)
        self.equal_btn.clicked.connect(self.equal)
        self.negate_btn.clicked.connect(self.negate)
        self.percent_btn.clicked.connect(self.percent)
        self.sqr_btn.clicked.connect(self.sqr)
        self.root_btn.clicked.connect(self.root)
        self.oneDivider_btn.clicked.connect(self.oneDiv)


        for i in xrange(0, 10):
            btn = self.__dict__.get('btn_' + str(i))
            if btn:
                btn.clicked.connect(self.input)

    def display(self):
        # update display and label
        self.field.display(self.fieldList)
        self.label.setText(self.labelList)

    def eval(self):
        # eval equation
        result = eval(re.split(r'[\W]+$', self.labelList)[0])
        return result

    def input(self):
        # input numbers
        if self.temp == 1:
            self.fieldList = ''
            self.temp = 0
            if self.prcntSqr_temp == 1:
                self.labelList = re.split(r'[^-+*/]+$', self.labelList)[0]
                self.prcntSqr_temp = 0
        sender = self.sender()
        self.fieldList += sender.objectName()[-1]
        self.display()

    def action(self, sign):
        # input -+*/
        if self.temp == 0 or self.prcntSqr_temp == 1:
            if self.prcntSqr_temp == 1:
                self.fieldList = ''
                self.prcntSqr_temp = 0
                self.fieldList = self.eval()
                self.labelList += sign
            else:
                a1 = format(self.field.value(), '.10g')
                self.labelList += str(a1) + sign
                self.fieldList = self.eval()
                self.temp = 1
            self.display()

    def equal(self):
        a1 = format(self.field.value(), '.2g')
        if self.prcntSqr_temp != 1:
            self.labelList += str(a1)
        self.fieldList = eval(self.labelList)
        self.labelList = ''
        self.display()

    def dot(self):
        if self.temp == 0:
            self.fieldList += '.'
            self.display()

    def backspace(self):
        self.fieldList = self.fieldList[:-1]
        self.display()

    def negate(self):
        if self.prcntSqr_temp == 1:
            self.labelList = re.split(r'[^-+*/]+$', self.labelList)[0]
        if self.labelList == '':
            self.labelList += '-'
        elif self.labelList[-1] != '-':
            self.labelList = self.labelList[:-1] + '-'
        else:
            self.labelList = self.labelList[:-1] + '+'
        self.temp = 0
        self.prcntSqr_temp = 0
        self.display()

    def percent(self):
        if self.fieldList:
            a1 = self.field.value()
            b1 = self.eval()
            result = b1 * a1 / 100
            self.fieldList = result
            self.labelList += format(result, '.2g')
            self.prcntSqr_temp = 1
            self.temp = 1
            self.display()

    def sqr(self):
        if self.temp == 0 and self.fieldList:
            result = format((self.field.value() ** 2), '.2g')
            self.labelList += result
            self.prcntSqr_temp = 1
            self.temp = 1
            self.fieldList = result
            self.display()

    def clear(self):
        sender = self.sender().objectName()
        self.temp = 0
        self.prcntSqr_temp = 0
        if sender == 'clear_btn':
            self.fieldList = ''
        elif sender == 'gClear_btn':
            self.fieldList = ''
            self.labelList = ''
        self.display()

    def root(self):
        if self.temp == 0 and self.fieldList:
            result = format(sqrt(float(self.fieldList)), '.2g')
            self.labelList += result
            self.prcntSqr_temp = 1
            self.temp = 1
            self.fieldList = result
            self.display()

    def oneDiv(self):
         if self.fieldList:
            result = 1 / float(self.fieldList)
            self.labelList += format(result, '.2g')
            self.prcntSqr_temp = 1
            self.temp = 1
            self.fieldList = result
            self.display()

if __name__ == '__main__':
    app = QApplication([])
    w = calculatorClass()
    w.show()
    app.exec_()