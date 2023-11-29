from register2 import Ui_Dialog
from PyQt6.QtWidgets import QDialog,QLineEdit,QMessageBox
from PyQt6 import QtGui
from mahoaclass import mahoasha3 
import os
import re

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
            username = self.ui.txt_username.text()
            password = self.ui.txt_password.text()
            self.login_dialog.set_username_password(username,password)

            
               
            message_box = QMessageBox()
            message_box.setIcon(QMessageBox.Icon.Information)  # Loại biểu tượng (Information)
            message_box.setWindowTitle('Thông báo')  # Tiêu đề
            message_box.setText('Đăng ký tài khoản thành công!')  # Nội dung thông báo
            message_box.setStandardButtons(QMessageBox.StandardButton.Ok)  # Các nút (OK)
            message_box.exec() 


    def check_signup(self):
        username = self.ui.txt_username.text()
        password = self.ui.txt_password.text()
        password2 = self.ui.txt_repassword.text()
        email = self.ui.txt_email.text()

        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Icon.Information)          
        
        if(not self.check_email_format(email)):           
            message_box.setWindowTitle('Lỗi') 
            message_box.setText('Bạn nhập sai định dạng email') 
            message_box.setStandardButtons(QMessageBox.StandardButton.Ok)  
            message_box.exec() 
            self.ui.txt_email.setFocus()
            return False
       
        if(password != password2):
           
            message_box.setWindowTitle('Lỗi') 
            message_box.setText('Password nhập lại không khớp!') 
            message_box.setStandardButtons(QMessageBox.StandardButton.Ok)  
            message_box.exec() 
            self.ui.txt_repassword.setFocus()
            return False
        else:
            with open(account_file_path, "r", encoding='utf-8') as file:
                lines = file.readlines()
                existing_usernames = [line.split(',')[0] for line in lines]
                hashed_new_username = mahoasha3.MaHoaSha3(username)
                existing_emails = [line.split(',')[1].strip() for line in lines] 

                if hashed_new_username in existing_usernames:                   
                    message_box.setWindowTitle('Lỗi')  
                    message_box.setText('Tài khoản đã tồn tại!')  
                    message_box.exec()  
                    self.ui.txt_username.setFocus()
                    return False  
                elif email in existing_emails:       
                    message_box.setWindowTitle('Lỗi')  
                    message_box.setText('Email đã tồn tại!')  
                    message_box.exec() 
                    self.ui.txt_email.setFocus()
                    return False  
                else:
                    us = mahoasha3.MaHoaSha3(username)
                    ps = mahoasha3.MaHoaSha3(password)  
    
                    with open(account_file_path, "a", encoding='utf-8') as file:
                        file.write(us + "," + ps +","+email+ "\n")
                    return True
        

    def check_email_format(self,email):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if re.match(pattern, email):
            return True
        else:
            return False 