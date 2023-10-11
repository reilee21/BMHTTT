import sys
from PyQt6.QtWidgets import QMainWindow, QApplication,QWidget
from demo1 import Ui_MainWindow

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup()

        # set state button
        self.btnBack_state = False
        self.activeButton = None      
        ###
        #[101,102,103,104] --> menu mahoa
        #[201,202,203,204] --> menu giaima
        self.curMenu = 0
       # [401,402,403,504] --> MH TT
       # []
        self.btnAction = 0
        
        


    def setup(self):
        self.ui.toolBox.setCurrentIndex(0)
        self.ui.body.hide()
        self.ui.header.hide()
        self.ui.btnBack.hide()
        self.setupMenuEvent()
        self.setupActionEvent()

    def setupMenuEvent(self):
        
        self.ui.btnMH_ThayThe.clicked.connect(lambda: self.openMenu(101))
        self.ui.btnMH_ChuyenVi.clicked.connect(lambda: self.openMenu(102))
        self.ui.btnMH_XOR.clicked.connect(lambda: self.openMenu(103))
        self.ui.btnMH_HienDai.clicked.connect(lambda: self.openMenu(104))
        self.ui.btnGM_ThayThe.clicked.connect(lambda: self.openMenu(201))
        self.ui.btnGM_ChuyenVi.clicked.connect(lambda: self.openMenu(202))
        self.ui.btnGM_XOR.clicked.connect(lambda: self.openMenu(203))
        self.ui.btnGM_HienDai.clicked.connect(lambda: self.openMenu(204))
        
        


        #####
        self.ui.btnMH_ThayThe.pressed.connect(lambda: self.setActiveButton(self.ui.btnMH_ThayThe))
        self.ui.btnMH_ChuyenVi.pressed.connect(lambda: self.setActiveButton(self.ui.btnMH_ChuyenVi))
        self.ui.btnMH_XOR.pressed.connect(lambda: self.setActiveButton(self.ui.btnMH_XOR))
        self.ui.btnMH_HienDai.pressed.connect(lambda: self.setActiveButton(self.ui.btnMH_HienDai))
        self.ui.btnGM_ThayThe.pressed.connect(lambda: self.setActiveButton(self.ui.btnGM_ThayThe))
        self.ui.btnGM_ChuyenVi.pressed.connect(lambda: self.setActiveButton(self.ui.btnGM_ChuyenVi))
        self.ui.btnGM_XOR.pressed.connect(lambda: self.setActiveButton(self.ui.btnGM_XOR))
        self.ui.btnGM_HienDai.pressed.connect(lambda: self.setActiveButton(self.ui.btnGM_HienDai))
    
    def setupActionEvent(self):
        ##Back
        self.ui.btnBack.clicked.connect(lambda: self.openMenu(self.curMenu))
        ######  5: Ui have Key  --- 6: Ui have no key
        self.ui.btn_MH_CCeasar.clicked.connect(lambda: self.action(401))
        self.ui.btn_MH_TT_Vignere.clicked.connect(lambda: self.action(402))
        self.ui.btn_MH_TT_Belassco.clicked.connect(lambda: self.action(403))
        self.ui.btn_MH_TT_Trithemius.clicked.connect(lambda: self.action(504))



    def setActiveButton(self, button):
        if self.activeButton:
            self.activeButton.setStyleSheet("QPushButton { background-color: rgb(255, 255, 255); color: rgb(0, 0, 0); font-weight: regular; QPushButton:hover { background-color: rgb(255, 255, 255); }")
        button.setStyleSheet("QPushButton { color: rgb(255, 255, 255);background-color: rgb(104, 92, 254);font:bold; }")
        self.activeButton = button

    def openMenu(self,index):        
        self.ui.body.show()
        self.ui.header.show()  
        self.ui.btnBack.hide()       

        menu = (index//100) - 1        
        kythuatmenu = (index % 100) - 1

        self.ui.label_action.setText(self.ui.toolBox.itemText(menu))        
        self.curMenu = index
        
        self.ui.label_action.setStyleSheet("font-weight: bold;")
        self.ui.stackedWidget.setCurrentIndex(kythuatmenu)
    def action(self,index):
        ui = index//100
        technique = index%100        
        if(ui ==5):
             self.ui.stackedWidget.setCurrentIndex(ui-1)
             self.ui.label_2.hide()
             self.ui.txt_Key_UIKEY.hide()
        else: self.ui.stackedWidget.setCurrentIndex(ui)
        self.ui.btnBack.show()
        
        if(technique ==1):
            self.ui.label_action.setText('Mã hoá CCeasar')
        elif(technique==2):
            self.ui.label_action.setText('Mã hoá Vignere')
        elif(technique==3):
                    self.ui.label_action.setText('Mã hoá Belasso')
        elif(technique==4):
                    self.ui.label_action.setText('Mã hoá Trithemius')

        
       



   # def checkAction(self):





def main():
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()