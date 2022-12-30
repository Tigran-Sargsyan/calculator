from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5 import QtGui
import math
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()
        
        # Loading the ui file
        uic.loadUi("calculator.ui", self) 
        
        # Changing the title of the window
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QtGui.QIcon("icon.png"))

        # Showing the window
        self.show()

        # sign_count variable for understanding the proper
        # sign of the variable if present
        self.sign_count = 0

        # Defining buttons
        self.btn0 = self.findChild(QPushButton,"btn0")
        self.btn1 = self.findChild(QPushButton,"btn1")
        self.btn2 = self.findChild(QPushButton,"btn2")
        self.btn3 = self.findChild(QPushButton,"btn3")
        self.btn4 = self.findChild(QPushButton,"btn4")
        self.btn5 = self.findChild(QPushButton,"btn5")
        self.btn6 = self.findChild(QPushButton,"btn6")
        self.btn7 = self.findChild(QPushButton,"btn7")
        self.btn8 = self.findChild(QPushButton,"btn8")
        self.btn9 = self.findChild(QPushButton,"btn9")
        self.plus = self.findChild(QPushButton,"plus")
        self.minus = self.findChild(QPushButton,"minus")
        self.mult = self.findChild(QPushButton,"mult")
        self.div = self.findChild(QPushButton,"div")
        self.result = self.findChild(QLabel,"result")
        self.equal = self.findChild(QPushButton,"equal")
        self.clear = self.findChild(QPushButton,"clear")
        self.signn = self.findChild(QPushButton,"sign")
        self.point = self.findChild(QPushButton,"point") 

        # Clicking buttons
        self.btn1.clicked.connect(lambda: self.click(self.btn1,"1"))
        self.btn2.clicked.connect(lambda: self.click(self.btn2,"2"))
        self.btn3.clicked.connect(lambda: self.click(self.btn3,"3"))
        self.btn4.clicked.connect(lambda: self.click(self.btn4,"4"))
        self.btn5.clicked.connect(lambda: self.click(self.btn5,"5"))
        self.btn6.clicked.connect(lambda: self.click(self.btn6,"6"))
        self.btn7.clicked.connect(lambda: self.click(self.btn7,"7"))
        self.btn8.clicked.connect(lambda: self.click(self.btn8,"8"))
        self.btn9.clicked.connect(lambda: self.click(self.btn9,"9"))
        self.btn0.clicked.connect(lambda: self.click(self.btn0,"0"))
        self.plus.clicked.connect(lambda: self.click(self.plus,"+"))
        self.minus.clicked.connect(lambda: self.click(self.minus,"-"))
        self.mult.clicked.connect(lambda: self.click(self.mult,"*"))
        self.div.clicked.connect(lambda: self.click(self.div,"/"))
        self.equal.clicked.connect(lambda: self.click(self.equal,"="))
        self.clear.clicked.connect(lambda: self.click(self.clear,"C"))
        self.signn.clicked.connect(lambda: self.click(self.signn,"+/-"))
        self.point.clicked.connect(lambda: self.click(self.point,"."))

        self.result.setAlignment(QtCore.Qt.AlignRight)

        # A list of all the number-buttons in the calculator
        self.num_list = [
            self.btn0,
            self.btn1,
            self.btn2,
            self.btn3,
            self.btn4,
            self.btn5,
            self.btn6,
            self.btn7,
            self.btn8,
            self.btn9,
        ]

        # A list of all basic mathematical signs
        self.sign_list = [
            "+",
            "-",
            "*",
            "/"
        ]

        # A variable for holding the expression we are going to calculate the result for
        self.expression = ""

        # Styling 
        design = 'color: #003300; background-color: #7b7b87;'

        self.setStyleSheet('background-color: #adc9c3;')
        self.clear.setStyleSheet(design)
        self.plus.setStyleSheet(design)
        self.minus.setStyleSheet(design)
        self.div.setStyleSheet(design)
        self.mult.setStyleSheet(design)
        self.signn.setStyleSheet(design)
        self.point.setStyleSheet(design)
        self.equal.setStyleSheet('color: #e8e8ff; background-color: #1A9900')

        for button in self.num_list:
            button.setStyleSheet('color: #000000; background-color: #7b7b87;')

    def click(self,btn,symbol):
        """
        A function which takes as an input the button object 
        that has been clicked and it's corresponding symbol and 
        invokes the function according to that symbol
        """
        count = 0

        if self.expression and self.expression[-1] == '0' and symbol != '.':
            print('added sth!')
            return self.expression

        if symbol == "=":
            self.expression = str(self.count(self.expression))
            self.set_output(self.expression)
            self.sign_count = 0

        elif (symbol in self.sign_list) and self.expression and (self.expression[-1] in self.sign_list):
            self.expression = self.expression[:-1] + symbol
            self.set_output(self.expression)
    
        elif symbol == "C":
            self.expression = ""
            self.set_output(self.expression)

        elif symbol == "+/-":
            if self.sign_count % 2 == 0:
                self.expression = "-"
                self.set_output(self.expression) 

            else:              
                self.set_output("")
                self.expression = ""
            self.sign_count += 1
        elif not self.expression and symbol in self.sign_list:
            return self.expression
        else:
            self.expression += symbol
            for sign in self.sign_list:
                count += self.expression.count(sign)
            if count > 1:
                self.expression = ""
                self.set_output(self.expression)
            else:        
                self.set_output(self.expression)

        print(self.expression)

    def check_if_int(self,num):
        """
        A function that takes a number as an input and
        returns integer form of it if it is an integer
        and float format of it if it is a float
        """
        if num == int(num):
            return int(num)
        return round(num,7)   

    def count(self,expression):
        """
        A function that takes an expression as an input
        and calculates the result
        """
        if not '+' in expression and not '-' in expression and not '*' in expression and not '/' in expression:  
            return self.expression
        for i in range(len(expression)):
            if expression[i] in self.sign_list:
                sign = expression[i]
                index = i

        op1 = float(expression[:index])
        op2 = float(expression[index+1:])

        if sign == "+":
            res = op1 + op2
            return self.check_if_int(res)
        elif sign == "-":
            res = op1 - op2
            return self.check_if_int(res)
        elif sign == "*":
            res = op1 * op2
            return self.check_if_int(res)
        elif sign == "/":
            res = op1 / op2
            return self.check_if_int(res)

    def set_output(self,output):
        """
        A function that takes a string as an input
        and prints that string into interface
        """
        self.result.setText(output)
 
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()                