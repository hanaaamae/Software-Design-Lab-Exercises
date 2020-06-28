import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize    

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(240, 200))    
        self.setWindowTitle("Temperature Converter") 

        self.c_to_f_label = QLabel(self)
        self.c_to_f_label.setText('Celsius')
        self.c_to_f_label.move(40, 20)
        self.c_to_f_input = QLineEdit(self)

        self.c_to_f_input.move(30, 60)
        self.c_to_f_input.resize(70, 32)
     
        self.f_to_c_label = QLabel(self)
        self.f_to_c_label.setText('Fahrenheit')
        self.f_to_c_label.move(140, 20)
        self.f_to_c_input = QLineEdit(self)

        self.f_to_c_input.move(130, 60)
        self.f_to_c_input.resize(70, 32)

        self.setStyleSheet("QLabel {font: 12pt Arial}")
        self.c_to_f_input.setText('0')
        self.f_to_c_input.setText('32')
        
        pybutton1 = QPushButton('>>>>', self)
        pybutton1.clicked.connect(self.clickMethod1)
        pybutton1.resize(50,32)
        pybutton1.move(40, 100)

        pybutton2 = QPushButton('<<<<', self)
        pybutton2.clicked.connect(self.clickMethod2)
        pybutton2.resize(50,32)
        pybutton2.move(140, 100)

        Clear = QPushButton('Clear', self)
        Clear.clicked.connect(self.clickMethod3)
        Clear.resize(50,32)
        Clear.move(95, 140)

    def clickMethod1(self):
        self.f_to_c_input.setText(str(round(float(self.c_to_f_input.text())*9/5+32,2)))

    def clickMethod2(self):
        self.c_to_f_input.setText(str(round((float(self.f_to_c_input.text())-32)*5/9,2)))
        
    def clickMethod3(self):
        self.c_to_f_input.clear()
        self.f_to_c_input.clear()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )