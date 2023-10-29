from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

class CDES:
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


# Hàm kiểm tra dữ liệu có thể mã hóa thành 8 bytes hay không
def is_valid_input(plaintext):
    plaintext_bytes = plaintext.encode("utf-8")
    if len(plaintext_bytes) % 8 != 0:
        return False
    return True


def main():
    # Sử dụng class DESCipher
    des_cipher = CDES()

    # Nhập dữ liệu từ người dùng và kiểm tra tính hợp lệ
    while True:
        plaintext = input("Mời nhập vào dữ liệu cần mã hóa: ")
        if not is_valid_input(plaintext):
            print("Nội dung không đúng 8 bytes. Vui lòng nhập lại.")
        else:
            plaintext_bytes = plaintext.encode("utf-8")
            ciphertext = des_cipher.encrypt(plaintext_bytes)
            print("Ciphertext:", ciphertext)
            print("Key:", des_cipher.key)
            decrypted = des_cipher.decrypt(ciphertext)
            print("Decrypted:", decrypted.decode("utf-8"))
            break


# Gọi hàm main để thực thi chương trình
if __name__ == "__main__":
    main()
