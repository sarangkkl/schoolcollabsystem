# Code for Generate otp
import pyotp

def generate_otp():
    secret_key = pyotp.random_base32()
    totp = pyotp.TOTP(secret_key)
    otp = totp.now()
    return secret_key

