import pyotp
import time

def generate_otp_from_secret():
    # 1. Ask for the secret key
    # Use a standard Base32 key (e.g., 'JBSWY3DPEBLW64TMMQ======')
    secret = input("Enter your Base32 secret key: ").strip().replace(" ", "").upper()

    try:
        # 2. Initialize the TOTP object
        totp = pyotp.TOTP(secret)

        # 3. Generate and display the current code
        print(f"Current TOTP code: {totp.now()}")
        
        # Optional: Show how long until it expires
        time_remaining = 30 - (int(time.time()) % 30)
        print(f"Time remaining: {time_remaining} seconds")

    except Exception as e:
        print(f"Error: Could not generate OTP. Ensure your key is valid Base32. ({e})")

if __name__ == "__main__":
    generate_otp_from_secret()

