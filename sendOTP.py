import smtplib
from email.message import EmailMessage
import secrets
import time

def send_email(receiver_email, otp):
    sender_email = "adadda413@gmail.com"  # Replace with your email
    password = "nyek ttoc ryqa nifi"  # Replace with your email password

    message = EmailMessage()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "OTP for password reset"
    message.set_content(f"Your OTP is: {otp}")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.send_message(message)
def generate_otp():
    # Tạo một mã OTP ngẫu nhiên, ví dụ mã có 6 chữ số
    otp = secrets.randbelow(10**6)
    return f"{otp:06}"


def verify_otp(entered_otp, original_otp):
    return entered_otp == original_otp


if __name__ == "__main__":
    receiver_email = "reilee2104@gmail.com"  
    otp_code = generate_otp()
    send_email(receiver_email, otp_code)

    start_time = time.time()
    
    while time.time() - start_time < 180:  
        entered_otp = input("Nhập mã OTP của bạn: ")
        if verify_otp(entered_otp, otp_code):
            print("Mã OTP chính xác. Quá trình xác minh thành công.")
            break
        else:
            print("Mã OTP không chính xác. Vui lòng thử lại.")

    if time.time() - start_time >= 180:
        print("Quá thời hạn. Mã OTP đã hết hiệu lực.")
