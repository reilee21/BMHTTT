#========================
class CCeasar:
    def __init__(self, plaintext, key, ciphertext=""): #self: dùng để xác định đây là tv của lớp --> this, nên nó kh phải là parameter
        self.plaintext = plaintext
        self.key = key
        self.ciphertext=ciphertext
    #========================================
    def MaHoa(self):
        self.ciphertext=""
        for c in self.plaintext:
            if c!=' ':
                so = ord(c) - 33
                so = (so+self.key) % 65500
                self.ciphertext += chr(so+ 33)
            else:
                self.ciphertext+=c
        return self.ciphertext
    #========================================
    def GiaiMa(self):
        self.plaintext = ""
        for c in self.ciphertext:
            if c != ' ':
                so = ord(c)- 33
                so = (so - self.key + 65500) % 65500
                self.plaintext += chr(so+33)
            else:
                self.plaintext +=c
        return self.plaintext
#========================
def main():
    p =  input("Mời nhập chuỗi cần mã hóa: ")
    key = int(input("Mời nhập mã khóa: "))
    cCeasar = CCeasar(p,key)
    c = cCeasar.MaHoa()
    print("Văn bản sau khi mã hóa: ", c)
    s= cCeasar.GiaiMa()
    print("Văn bản sau khi giải mã: ",s)
#========================================
if __name__=="__main__": #entry point
    main() 
