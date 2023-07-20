# Code for Generate otp
import pyotp, json, time

def generate_otp():
    secretkey = pyotp.random_base32()

    totp = pyotp.TOTP(secretkey)
    otp_value = totp.now()
    return secretkey, otp_value
