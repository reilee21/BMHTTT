# main.py
import sys
from manhinhchinh import ManHinhChinh
from PyQt6.QtWidgets import QMainWindow, QApplication,QDialog,QMessageBox
from manhinh2 import MyMainWindow
from manhinhlogin import LoginDialog
cur_wd = None
old_wd = None
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = ManHinhChinh()
        self.ui.setupUi(self)

def main():
    global cur_wd, app

    app = QApplication(sys.argv)
    home()
    sys.exit(app.exec())

def wd2():
    global cur_wd, old_wd
    old_wd = cur_wd
    cur_wd = MyMainWindow()
    cur_wd.show()
    cl()

    cur_wd.ui.btn_Home.clicked.connect(home)


def home():
    global cur_wd, old_wd
    old_wd = cur_wd    
    cur_wd = Main()
    cur_wd.show() 
    cur_wd.ui.pushButton.clicked.connect(login)
    if (old_wd):
        cl()
def cl():
    old_wd.close()

def login():
    global dialog
    dialog = LoginDialog()
    dialog.data_signal.connect(checklogin)
    dialog.exec()

def checklogin(data):
    global dialog
    if data:
        dialog.close()
        QMessageBox.information(None, "Thông báo", "Đăng nhập thành công.")       
        wd2()
        
        



if __name__ == "__main__":
    main()
