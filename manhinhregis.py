from register import Ui_Dialog
from PyQt6.QtWidgets import QDialog,QLineEdit,QMessageBox
from PyQt6 import QtGui
from mahoaclass import mahoasha3 
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
account_file_path = os.path.join(script_dir, "data", "account.txt")

class RegisterDialog(QDialog):
    def __init__(self,login_dialog):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.hidepass_state = True
        self.hiderepass_state = True
        self.login_dialog = login_dialog


        self.hidepass(self.ui.btn_hidepass,self.ui.txt_password)
        self.hiderepass(self.ui.btn_hiderepass,self.ui.txt_repassword)

        self.ui.btn_signup.clicked.connect(self.regis)
        self.ui.btn_hidepass.clicked.connect(lambda:self.hidepass(self.ui.btn_hidepass,self.ui.txt_password))
        self.ui.btn_hiderepass.clicked.connect(lambda:self.hiderepass(self.ui.btn_hiderepass,self.ui.txt_repassword))




    def hidepass(self,toggle,txtedit):
        icon = QtGui.QIcon()
        if self.hidepass_state:
            txtedit.setEchoMode(QLineEdit.EchoMode.Password) 
            self.hidepass_state=False    
            icon.addPixmap(QtGui.QPixmap("icon//hidepass.png"))
        elif not self.hidepass_state:
            txtedit.setEchoMode(QLineEdit.EchoMode.Normal)
            self.hidepass_state=True
            icon.addPixmap(QtGui.QPixmap("icon//showpass.png"))        
        toggle.setIcon(icon)

    def hiderepass(self,toggle,txtedit):
        icon = QtGui.QIcon()

        if self.hiderepass_state:
            txtedit.setEchoMode(QLineEdit.EchoMode.Password) 
            self.hiderepass_state=False    
            icon.addPixmap(QtGui.QPixmap("icon//hidepass.png"))
        else:
            txtedit.setEchoMode(QLineEdit.EchoMode.Normal)
            self.hiderepass_state=True
            icon.addPixmap(QtGui.QPixmap("icon//showpass.png"))     
        toggle.setIcon(icon)
    def regis(self):
        if self.check_signup():
            self.accept()
            self.login_dialog.set_username_password(self.ui.txt_username.text(),self.ui.txt_password.text())


    def check_signup(self):
        username = self.ui.txt_username.text()
        password = self.ui.txt_password.text()
        password2 = self.ui.txt_repassword.text()
        if(password != password2):
            message_box = QMessageBox()
            message_box.setIcon(QMessageBox.Icon.Information)  # Loại biểu tượng (Information)
            message_box.setWindowTitle('Thông báo')  # Tiêu đề
            message_box.setText('Bạn nhập password lần hai chưa đúng.')  # Nội dung thông báo
            message_box.setStandardButtons(QMessageBox.StandardButton.Ok)  # Các nút (OK)
            result = message_box.exec()  # Hiển thị hộp thoại và chờ đợi phản hồi từ người dùng
            self.ui.txt_repassword.setFocus()
            return False
        else:
            us = mahoasha3.MaHoaSha3(username)
            ps = mahoasha3.MaHoaSha3(password)            
            
            with open(account_file_path, "a", encoding='utf-8') as file:
                file.write(us+","+ps+"\n")

        return True