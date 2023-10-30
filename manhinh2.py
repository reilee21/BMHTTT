import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QFileDialog, QMessageBox
from demo2 import Ui_MainWindow
from models.baomat import DoiTuongBaoMat
from mahoaclass.mahoaceasar_class import CCeasar
from mahoaclass.mahoavignere_class import CVigenere
from mahoaclass.mahoabelasco_class import CBelasco
from mahoaclass.mahoatrithemius_class import CTrithemius
from mahoaclass.mahoachuyenvihaidong_class import CChuyenViHaiDong
from mahoaclass.mahoachuyenvinhieudong_class import CChuyenViNhieuDong
from mahoaclass.mahoaXorCeasar_class import CXORCeasar
from mahoaclass.mahoaXorvignere_class import CXORVigenere
from mahoaclass.mahoaXorbelasco_class import CXORBelasco
from mahoaclass.mahoaXortrithemius_class import CXORTrithemius
import mahoaclass.mahoaRSA
from mahoaclass.mahoaAES_class import CAES
import mahoaclass.mahoaS_DES
from mahoaclass.mahoaDES_class import CDES
from cryptography.fernet import Fernet


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup()
        ## Create DoiTuongBaoMat
        self.doituongbaomat = DoiTuongBaoMat("", "", "")

        # set state button

        self.activeMenuButton = None
        self.activeTechniqueButton = None

        ###
        # [101,102,103,104] --> menu mahoa
        # [201,202,203,204] --> menu giaima
        #####
        self.btnAction = 0
        self.curtechnique = 0

        self.menu_mapping = {
            101: "Mã hoá thay thế",
            102: "Mã hoá chuyển vị",
            103: "Mã hoá XOR",
            104: "Mã hoá hiện đại",
            201: "Giải mã thay thế ",
            202: "Giải mã chuyển vị",
            203: "Giải mã XOR",
            204: "Giải mã hiện đại",
        }

        self.action_mapping = {
            1: "Mã hoá thay thế - Ceasar",
            2: "Mã hoá thay thế - Vigenere",
            3: "Mã hoá thay thế - Belasco",
            4: "Mã hoá thay thế - Trithemius",
            5: "Mã hoá chuyển vị - Hai dòng",
            6: "Mã hoá chuyển vị - Nhiều dòng",
            7: "Mã hoá XOR - Ceasar",
            8: "Mã hoá XOR - Vigenere",
            9: "Mã hoá XOR - Belasco",
            10: "Mã hoá XOR - Trithemius",
            11: "Mã hoá Hiện đại - RSA",
            12: "Mã hoá Hiện đại - S-DES",
            13: "Mã hoá Hiện đại - DES",
            14: "Mã hoá Hiện đại - AES",
            15: "Mã hoá Hiện đại - HSA6",
            16: "Mã hoá Hiện đại - MD5",
            17: "Giải mã thay thế - Ceasar",
            18: "Giải mã thay thế - Vigenere",
            19: "Giải mã thay thế - Belasco",
            20: "Giải mã thay thế - Trithemius",
            21: "Giải mã chuyển vị - Hai dòng",
            22: "Giải mã chuyển vị - Nhiều dòng",
            23: "Giải mã XOR - Ceasar",
            24: "Giải mã XOR - Vigenere",
            25: "Giải mã XOR - Belasco",
            26: "Giải mã XOR - Trithemius",
            27: "Giải mã Hiện đại - RSA",
            28: "Giải mã Hiện đại - S-DES",
            29: "Giải mã Hiện đại - DES",
            30: "Giải mã Hiện đại - AES",
            31: "Giải mã Hiện đại - HSA6",
            32: "Giải mã Hiện đại - MD5",
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
        self.ui.btnMH_ThayThe.pressed.connect(
            lambda: self.setActiveMenuButton(self.ui.btnMH_ThayThe)
        )
        self.ui.btnMH_ChuyenVi.pressed.connect(
            lambda: self.setActiveMenuButton(self.ui.btnMH_ChuyenVi)
        )
        self.ui.btnMH_XOR.pressed.connect(
            lambda: self.setActiveMenuButton(self.ui.btnMH_XOR)
        )
        self.ui.btnMH_HienDai.pressed.connect(
            lambda: self.setActiveMenuButton(self.ui.btnMH_HienDai)
        )
        self.ui.btnGM_ThayThe.pressed.connect(
            lambda: self.setActiveMenuButton(self.ui.btnGM_ThayThe)
        )
        self.ui.btnGM_ChuyenVi.pressed.connect(
            lambda: self.setActiveMenuButton(self.ui.btnGM_ChuyenVi)
        )
        self.ui.btnGM_XOR.pressed.connect(
            lambda: self.setActiveMenuButton(self.ui.btnGM_XOR)
        )
        self.ui.btnGM_HienDai.pressed.connect(
            lambda: self.setActiveMenuButton(self.ui.btnGM_HienDai)
        )
        #### Action
        self.ui.btn_TT_Ceasar.pressed.connect(
            lambda: self.setActiveTechniqueButton(self.ui.btn_TT_Ceasar)
        )
        self.ui.btn_TT_Vigenere.pressed.connect(
            lambda: self.setActiveTechniqueButton(self.ui.btn_TT_Vigenere)
        )
        self.ui.btn_TT_Belassco.pressed.connect(
            lambda: self.setActiveTechniqueButton(self.ui.btn_TT_Belassco)
        )
        self.ui.btn_TT_Trithemius.pressed.connect(
            lambda: self.setActiveTechniqueButton(self.ui.btn_TT_Trithemius)
        )

        self.ui.btn_CV_2D.pressed.connect(
            lambda: self.setActiveTechniqueButton(self.ui.btn_CV_2D)
        )
        self.ui.btn_CV_ND.pressed.connect(
            lambda: self.setActiveTechniqueButton(self.ui.btn_CV_ND)
        )
        self.ui.btn_XOR_Ceasar.pressed.connect(
            lambda: self.setActiveTechniqueButton(self.ui.btn_XOR_Ceasar)
        )
        self.ui.btn_XOR_Vigenere.pressed.connect(
            lambda: self.setActiveTechniqueButton(self.ui.btn_XOR_Vigenere)
        )
        self.ui.btn_XOR_Belassco.pressed.connect(
            lambda: self.setActiveTechniqueButton(self.ui.btn_XOR_Belassco)
        )
        self.ui.btn_XOR_Trithemius.pressed.connect(
            lambda: self.setActiveTechniqueButton(self.ui.btn_XOR_Trithemius)
        )
        self.ui.btn_MH_HD_RSA.pressed.connect(
            lambda: self.setActiveTechniqueButton(self.ui.btn_MH_HD_RSA)
        )
        self.ui.btn_MH_HD_SDES.pressed.connect(
            lambda: self.setActiveTechniqueButton(self.ui.btn_MH_HD_SDES)
        )
        self.ui.btn_MH_HD_DES.pressed.connect(
            lambda: self.setActiveTechniqueButton(self.ui.btn_MH_HD_DES)
        )
        self.ui.btn_MH_HD_AES.pressed.connect(
            lambda: self.setActiveTechniqueButton(self.ui.btn_MH_HD_AES)
        )

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
        self.ui.btn_TT_Ceasar.clicked.connect(lambda: self.action(1))
        self.ui.btn_TT_Vigenere.clicked.connect(lambda: self.action(2))
        self.ui.btn_TT_Belassco.clicked.connect(lambda: self.action(3))
        self.ui.btn_TT_Trithemius.clicked.connect(lambda: self.action(4))
        self.ui.btn_CV_2D.clicked.connect(lambda: self.action(5))
        self.ui.btn_CV_ND.clicked.connect(lambda: self.action(6))
        self.ui.btn_XOR_Ceasar.clicked.connect(lambda: self.action(7))
        self.ui.btn_XOR_Vigenere.clicked.connect(lambda: self.action(8))
        self.ui.btn_XOR_Belassco.clicked.connect(lambda: self.action(9))
        self.ui.btn_XOR_Trithemius.clicked.connect(lambda: self.action(10))
        self.ui.btn_MH_HD_RSA.clicked.connect(lambda: self.action(11))
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
            self.activeMenuButton.setStyleSheet(
                "QPushButton { background-color: rgb(255, 255, 255); color: rgb(0, 0, 0); font-weight: regular; QPushButton:hover { background-color: rgb(255, 255, 255); }"
            )
        button.setStyleSheet(
            "QPushButton { color: rgb(255, 255, 255);background-color: rgb(104, 92, 254);font:bold; }"
        )
        self.setActiveTechniqueButton(None)
        self.activeMenuButton = button

    def setActiveTechniqueButton(self, button):
        if button:
            button.setStyleSheet(
                "QPushButton { color: rgb(255, 255, 255);background-color: rgb(0, 65, 181);font:bold; }"
            )
        if self.activeTechniqueButton:
            self.activeTechniqueButton.setStyleSheet(
                "QPushButton { background-color: rgb(255, 255, 255); color: rgb(0, 0, 0); font-weight: regular; QPushButton:hover { background-color: rgb(255, 255, 255); }"
            )
        self.activeTechniqueButton = button

    def openMenu(self, index):
        self.ui.body.show()
        self.ui.header.show()
        self.ui.stackedWidget_2.setCurrentIndex(4)
        kythuatmenu = (index % 100) - 1

        self.setText_MenuOnclick(index)

        self.ui.label.setStyleSheet("font-weight: bold;")
        self.ui.stackedWidget.setCurrentIndex(kythuatmenu)

    def setText_MenuOnclick(self, menu_code):
        menu_name = self.menu_mapping[menu_code]
        self.ui.label.setText(menu_name)

    def setText_ActionOnclick(self):
        if self.ui.toolBox.currentIndex() == 1:
            self.curtechnique += 16
        action_name = self.action_mapping[self.curtechnique]
        self.ui.label.setText(action_name)

    def action(self, technique):
        self.curtechnique = technique
        self.setText_ActionOnclick()
        self.doituongbaomat = DoiTuongBaoMat("", "", "")
        ### Setup page
        temp = 0
        if self.ui.toolBox.currentIndex() == 1:
            temp = 2
        if self.curtechnique not in [4, 5, 6, 10, 14, 20, 21, 22, 26, 30]:
            self.ui.stackedWidget_2.setCurrentIndex(0 + temp)
        else:
            self.ui.stackedWidget_2.setCurrentIndex(1 + temp)

        self.UpdateViewModel()


    def MoFile(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilters(["Text Files (*.txt)"])
        file_dialog.selectNameFilter("Text Files (*.txt)")

        filePath, _ = file_dialog.getOpenFileName(
            self, "Open Txt File", "", "Text Files (*.txt)"
        )
        if filePath:
            QMessageBox.information(self, "Thông báo", "Mở file thành công !!!")
            with open(filePath, "r", encoding="utf-8") as file:
                fileContent = file.read()
                self.doituongbaomat.truoc = fileContent
                self.setTextFromFile()

    def MoFileKey(self):
        temp = "Mở file key " + self.ui.label.text()
        file_dialog = QFileDialog()
        file_dialog.setNameFilters(["Text Files (*.txt)"])
        file_dialog.selectNameFilter("Text Files (*.txt)")

        filePath, _ = file_dialog.getOpenFileName(
            self, "Open Txt File", "", "Text Files (*.txt)"
        )
        if filePath:
            with open(filePath, "r", encoding="utf-8") as file:
                fileContent = file.read()
                self.doituongbaomat.key = fileContent
                self.setTextKeyFromFile()

    def setTextFromFile(self):
        page = self.ui.stackedWidget_2.currentIndex()
        if page == 0:
            self.ui.txt_PlainText_MH_K.setText(self.doituongbaomat.truoc)
        elif page == 1:
            self.ui.txt_PlainText_MH_0K.setText(self.doituongbaomat.truoc)
        elif page == 2:
            self.ui.txt_Cyphertext_GM_K.setText(self.doituongbaomat.truoc)
        elif page == 3:
            self.ui.txt_Cyphertext_GM_0K.setText(self.doituongbaomat.truoc)

    def setTextKeyFromFile(self):
        page = self.ui.stackedWidget_2.currentIndex()
        if page == 0:
            self.ui.txt_Key_MH_K.setText(self.doituongbaomat.key)
        else:
            self.ui.txt_Key_GM_K.setText(self.doituongbaomat.key)

    def GhiFile(self):
        temp = "Lưu File " + self.ui.label.text()
        flag = False
        file_name, _ = QFileDialog.getSaveFileName(
            self, temp, "", "Text Files (*.txt);;All Files (*)"
        )
        if file_name:
            if not file_name.endswith(".txt"):
                file_name += ".txt"
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(self.doituongbaomat.sau)
            QMessageBox.information(self, "Thông báo", temp + " thành công !!!")
            flag = True

        if (self.curtechnique not in [4, 5, 6, 10, 14, 20, 21, 22, 26, 30] and self.ui.toolBox.currentIndex() == 0):
            temp = "Lưu File Key " + self.ui.label.text()
            file_name, _ = QFileDialog.getSaveFileName(self, temp, "", "Text Files (*.txt);;All Files (*)")
            if file_name:
                with open(file_name, "w", encoding="utf-8") as file:
                    file.write(self.doituongbaomat.key)
                QMessageBox.information(self, "Thông báo", temp + " thành công !!!")
        if(flag):
            self.doituongbaomat = DoiTuongBaoMat("", "", "")
            self.UpdateViewModel()

    def UpdateTxtToObjectFromView(self):
        page = self.ui.stackedWidget_2.currentIndex()
        if page == 0:
            self.doituongbaomat.truoc = self.ui.txt_PlainText_MH_K.toPlainText()
            self.doituongbaomat.key = self.ui.txt_Key_MH_K.toPlainText()
        elif page == 1:
            self.doituongbaomat.truoc = self.ui.txt_PlainText_MH_0K.toPlainText()
        elif page == 2:
            self.doituongbaomat.truoc = self.ui.txt_Cyphertext_GM_K.toPlainText()
            self.doituongbaomat.key = self.ui.txt_Key_GM_K.toPlainText()
        elif page == 3:
            self.doituongbaomat.truoc = self.ui.txt_Cyphertext_GM_0K.toPlainText()

    def UpdateViewModel(self):
        page = self.ui.stackedWidget_2.currentIndex()
        if page == 0:
            self.ui.txt_PlainText_MH_K.setText(self.doituongbaomat.truoc)
            self.ui.txt_Cyphertext_MH_K.setText(self.doituongbaomat.sau)
            self.ui.txt_Key_MH_K.setText(self.doituongbaomat.key)
        elif page == 1:
            self.ui.txt_PlainText_MH_0K.setText(self.doituongbaomat.truoc)
            self.ui.txt_Cyphertext_MH_0K.setText(self.doituongbaomat.sau)
        elif page == 2:
            self.ui.txt_PlainText_GM_K.setText(self.doituongbaomat.sau)
            self.ui.txt_Cyphertext_GM_K.setText(self.doituongbaomat.truoc)
            self.ui.txt_Key_GM_K.setText(self.doituongbaomat.key)
        elif page == 3:
            self.ui.txt_PlainText_GM_0K.setText(self.doituongbaomat.sau)
            self.ui.txt_Cyphertext_GM_0K.setText(self.doituongbaomat.truoc)

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
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập vào Nội dung!")
            self.set_focus_1()
            return
        if self.curtechnique not in [4, 5, 6, 10, 14, 20, 21, 22, 26, 30]:
            if not self.doituongbaomat.key:
                QMessageBox.warning(self, "Lỗi", "Vui lòng nhập vào Key!")
                self.set_focus_2()
                return

        if self.curtechnique == 1 or self.curtechnique == 17:
            self.KyThuatCeasar()
        if self.curtechnique == 2 or self.curtechnique == 18:
            self.KyThuatVigenere()
        if self.curtechnique == 3 or self.curtechnique == 19:
            self.KyThuatBelasco()
        if self.curtechnique == 4 or self.curtechnique == 20:
            self.KyThuatTrithemius()
        if self.curtechnique == 5 or self.curtechnique == 21:
            self.KyThuatHaiDong()
        if self.curtechnique == 6 or self.curtechnique == 22:
            self.KyThuatNhieuDong()
        if self.curtechnique == 7 or self.curtechnique == 23:
            self.KyThuatCeasar_Xor()
        if self.curtechnique == 8 or self.curtechnique == 24:
            self.KyThuatVigenere_Xor()
        if self.curtechnique == 9 or self.curtechnique == 25:
            self.KyThuatBelasco_Xor()
        if self.curtechnique == 10 or self.curtechnique == 26:
            self.KyThuatTrithemius_Xor()
        if self.curtechnique == 11 or self.curtechnique == 27:
            self.KyThuatRSA()
        if self.curtechnique == 12 or self.curtechnique == 28:
            self.KyThuatSDES()
        if self.curtechnique == 13 or self.curtechnique == 29:
            self.KyThuatDES()
        if self.curtechnique == 14 or self.curtechnique == 30:
            self.KyThuatAES()
        self.UpdateViewModel()

        # Các hàm kỹ thuật

    def KyThuatCeasar(self):
        baomat = CCeasar('','','')
        x = self.doituongbaomat.key
        if not x.isdigit():
            QMessageBox.information(self, "Thông báo", "Key phải là số nguyên!!!")
            self.set_focus_2()
            return
        baomat.key = int(x)
        if self.curtechnique == 1:  ## mã hoá
            baomat.plaintext = self.doituongbaomat.truoc
            self.doituongbaomat.sau = baomat.MaHoa()
        else:
            baomat.ciphertext = self.doituongbaomat.truoc
            self.doituongbaomat.sau = baomat.GiaiMa()

    def KyThuatVigenere(self):
        cVigenere = CVigenere()
        cVigenere.key = self.doituongbaomat.key
        if self.curtechnique == 2:
            cVigenere.plaintext = self.doituongbaomat.truoc
            self.doituongbaomat.sau = cVigenere.MaHoa()
        else:
            cVigenere.ciphertext = self.doituongbaomat.truoc
            self.doituongbaomat.sau = cVigenere.GiaiMa()

    def KyThuatBelasco(self):
        cBelasco = CBelasco()
        cBelasco.key = self.doituongbaomat.key
        if self.curtechnique == 3:
            cBelasco.plaintext = self.doituongbaomat.truoc
            self.doituongbaomat.sau = cBelasco.MaHoa()
        else:
            cBelasco.ciphertext = self.doituongbaomat.truoc
            self.doituongbaomat.sau = cBelasco.GiaiMa()

    def KyThuatTrithemius(self):
        cTrithemius = CTrithemius("", "")
        if self.curtechnique == 4:
            cTrithemius.plaintext = self.doituongbaomat.truoc
            self.doituongbaomat.sau = cTrithemius.MaHoa()
        else:
            cTrithemius.ciphertext = self.doituongbaomat.truoc
            self.doituongbaomat.sau = cTrithemius.GiaiMa()

    def KyThuatHaiDong(self):
        cChuyenViHaiDong = CChuyenViHaiDong()
        if self.curtechnique == 5:
            cChuyenViHaiDong.plaintext = self.doituongbaomat.truoc
            self.doituongbaomat.sau = cChuyenViHaiDong.MaHoa()
        else:
            cChuyenViHaiDong.ciphertext = self.doituongbaomat.truoc
            self.doituongbaomat.sau = cChuyenViHaiDong.GiaiMa()

    def KyThuatNhieuDong(self):
        cChuyenViNhieuDong = CChuyenViNhieuDong("", [3, 5, 6, 7, 2, 1, 4], "")
        if self.curtechnique == 6:
            cChuyenViNhieuDong.plaintext = self.doituongbaomat.truoc
            self.doituongbaomat.sau = cChuyenViNhieuDong.MaHoa()
        else:
            cChuyenViNhieuDong.ciphertext = self.doituongbaomat.truoc
            self.doituongbaomat.sau = cChuyenViNhieuDong.GiaiMa()

    def KyThuatCeasar_Xor(self):
        cXORCeasar = CXORCeasar()
        x = self.doituongbaomat.key
        if not x.isdigit():
            QMessageBox.information(self, "Thông báo", "Key phải là số nguyên!!!")
            return
        cXORCeasar.key = int(x)
        if self.curtechnique == 7:
            cXORCeasar.plaintext = self.doituongbaomat.truoc
            self.doituongbaomat.sau = cXORCeasar.MaHoa(
                cXORCeasar.plaintext, cXORCeasar.key
            )
        else:
            cXORCeasar.ciphertext = self.doituongbaomat.truoc
            self.doituongbaomat.sau = cXORCeasar.MaHoa(
                cXORCeasar.ciphertext, cXORCeasar.key
            )

    def KyThuatVigenere_Xor(self):
        cXORVigenere = CXORVigenere()
        cXORVigenere.key = self.doituongbaomat.key
        if self.curtechnique == 8:
            cXORVigenere.plaintext = self.doituongbaomat.truoc
            self.doituongbaomat.sau = cXORVigenere.MaHoa()
        else:
            cXORVigenere.ciphertext = self.doituongbaomat.truoc
            self.doituongbaomat.sau = cXORVigenere.GiaiMa()

    def KyThuatBelasco_Xor(self):
        cXORBelasco = CXORBelasco()
        cXORBelasco.key = self.doituongbaomat.key
        if self.curtechnique == 9:
            cXORBelasco.plaintext = self.doituongbaomat.truoc
            self.doituongbaomat.sau = cXORBelasco.MaHoa(
                cXORBelasco.plaintext, cXORBelasco.key
            )
        else:
            cXORBelasco.ciphertext = self.doituongbaomat.truoc
            self.doituongbaomat.sau = cXORBelasco.MaHoa(
                cXORBelasco.ciphertext, cXORBelasco.key
            )

    def KyThuatTrithemius_Xor(self):
        cXORTrithemius = CXORTrithemius()
        cXORTrithemius.key = self.doituongbaomat.key
        if self.curtechnique == 10:
            cXORTrithemius.plaintext = self.doituongbaomat.truoc
            self.doituongbaomat.sau = cXORTrithemius.MaHoa(cXORTrithemius.plaintext)
        else:
            cXORTrithemius.ciphertext = self.doituongbaomat.truoc
            self.doituongbaomat.sau = cXORTrithemius.MaHoa(cXORTrithemius.ciphertext)

    def KyThuatRSA(self):
        e=65537; n=4255903; d=2480777
        if self.curtechnique == 11:
            plaintext = self.doituongbaomat.truoc
            self.doituongbaomat.sau = mahoaclass.mahoaRSA.MaHoa(plaintext,e,n)
        else:
            ciphertext = self.doituongbaomat.truoc
            self.doituongbaomat.sau = self.mahoaRSA.GiaiMa(ciphertext,d,n)
    def KyThuatSDES(self):
        if self.curtechnique == 12:
            plaintext = self.doituongbaomat.truoc
            key = self.doituongbaomat.key
            self.doituongbaomat.sau = mahoaclass.mahoaS_DES.MaHoa(plaintext,key)
        else:
            ciphertext = self.doituongbaomat.truoc
            key = self.doituongbaomat.key
            self.doituongbaomat.sau = mahoaclass.mahoaS_DES.GiaiMa(ciphertext,key)

    def KyThuatDES(self):
        cDES = CDES()
        if self.curtechnique == 13:
            self.doituongbaomat.sau = cDES.encrypt(self.doituongbaomat.truoc)
        else:
            self.doituongbaomat.sau = cDES.decrypt(self.doituongbaomat.truoc) 

    def KyThuatAES(self):
        cAES = CAES()
        cAES.key = Fernet.generate_key()
        if self.curtechnique == 14:
            cAES.plaintext = self.doituongbaomat.truoc
            self.doituongbaomat.sau = str(cAES.encrypt_text())
        else:
            cAES.ciphertext = self.doituongbaomat.truoc
            self.doituongbaomat.sau = cAES.decrypt_text()


def main():
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
