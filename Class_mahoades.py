from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

class DESCipher:
    def __init__(self):
        # Tạo một khóa DES 8 byte ngẫu nhiên khi khởi tạo đối tượng
        self.key = get_random_bytes(8)

    def encrypt(self, plaintext):
        cipher = DES.new(self.key, DES.MODE_ECB)
        ciphertext = cipher.encrypt(plaintext)
        return ciphertext

    def decrypt(self, ciphertext):
        decipher = DES.new(self.key, DES.MODE_ECB)
        decrypted = decipher.decrypt(ciphertext)
        return decrypted

# Sử dụng class DESCipher
des_cipher = DESCipher()

plaintext = input("Mời nhập vào dữ liệu cần mã hóa: ")
plaintext_bytes = plaintext.encode('utf-8')

ciphertext = des_cipher.encrypt(plaintext_bytes)
print("Ciphertext:", ciphertext)

decrypted = des_cipher.decrypt(ciphertext)
print("Decrypted:", decrypted.decode('utf-8'))
