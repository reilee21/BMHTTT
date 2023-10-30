import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QFileDialog, QMessageBox
from PyQt6 import QtCore, QtGui, QtWidgets
from manhinh2 import MyMainWindow


class ManHinhChinh(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setMaximumSize(QtCore.QSize(1000, 600))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("QPushButton{\n"
"    border-radius:10px;\n"
"    border:2px solid #E6F4F1;\n"
"    color:black;\n"
"    background-color:#E6F4F1;\n"
"    font:bold;    \n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #003748;\n"
"    color: white;\n"
"}\n"
"QLabel{\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1000, 500))
        self.label.setMaximumSize(QtCore.QSize(1000, 600))
        self.label.setStyleSheet("border-image: url(icon//bg.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 500, 1000, 100))
        self.label_2.setStyleSheet("background-color: rgb(52, 191, 210);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(225, 30, 550, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(425, 500, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(350, 320, 300, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.layoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(100, 110, 521, 191))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_6 = QtWidgets.QLabel(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.wd = MyMainWindow()
        self.Event()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Phần mềm mã hoá văn bản tiếng việt"))
        self.label_3.setText(_translate("MainWindow", "Các thuật toán mã hoá văn bản tiếng việt"))
        self.pushButton.setText(_translate("MainWindow", "Bắt đầu"))
        self.label_7.setText(_translate("MainWindow", "HỌC KỲ I NĂM HỌC 2023-2024 "))
        self.label_5.setText(_translate("MainWindow", "Lê Hoàng Quốc Khánh – 21DH113760 "))
        self.label_4.setText(_translate("MainWindow", "Võ Hoàng Thái Đạt – 21DH114385"))
        self.label_6.setText(_translate("MainWindow", "Lê Ngọc Tùng – 21DH114565 "))


    def Event(self):
        self.pushButton.clicked.connect(self.ex)
                
    def ex(self):
        self.wd.show()
        self.window.close()



def main():
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = ManHinhChinh()
    ui.setupUi(window)  
    ui.window = window 
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()