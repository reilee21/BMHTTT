#========================================
class CXORCeasar:
    def __init__(self, plaintext, key):
        self.plaintext = plaintext
        self.key = key

    def MaHoa(self, plaintext):
        ciphertext = ""
        for char in plaintext:
            if char !=' ':
                encrypted_char = ord(char) - 65
                encrypted_char = encrypted_char ^ self.key
                ciphertext += chr(encrypted_char+65)
            else:
                ciphertext += char
        return ciphertext
#========================================
def main():
    plaintext = input("Mời nhập chuỗi cần mã hóa: ")
    key = int(input("Mời nhập key: "))

    cipher = CXORCeasar(plaintext,key)

    encrypted_text = cipher.MaHoa(plaintext)
    print("Sau khi mã hóa: ", encrypted_text)

    decrypted_text = cipher.MaHoa(encrypted_text)
    print("Sau khi giải mã: ", decrypted_text)

#========================================

if __name__ == "__main__":
    main()
