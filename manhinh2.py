import sys
from PyQt6.QtWidgets import QMainWindow, QApplication,QWidget,QFileDialog,QMessageBox
from demo2 import Ui_MainWindow
from models.baomat import DoiTuongBaoMat 
from mahoaclass.mahoaceasar_class import CCeasar

class MyMainWindow(QMainWindow):   
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup()
        ## Create DoiTuongBaoMat
        self.doituongbaomat = DoiTuongBaoMat('','','')
        

        # set state button
        
        self.activeMenuButton = None 
        self.activeTechniqueButton = None      

        ###
        #[101,102,103,104] --> menu mahoa
        #[201,202,203,204] --> menu giaima
        #####
        self.btnAction = 0
        self.curtechnique = 0

        self.menu_mapping = {   101: "Mã hoá thay thế",
                                102: "Mã hoá chuyển vị",
                                103: "Mã hoá XOR",
                                104: "Mã hoá hiện đại",
                                201: "Giải mã thay thế ",
                                202: "Giải mã chuyển vị",
                                203: "Giải mã XOR",
                                204: "Giải mã hiện đại",
                                }
       
        self.action_mapping = { 1: "Mã hoá thay thế - CCeasar",
                                2: "Mã hoá thay thế - Vignere",
                                3: "Mã hoá thay thế - Belasso",
                                4: "Mã hoá thay thế - Trithemius",
                                5: "Mã hoá chuyển vị - Hai dòng",
                                6: "Mã hoá chuyển vị - Nhiều dòng",
                                7: "Mã hoá XOR - CCeasar",
                                8: "Mã hoá XOR - Vignere",
                                9: "Mã hoá XOR - Belasso",
                                10: "Mã hoá XOR - Trithemius",
                                11: "Mã hoá Hiện đại - RSAR",
                                12: "Mã hoá Hiện đại - S-DES",
                                13: "Mã hoá Hiện dại - DES",
                                14: "Mã hoá Hiện dại - AES",
                                15: "Giải mã thay thế - CCeasar",
                                16: "Giải mã thay thế - Vignere",
                                17: "Giải mã thay thế - Belasso",
                                18: "Giải mã thay thế - Trithemius",
                                19: "Giải mã chuyển vị - Hai dòng",
                                20: "Giải mã chuyển vị - Nhiều dòng",
                                21: "Giải mã XOR - CCeasar",
                                22: "Giải mã XOR - Vignere",
                                23: "Giải mã XOR - Belasso",
                                24: "Giải mã XOR - Trithemius",
                                25: "Giải mã Hiện đại - RSAR",
                                26: "Giải mã Hiện đại - S-DES",
                                27: "Giải mã Hiện đại - DES",
                                28: "Giải mã Hiện đại - AES",
                            }
        
        


    def setup(self):
        self.ui.toolBox.setCurrentIndex(0)
        self.ui.body.hide()
        self.ui.header.hide()
        self.ui.stackedWidget_2.setCurrentIndex(4)
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
        
        #####   Menu
        self.ui.btnMH_ThayThe.pressed.connect(lambda: self.setActiveMenuButton(self.ui.btnMH_ThayThe))
        self.ui.btnMH_ChuyenVi.pressed.connect(lambda: self.setActiveMenuButton(self.ui.btnMH_ChuyenVi))
        self.ui.btnMH_XOR.pressed.connect(lambda: self.setActiveMenuButton(self.ui.btnMH_XOR))
        self.ui.btnMH_HienDai.pressed.connect(lambda: self.setActiveMenuButton(self.ui.btnMH_HienDai))
        self.ui.btnGM_ThayThe.pressed.connect(lambda: self.setActiveMenuButton(self.ui.btnGM_ThayThe))
        self.ui.btnGM_ChuyenVi.pressed.connect(lambda: self.setActiveMenuButton(self.ui.btnGM_ChuyenVi))
        self.ui.btnGM_XOR.pressed.connect(lambda: self.setActiveMenuButton(self.ui.btnGM_XOR))
        self.ui.btnGM_HienDai.pressed.connect(lambda: self.setActiveMenuButton(self.ui.btnGM_HienDai))
        #### Action
        self.ui.btn_TT_CCeasar.pressed.connect(lambda: self.setActiveTechniqueButton(self.ui.btn_TT_CCeasar))
        self.ui.btn_TT_Vignere.pressed.connect(lambda: self.setActiveTechniqueButton(self.ui.btn_TT_Vignere))
        self.ui.btn_TT_Belassco.pressed.connect(lambda: self.setActiveTechniqueButton(self.ui.btn_TT_Belassco))
        self.ui.btn_TT_Trithemius.pressed.connect(lambda: self.setActiveTechniqueButton(self.ui.btn_TT_Trithemius))

        self.ui.btn_CV_2D.pressed.connect(lambda: self.setActiveTechniqueButton(self.ui.btn_CV_2D))
        self.ui.btn_CV_ND.pressed.connect(lambda: self.setActiveTechniqueButton(self.ui.btn_CV_ND))
        self.ui.btn_XOR_CCeasar.pressed.connect(lambda: self.setActiveTechniqueButton(self.ui.btn_XOR_CCeasar))
        self.ui.btn_XOR_Vignere.pressed.connect(lambda: self.setActiveTechniqueButton(self.ui.btn_XOR_Vignere))
        self.ui.btn_XOR_Belassco.pressed.connect(lambda: self.setActiveTechniqueButton(self.ui.btn_XOR_Belassco))
        self.ui.btn_XOR_Trithemius.pressed.connect(lambda: self.setActiveTechniqueButton(self.ui.btn_XOR_Trithemius))
        self.ui.btn_MH_HD_RSAR.pressed.connect(lambda: self.setActiveTechniqueButton(self.ui.btn_MH_HD_RSAR))
        self.ui.btn_MH_HD_SDES.pressed.connect(lambda: self.setActiveTechniqueButton(self.ui.btn_MH_HD_SDES))
        self.ui.btn_MH_HD_DES.pressed.connect(lambda: self.setActiveTechniqueButton(self.ui.btn_MH_HD_DES))
        self.ui.btn_MH_HD_AES.pressed.connect(lambda: self.setActiveTechniqueButton(self.ui.btn_MH_HD_AES))
    
    def setupActionEvent(self):

        ### đọc ghi file
        self.ui.btn_Import_MH_K.clicked.connect(self.MoFile)
        self.ui.btn_Import_MH_0K.clicked.connect(self.MoFile)
        self.ui.btn_Import_GM_0K.clicked.connect(self.MoFile)
        self.ui.btn_Import_GM_K.clicked.connect(self.MoFile)
        self.ui.btn_Import_GM_K_Key.clicked.connect(self.MoFileKey)

        self.ui.btn_Save_MH_K.clicked.connect(self.GhiFile)
        self.ui.btn_Save_GM_K.clicked.connect(self.GhiFile)
        self.ui.btn_Save_MH_0K.clicked.connect(self.GhiFile)
        self.ui.btn_Save_GM_0K.clicked.connect(self.GhiFile)


        ### Chọn kỹ thuật 
        self.ui.btn_TT_CCeasar.clicked.connect(lambda: self.action(1))
        self.ui.btn_TT_Vignere.clicked.connect(lambda: self.action(2))
        self.ui.btn_TT_Belassco.clicked.connect(lambda: self.action(3))
        self.ui.btn_TT_Trithemius.clicked.connect(lambda: self.action(4))
        self.ui.btn_CV_2D.clicked.connect(lambda: self.action(5))
        self.ui.btn_CV_ND.clicked.connect(lambda: self.action(6))
        self.ui.btn_XOR_CCeasar.clicked.connect(lambda: self.action(7))
        self.ui.btn_XOR_Vignere.clicked.connect(lambda: self.action(8))
        self.ui.btn_XOR_Belassco.clicked.connect(lambda: self.action(9))
        self.ui.btn_XOR_Trithemius.clicked.connect(lambda: self.action(10))
        self.ui.btn_MH_HD_RSAR.clicked.connect(lambda: self.action(11))
        self.ui.btn_MH_HD_SDES.clicked.connect(lambda: self.action(12))
        self.ui.btn_MH_HD_DES.clicked.connect(lambda: self.action(13))
        self.ui.btn_MH_HD_AES.clicked.connect(lambda: self.action(14))

        ### sự kiện cho btn mã hoá và btn giải mã
        self.ui.btn_MH_K.clicked.connect(self.ThucHienMH_GM)
        self.ui.btn_GM_K.clicked.connect(self.ThucHienMH_GM)
        self.ui.btn_MH_0K.clicked.connect(self.ThucHienMH_GM)
        self.ui.btn_GM_0K.clicked.connect(self.ThucHienMH_GM)

    

    def setActiveMenuButton(self, button):
        if self.activeMenuButton:
            self.activeMenuButton.setStyleSheet("QPushButton { background-color: rgb(255, 255, 255); color: rgb(0, 0, 0); font-weight: regular; QPushButton:hover { background-color: rgb(255, 255, 255); }")
        button.setStyleSheet("QPushButton { color: rgb(255, 255, 255);background-color: rgb(104, 92, 254);font:bold; }")
        self.setActiveTechniqueButton(None)
        self.activeMenuButton = button
    def setActiveTechniqueButton(self, button):
        if button:
            button.setStyleSheet("QPushButton { color: rgb(255, 255, 255);background-color: rgb(0, 65, 181);font:bold; }")           
        if self.activeTechniqueButton:
            self.activeTechniqueButton.setStyleSheet("QPushButton { background-color: rgb(255, 255, 255); color: rgb(0, 0, 0); font-weight: regular; QPushButton:hover { background-color: rgb(255, 255, 255); }")
        self.activeTechniqueButton = button

    def openMenu(self,index):        
        self.ui.body.show()
        self.ui.header.show()  
        self.ui.stackedWidget_2.setCurrentIndex(4)        
        kythuatmenu = (index % 100) - 1

        self.setText_MenuOnclick(index)       
        
        self.ui.label.setStyleSheet("font-weight: bold;")
        self.ui.stackedWidget.setCurrentIndex(kythuatmenu)

    def setText_MenuOnclick(self,menu_code):
        menu_name = self.menu_mapping[menu_code]
        self.ui.label.setText(menu_name)
    def setText_ActionOnclick(self):

        if(self.ui.toolBox.currentIndex()==1):
            self.curtechnique+=14
        action_name = self.action_mapping[self.curtechnique]
        self.ui.label.setText(action_name)

    def action(self,technique): 
        self.curtechnique = technique       
        self.setText_ActionOnclick()
        self.doituongbaomat = DoiTuongBaoMat('','','')
        self.UpdateViewModel()
        ### Setup page
        temp = 0
        if (self.ui.toolBox.currentIndex()==1):
            temp = 2
        if self.curtechnique not in [4, 5, 10, 18, 19, 24]:
            self.ui.stackedWidget_2.setCurrentIndex(0 + temp)
        else:
            self.ui.stackedWidget_2.setCurrentIndex(1 + temp)
             
    def MoFile(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Mở file văn bản", "",
                                                  "Text Files (*.txt);;All Files (*)")
        if filePath:            
            with open(filePath, 'r', encoding='utf-8') as file:
                fileContent = file.read()
                self.doituongbaomat.truoc = fileContent
                self.setTextFromFile()
               # self.txtPlaintext.setPlainText(fileContent)
   
    def MoFileKey(self):
            temp = "Mở file key "+ self.ui.label.text()
            filePath, _ = QFileDialog.getOpenFileName(self, temp, "",
                                                    "Text Files (*.txt);;All Files (*)")
            if filePath:            
                with open(filePath, 'r', encoding='utf-8') as file:
                    fileContent = file.read()
                    self.doituongbaomat.key = fileContent
                    self.setTextKeyFromFile()
    
    def setTextFromFile(self):
        page = self.ui.stackedWidget_2.currentIndex()
        if(page == 0):
            self.ui.txt_PlainText_MH_K.setText(self.doituongbaomat.truoc)
        elif(page == 1):
            self.ui.txt_PlainText_MH_0K.setText(self.doituongbaomat.truoc)
        elif(page == 2):
            self.ui.txt_Cyphertext_GM_K.setText(self.doituongbaomat.truoc)
        elif(page ==3):
            self.ui.txt_Cyphertext_GM_0K.setText(self.doituongbaomat.truoc)

    def setTextKeyFromFile(self):
        page = self.ui.stackedWidget_2.currentIndex()  
        if(page == 0):
            self.ui.txt_Key_MH_K.setText(self.doituongbaomat.key)
        else:
            self.ui.txt_Key_GM_K.setText(self.doituongbaomat.key)

    def GhiFile(self):
        temp = "Lưu File "+ self.ui.label.text()        
        file_name, _ = QFileDialog.getSaveFileName(self,temp, "",
                                                  "Text Files (*.txt);;All Files (*)")
        if file_name:
            if not file_name.endswith(".txt"):
              file_name += ".txt"
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(self.doituongbaomat.sau)
            QMessageBox.information(self, "Thông báo", temp+" thành công !!!")
        
        if self.curtechnique not in [4, 5, 10, 18, 19, 24] and self.ui.toolBox.currentIndex() == 0:
            temp = "Lưu File Key "+ self.ui.label.text()
            # Lưu file KEY
            file_name, _ = QFileDialog.getSaveFileName(self, temp, "",
                                                    "Text Files (*.txt);;All Files (*)")
            if file_name:
                with open(file_name, 'w', encoding='utf-8') as file:
                    file.write(self.doituongbaomat.key)
                QMessageBox.information(self, "Thông báo",  temp+" thành công !!!")

    def UpdateTxtToObjectFromView(self):
        page = self.ui.stackedWidget_2.currentIndex()
        if(page == 0):
            self.doituongbaomat.truoc = self.ui.txt_PlainText_MH_K.toPlainText()
            self.doituongbaomat.key = self.ui.txt_Key_MH_K.toPlainText()
        elif(page == 1):
            self.doituongbaomat.truoc = self.ui.txt_PlainText_MH_0K.toPlainText()
        elif(page == 2):
            self.doituongbaomat.truoc = self.ui.txt_Cyphertext_GM_K.toPlainText()
            self.doituongbaomat.key = self.ui.txt_Key_GM_K.toPlainText()
        elif(page ==3):
            self.doituongbaomat.truoc = self.ui.txt_Cyphertext_GM_0K.toPlainText()
    def UpdateViewModel(self):
        page = self.ui.stackedWidget_2.currentIndex()
        if(page == 0):
            self.ui.txt_PlainText_MH_K.setText(self.doituongbaomat.truoc)
            self.ui.txt_Cyphertext_MH_K.setText(self.doituongbaomat.sau)
            self.ui.txt_Key_MH_K.setText(self.doituongbaomat.key)
        elif(page == 1):
            self.ui.txt_PlainText_MH_0K.setText(self.doituongbaomat.truoc)
            self.ui.txt_Cyphertext_MH_0K.setText(self.doituongbaomat.sau)
        elif(page == 2):
             self.ui.txt_PlainText_GM_K.setText(self.doituongbaomat.sau)
             self.ui.txt_Cyphertext_GM_K.setText(self.doituongbaomat.truoc)
             self.ui.txt_Key_GM_K.setText(self.doituongbaomat.key)
        elif(page ==3):
            self.ui.txt_PlainText_GM_0K.setText(self.doituongbaomat.truoc)
            self.ui.txt_Cyphertext_GM_0K.setText(self.doituongbaomat.sau)


    def set_focus_1(self):
        page = self.ui.stackedWidget_2.currentIndex()
        if page == 0:
            self.ui.txt_PlainText_MH_K.setFocus()
        elif page == 1:
            self.ui.txt_PlainText_MH_0K.setFocus()
        elif page == 2:
            self.ui.txt_Cyphertext_GM_K.setFocus()
        elif page == 3:
            self.ui.txt_Cyphertext_GM_0K.setFocus()

    def set_focus_2(self):
        page = self.ui.stackedWidget_2.currentIndex()
        if page == 0:
            self.ui.txt_Key_MH_K.setFocus()
        elif page == 2:
            self.ui.txt_Key_GM_K.setFocus()


    def ThucHienMH_GM(self):   
        self.UpdateTxtToObjectFromView()
        if not self.doituongbaomat.truoc:
            QMessageBox.information(self, "Thông báo", "Bạn chưa nhập văn bản!!!")
            self.set_focus_1()
            return
        if self.curtechnique not in [4, 5, 10, 18, 19, 24]:
            if not self.doituongbaomat.key:
                QMessageBox.information(self, "Thông báo", "Bạn chưa nhập key!!!")
                self.set_focus_2()
                return
        
        if self.curtechnique == 1 or self.curtechnique == 15:
            self.KyThuatCCeasar()       
        ##### code tiếp tục cho các kỹ thuật còn lại ---> tạo hàm riêng cho mỗi kỹ thuật
        self.UpdateViewModel()


    ####   hàm kỹ thuật
    def KyThuatCCeasar(self):
        baomat = CCeasar("","","")
        x = self.doituongbaomat.key
        if not x.isdigit():
            QMessageBox.information(self, "Thông báo", "Key phải là số nguyên!!!")                
            return
        baomat.key = int(x)
        if(self.curtechnique==1):## mã hoá
            baomat.plaintext = self.doituongbaomat.truoc            
            self.doituongbaomat.sau = baomat.MaHoa()
        else:
            baomat.ciphertext = self.doituongbaomat.truoc
            self.doituongbaomat.sau = baomat.GiaiMa()

    

def main():
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()