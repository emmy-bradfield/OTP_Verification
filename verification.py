import os
import math
import random
import smtplib
from time import sleep
import tkinter as tk
from dotenv import load_dotenv
load_dotenv()

KEY = os.getenv('PASS')
SENDER = os.getenv('EMAIL')
DIGITS = "0123456789"
MSG = ""
OTP = ""
OTP_IN = ''
ATTEMPTS = 3

def goodbye():
    sleep(2)
    APP.destroy()

def generate_otp(event):
    TARGET = EMAIL_INPUT.get()
    EMAIL_LABEL.destroy()
    EMAIL_INPUT.destroy()
    GENERATE.destroy()
    for i in range(6):
        global OTP
        OTP += DIGITS[math.floor(random.random()*10)]
    global MSG 
    MSG = f"Your One-Time Passcoded is {OTP}"
    MAILER = smtplib.SMTP('smtp.gmail.com', 587)
    MAILER.starttls()
    MAILER.login(SENDER, KEY)
    MAILER.sendmail('&&&&&&&&&&&', TARGET, MSG)
    OTP_LABEL = tk.Label(text="Please enter your One-Time Passcode:", bg='black', fg='white')
    OTP_LABEL.pack()
    global OTP_INPUT
    OTP_INPUT = tk.Entry()
    OTP_INPUT.pack()
    CHECK = tk.Button(text="Verify OTP", bg='black', fg='white')
    CHECK.bind("<Button-1>", validate_otp)
    CHECK.pack()
    
def validate_otp(event):
    global OTP_IN
    OTP_IN = OTP_INPUT.get()
    global ATTEMPTS
    if OTP_IN == OTP:
        CONFIRM = tk.Label(text="OTP Successfully Authorized", bg='black', fg='white')
        CONFIRM.pack()
        goodbye()
    elif ATTEMPTS > 0:
        OTP_INPUT.delete(0, tk.END)
        RETRY = tk.Label(text=f"Incorrect OTP Entered. You have {ATTEMPTS} remaining: please try again", bg='black', fg='white')
        RETRY.pack()
        ATTEMPTS -=1
    else:
        FAIL = tk.Label(text="Authorization Failed", bg='black', fg='white')
        FAIL.pack()
        goodbye()

APP = tk.Tk()
APP.configure(bg='black')
TITLE = tk.Label(text="One-Time Passcode Verification", bg='black', fg='white')
TITLE.pack()

EMAIL_LABEL = tk.Label(text="Please enter your email address", bg='black', fg='white')
EMAIL_LABEL.pack()
EMAIL_INPUT = tk.Entry(bg='black', fg='white')
EMAIL_INPUT.pack()
GENERATE = tk.Button(text="Generate OTP", bg='black', fg='white')
GENERATE.bind("<Button-1>", generate_otp)
GENERATE.pack()

APP.mainloop()