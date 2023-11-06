from PyQt6.QtWidgets import QDialog,QLineEdit,QMessageBox
from login import Ui_Dialog
from PyQt6 import QtGui
from PyQt6.QtCore import pyqtSignal
from manhinhregis import RegisterDialog
from mahoaclass import mahoasha3 
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
account_file_path = os.path.join(script_dir, "data", "account.txt")

class LoginDialog(QDialog):
    data_signal = pyqtSignal(bool)

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.hidepass_state = True
        self.register_dialog = None

        self.hidepass()
        self.ui.btn_hidepass.clicked.connect(self.hidepass)
        self.ui.btn_login.clicked.connect(self.check_UsPass)
        self.ui.btn_openregis.clicked.connect(self.regis)

    def hidepass(self):
       self.changeiconhidepass()

    def changeiconhidepass(self):
        icon = QtGui.QIcon()
        if self.hidepass_state:
            self.ui.txt_password.setEchoMode(QLineEdit.EchoMode.Password) 
            self.hidepass_state=False    
            icon.addPixmap(QtGui.QPixmap("icon//hidepass.png"))
        else:
            self.ui.txt_password.setEchoMode(QLineEdit.EchoMode.Normal)
            self.hidepass_state=True
            icon.addPixmap(QtGui.QPixmap("icon//showpass.png"))
        self.ui.btn_hidepass.setIcon(icon)

    def send_loginstate(self,data):
        self.data_signal.emit(data)

    def check_UsPass(self):
        username = self.ui.txt_username.text()
        us = mahoasha3.MaHoaSha3(username) 
        password = self.ui.txt_password.text()
        ps = mahoasha3.MaHoaSha3(password)
        if self.check_Account(us,ps):
            self.send_loginstate(True)
            return 
        else:
            message_box = QMessageBox()
            message_box.setIcon(QMessageBox.Icon.Information)  # Loại biểu tượng (Information)
            message_box.setWindowTitle('Thông báo')  # Tiêu đề
            message_box.setText('Bạn nhập sai username và password.')  # Nội dung thông báo
            message_box.setStandardButtons(QMessageBox.StandardButton.Ok)  # Các nút (OK)
            result = message_box.exec()  # Hiển thị hộp thoại và chờ đợi phản hồi từ người dùng
            self.ui.txt_password.setFocus()

    def check_Account(self,us,ps):
        with open(account_file_path, "r", encoding='utf-8') as file:
            for line in file:
                if line.strip() == us+","+ps:
                    return True
            return False
        

    def regis(self):
        self.register_dialog = RegisterDialog(self)
        self.register_dialog.exec()


    def set_username_password(self, username, password):
        self.ui.txt_username.setText(username)
        self.ui.txt_password.setText(password)


        
    
        
