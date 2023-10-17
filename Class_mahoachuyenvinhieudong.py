import numpy as np
import math
#========================================
class CChuyenViNhieuDong:
    def __init__(self,plaintext="",key=None,ciphertext=""):
        self.plaintext=plaintext
        self.key=key
        self.ciphertext=ciphertext
    #========================================
    #========================================
    def TimViTriX(self, x):
        for i in range(len(self.key)):
            if self.key[i]==x:
                return i
        return -1;
    #========================================
    def MaHoa(self):
        soCot = len(self.key)
        soDong = math.ceil(len(self.plaintext)/soCot)
        tam = []
        k=0
        for i in range(soDong):
            row = []
            for j in range(soCot):
                if k>=len(self.plaintext): row+=['*']; continue
                row+=[self.plaintext[k]]; k+=1
            tam+=[row]
        self.ciphertext = ""
        for i in range(1,len(self.key)+1,1):
            viTriCot = self.TimViTriX(i)
            for r in tam:
                self.ciphertext += r[viTriCot]
        return self.ciphertext
    #========================================
    def GiaiMa(self):
        soCot = len(self.key)
        soDong = math.ceil(len(self.ciphertext)/soCot)
        tam = np.zeros((soDong, soCot))
        i=0
        for k in range(1,len(self.key)+1,1):
            viTriCot = self.TimViTriX(k)
            for r in range(soDong):
                tam[r][viTriCot]=ord(self.ciphertext[i]); i+=1
        self.plaintext=""
        for r in tam:
            for c in r:
                self.plaintext+=chr(int(c))
        return self.plaintext.rstrip('*')
    #========================================
#========================================
def main():
    p =  input("Mời nhập chuỗi cần mã hóa: ")
    k=[3,5,6,7,2,1,4]
    obj = CChuyenViNhieuDong(p,k)
    c = obj.MaHoa()
    print("Sau khi mã hóa: ", c)
    s= obj.GiaiMa()
    print("Sau khi giải mã: ",s)
#========================================
if __name__=="__main__": #entry point
    main()






    



