from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

class CDES:
    def __init__(self, key=""):
        self.key = key

    def encrypt(self, plaintext):
        plaintext = pad(plaintext, 8)
        cipher = DES.new(self.key, DES.MODE_ECB)
        ciphertext = cipher.encrypt(plaintext)
        return ciphertext

    def decrypt(self, ciphertext):
        cipher = DES.new(self.key, DES.MODE_ECB)
        decrypted = cipher.decrypt(ciphertext)
        decrypted = unpad(decrypted, 8)
        return decrypted


if __name__ == "__main__":
    while True:
        key = input("Enter the 8-byte DES key: ").encode()
        if len(key) != 8:
            print("The key must be 8 bytes long.")
        else:
            # Initialize the DESCipher with the provided key
            des_cipher = CDES(key)
            break

    plaintext = input("Enter the data to encrypt: ")
    plaintext_bytes = plaintext.encode()

    ciphertext = des_cipher.encrypt(plaintext_bytes)
    print("Ciphertext:", ciphertext)

    decrypted = des_cipher.decrypt(ciphertext)
    print("Decrypted:", decrypted.decode())
