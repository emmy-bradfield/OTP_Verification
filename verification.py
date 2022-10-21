import os
import math
import random
import smtplib
from dotenv import load_dotenv
load_dotenv()

KEY = os.getenv('PASS')
SENDER = os.getenv('EMAIL')
DIGITS = "0123456789"
MSG = ""
ATTEMPTS = 3
VALID = False
OTP = ""

def generate_otp():
    for i in range(6):
        global OTP
        OTP += DIGITS[math.floor(random.random()*10)]

def send_OTP():
    global MSG 
    MSG = f"Your One-Time Passcoded is {OTP}"
    MAILER = smtplib.SMTP('smtp.gmail.com', 587)
    MAILER.starttls()
    MAILER.login(SENDER, KEY)
    TARGET = input("Please enter your email address: \n>>")
    MAILER.sendmail('&&&&&&&&&&&', TARGET, MSG)

if __name__ == "__main__":
    generate_otp()
    send_OTP()
    while VALID == False:
        OTP_IN = input("Enter your One-Time Passcode:\n>>")
        if OTP_IN == OTP:
            print("Account Verified")
            VALID = True
        elif ATTEMPTS > 0:
            ATTEMPTS -= 1
            print(f"Incorrect. You have {ATTEMPTS} remaining - please try again")
        else: 
            print("Verification Failed. Goodbye")
            os.kill()
            