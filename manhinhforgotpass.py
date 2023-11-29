from forgotpass import Ui_Dialog
from PyQt6.QtWidgets import QDialog,QLineEdit,QMessageBox
from sendOTP import send_email, generate_otp,verify_otp
import secrets
import time
from PyQt6 import QtGui
from mahoaclass import mahoasha3 
import os
import re

script_dir = os.path.dirname(os.path.abspath(__file__))
account_file_path = os.path.join(script_dir, "data", "account.txt")

class ForgotPassDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.hidepass_state = True
        self.hiderepass_state = True

        self.firsthide()
        self.ui.txt_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.ui.txt_repassword.setEchoMode(QLineEdit.EchoMode.Password)

        self.ui.btn_confirm.clicked.connect(self.validate)
        self.ui.btn_hidepass.clicked.connect(lambda:self.hidepass(self.ui.btn_hidepass,self.ui.txt_password))
        self.ui.btn_hiderepass.clicked.connect(lambda:self.hiderepass(self.ui.btn_hiderepass,self.ui.txt_repassword))
        self.email = ''
        self.us=''
        
    

    def validate(self):
        self.us = self.ui.txt_username.text()
        self.email = self.ui.txt_email.text()
        if(not self.validate1()):
           return
        if(not self.checkUsEmail()):
            self.setMS("Thông tin tài khoản không trùng khớp") 
            return
        self.setOK()
        
        self.sendOTP(self.email)


    def sendOTP(self,email):
        otp = generate_otp()   
        send_email(email, otp)
        self.setMS("Mã OTP được gửi chỉ có hiệu lực trong 3 phút.")
        self.ui.btn_confirm.hide()
        self.ui.btn_confirmotp.show()
        self.ui.btn_confirmotp.clicked.connect(lambda:self.checkOTP(otp))

    def checkOTP(self,otp_code):


        start_time = time.time()
        while time.time() - start_time < 180: 
            if verify_otp(self.ui.txt_otp.text(), otp_code):
                self.setMS("Mã OTP chính xác. Quá trình xác minh thành công.")
                self.movetoUpatePass()
                break
            else:
                self.setMS("Mã OTP không chính xác. Vui lòng thử lại.")

        if time.time() - start_time >= 180:
            self.setMS("Quá thời hạn. Mã OTP đã hết hiệu lực.")
           
    
    def movetoUpatePass(self):
        self.showPageUpdatepass()
       
        self.ui.btn_confirmpass.clicked.connect(self.updatepass)
        
    
    def updatepass(self):
        passw = self.ui.txt_password.text()
        repassw = self.ui.txt_repassword.text()
        if( passw != repassw):
            self.setMS("Mật khẩu nhập lại không trùng khớp.")
            self.ui.txt_repassword.setFocus()
            return;
        mahoaUs =  mahoasha3.MaHoaSha3(self.us)             
        with open(account_file_path, "r+", encoding="utf-8") as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                tach = line.strip().split(',')
                if len(tach) == 3 and tach[0] == mahoaUs:  
                    tach[1] = mahoasha3.MaHoaSha3(passw)  
                    line = ','.join(tach) + '\n'
                file.write(line)
        self.setMS("Cập nhật mật khẩu thành công")
        self.close()

    def checkUsEmail(self):
        with open(account_file_path, "r", encoding="utf-8") as file:
                lines = file.readlines()
                for line in lines:
                    parts = line.strip().split(',')
                    existing_usernames = []
                    existing_emails =[]

                    if len(parts) >= 3:
                        existing_usernames.append(parts[0])
                        existing_emails.append(parts[2].strip())                

                mahoaUs =  mahoasha3.MaHoaSha3(self.us)               

                for username, email in zip(existing_usernames, existing_emails):
                     if username == mahoaUs and email == self.email:                    
                         return True 
                return False


    def validate1(self):
        if(len(self.us)<3 or not self.check_email_format(self.email)):
            self.setMS("Thông tin không hợp lệ")
            return False
        return True



    def check_email_format(self,email):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if re.match(pattern, email):
            return True
        else:
            return False 
        

    def setOK(self):
            self.ui.txt_email.hide()
            self.ui.txt_username.hide()
            self.ui.label_2.hide()
            self.ui.label_5.hide()
            self.ui.txt_otp.show()

    def setMS(self, mess):
            message_box = QMessageBox()
            message_box.setIcon(QMessageBox.Icon.Information)  
            message_box.setWindowTitle('Thông báo')  
            message_box.setText(mess)  
            message_box.setStandardButtons(QMessageBox.StandardButton.Ok) 
            message_box.exec()



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

    def firsthide(self):
        self.ui.txt_otp.hide()
        self.ui.txt_password.hide()
        self.ui.txt_repassword.hide()
        self.ui.label_6.hide()
        self.ui.label_7.hide()
        self.ui.btn_hidepass.hide()
        self.ui.btn_hiderepass.hide()
        self.ui.btn_confirmotp.hide()
        self.ui.btn_confirmpass.hide()

    def showPageUpdatepass(self):
        self.ui.txt_otp.hide()
        self.ui.btn_confirmotp.hide()
        self.ui.btn_confirmpass.show()
        self.ui.txt_password.show()
        self.ui.txt_repassword.show()
        self.ui.label_6.show()
        self.ui.label_7.show()
        self.ui.btn_hidepass.show()
        self.ui.btn_hiderepass.show()