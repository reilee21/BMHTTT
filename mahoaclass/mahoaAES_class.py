from cryptography.fernet import Fernet
class CAES:
    def __init__(self, plaintext="", key="", ciphertext=""):
        self.plaintext = plaintext
        self.key = key
        self.ciphertext = ciphertext
    
    # Mã hóa văn bản bằng AES
    def encrypt_text(self):
        f = Fernet(self.key)
        self.ciphertext = encrypted_text = f.encrypt(self.plaintext.encode())
        return encrypted_text

    # Giải mã văn bản bằng AES
    def decrypt_text(self):
        f = Fernet(self.key)
        decrypted_text = f.decrypt(self.ciphertext).decode()
        return decrypted_text

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Ví dụ sử dụng
def Run():
    # Tạo khóa AES
    aes_key = Fernet.generate_key()# Tạo một khóa AES ngẫu nhiên

    # Văn bản gốc
    plaintext = input("Mời nhập văn bản cần mã hoá: ")

    # Tạo đối tượng
    cAES = CAES(plaintext, aes_key, "") 
    # Mã hóa văn bản
    encrypted_text = cAES.encrypt_text()
    print("Văn bản sau khi mã hoá: ", encrypted_text)

    # Giải mã văn bản
    decrypted_text = cAES.decrypt_text()
    print("Văn bản đã được giải mã: ", decrypted_text)


#=========================================
if __name__ == "__main__":
    Run()
    
