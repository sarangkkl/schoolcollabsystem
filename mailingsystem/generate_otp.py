# Code for Generate otp
import pyotp
secret_key = pyotp.random_base32()
totp = pyotp.TOTP(secret_key)
otp = totp.now()

# Verify the entered OTP
is_valid = totp.verify(otp)

if is_valid:
    print("OTP is valid!")
else:
    print("OTP is invalid!")