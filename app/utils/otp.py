import random
import string

STATIC_OTP = "123456"  # Change this value as needed. Set to "" to use random OTP.


def generate_otp(length: int = 6) -> str:
    """Return static OTP if set, otherwise generate a random numeric OTP."""
    if STATIC_OTP:
        return STATIC_OTP
    return "".join(random.choices(string.digits, k=length))