class CVigenere:
    def __init__(self, plaintext="", key="", ciphertext=""):
        self.plaintext = plaintext
        self.key = key
        self.ciphertext = ciphertext
    
    def MaHoa(self):
        self.ciphertext = ""
        for i in range(len(self.plaintext)):
            c = self.plaintext[i]
            vt_key = i % len(self.key)
            if c != ' ':
                so = ord(c) - 33
                so_key = ord(self.key[vt_key]) - 33 + 1
                so = (so + so_key) % 65500
                self.ciphertext = self.ciphertext + chr(so + 33)
            else:
                self.ciphertext = self.ciphertext + ' '
        return self.ciphertext
    
    def GiaiMa(self):
        self.plaintext = ""
        for i in range(len(self.ciphertext)):
            c = self.ciphertext[i]
            vt_key = i % len(self.key)
            if c != ' ':
                so = ord(c) - 33
                so_key = ord(self.key[vt_key]) - 33 + 1
                so = (so - so_key + 65500) % 65500
                self.plaintext = self.plaintext + chr(so + 33)
            else:
                self.plaintext = self.plaintext + ' '
        return self.plaintext

#========================================
def main():
    p =  input("Mời nhập nội dung cần mã hóa: ")
    key = input("Mời nhập key: ")
    cVigenere= CVigenere(p,key) 
    c = cVigenere.MaHoa()
    print("Sau khi mã hóa: ", c)
    s= cVigenere.GiaiMa()
    print("Sau khi giải mã: ",s)
#========================================
if __name__=="__main__": #entry point
    main()





    


    
