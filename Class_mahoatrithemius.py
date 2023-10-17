#=============================================
class CTrithemius:
    def __init__(self, plaintext, ciphertext=""):
        self.plaintext=plaintext
        self.ciphertext=ciphertext
    #========================================
    def MaHoa(self):
        self.ciphertext=""
        for i in range(len(self.plaintext)):
            c = self.plaintext[i]
            if c!=' ':
                so = ord(c) - 32;
                so = (so+(i%65500)) % 65500
                self.ciphertext += chr(so+ 32)
            else:
                self.ciphertext += ' '
        return self.ciphertext
    #========================================
    def GiaiMa(self):
        self.plaintext = ""
        for i in range(len(self.ciphertext)):
            c=self.ciphertext[i]
            if c != ' ':
                so = ord(c)- 32
                so = (so - (i%65500) + 65500) % 65500
                self.plaintext += chr(so+32)
            else:
                self.plaintext += ' '
        return self.plaintext
#========================================
def main():
    p =  input("Mời nhập chuỗi cần mã hóa: ")
    cTrithemius= CTrithemius(p)
    c = cTrithemius.MaHoa()
    print("Chuỗi sau khi mã hóa: ", c)
    s= cTrithemius.GiaiMa()
    print("Chuỗi sau khi giải mã: ",s)
#========================================
if __name__=="__main__": #entry point
    main() 
