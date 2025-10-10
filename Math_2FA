import base64
import hmac
import struct
import hashlib
import time

def generate_totp(secret, digits=6, time_step=30):
    # 1. Decode the Base32 secret key (like from QR)
    key = base64.b32decode(secret, casefold=True)

    # 2. Get current Unix time and divide by time step
    counter = int(time.time() // time_step)

    # 3. Pack counter as 8-byte big-endian
    msg = struct.pack(">Q", counter)

    # 4. Create HMAC-SHA1 digest
    hmac_hash = hmac.new(key, msg, hashlib.sha1).digest()

    # 5. Dynamic truncation to get 4 bytes
    offset = hmac_hash[-1] & 0x0F
    code = struct.unpack(">I", hmac_hash[offset:offset + 4])[0] & 0x7FFFFFFF

    # 6. Modulo to get a 6-digit code
    otp = code % (10 ** digits)

    # 7. Return OTP as zero-padded string
    return str(otp).zfill(digits)

# Example secret (from a QR code)

secret_key = input("Enter yout Secret key:  ")  # Enter your secret key 
totp_code = generate_totp(secret_key)

print(f"Your current TOTP code: {totp_code}")
