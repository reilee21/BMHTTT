class CXORVigenere:
    def __init__(self, plaintext, key):
        self.plaintext = plaintext
        self.key = key

    def MaHoa(self, plaintext):
        ciphertext = ""
        key_index = 0
        for char in plaintext:
            if char != ' ':
                # Mã hóa ký tự bằng phép XOR với ký tự tương ứng trong khóa
                encrypted_char = ord(char) - 65
                key_char = ord(self.key[key_index % len(self.key)]) - 65
                encrypted_char = encrypted_char ^ key_char
                ciphertext += chr(encrypted_char + 65)
                key_index += 1
            else:
                ciphertext += char
        return ciphertext


def main():
    plaintext = input("Mời nhập chuỗi cần mã hóa: ")
    key = input("Mời nhập khóa: ")

    cipher = CXORVigenere(plaintext, key)

    encrypted_text = cipher.MaHoa(plaintext)
    print("Sau khi mã hóa: ", encrypted_text)

    decrypted_text = cipher.MaHoa(encrypted_text)
    print("Sau khi giải mã: ", decrypted_text)


if __name__ == "__main__":
    main()
