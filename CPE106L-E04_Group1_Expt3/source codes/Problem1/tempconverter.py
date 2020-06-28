import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from decimal import Decimal

qtcreator_file = "TEMPGUI.ui"  # ui file here
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.FahConvert.clicked.connect(self.Fahconvert)
        self.CelConvert.clicked.connect(self.Celconvert)

    def Fahconvert(self):
        tempC = Decimal(self.Fahrenheit.toPlainText())
        tempC = round(((tempC)-32)*5/9, 3)
        self.Celsius.setPlainText(str(tempC))

    def Celconvert(self):
        tempF = Decimal(self.Celsius.toPlainText())
        tempF = round((tempF)*9/5+32, 3)

        self.Fahrenheit.setPlainText(str(tempF))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())