## demo2_1_Hello.py

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

app = QtWidgets.QApplication(sys.argv)   #建立app, 用Qapplication 類別
widgetHello = QtWidgets.QWidget()        #建立表單, 用QWidget 類別
widgetHello.resize(280, 150)             #設定表單的寬度和高度
widgetHello.setWindowTitle("Demo2_1")    #設定表單的標題文字

LabHello = QtWidgets.QLabel(widgetHello)
LabHello.setText("Hello World, PyQt5")

font = QtGui.QFont()
font.setPointSize(12)
font.setBold(True)
LabHello.setFont(font)
size=LabHello.sizeHint()
LabHello.setGeometry(70,60, size.width(), size.height())

widgetHello.show()
sys.exit(app.exec())