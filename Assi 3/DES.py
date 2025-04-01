from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes


def encrypt(msg, key):
    cipher = DES.new(key, DES.MODE_ECB)
    # Make sure the message is a multiple of 8 bytes (DES block size)
    # Padding the message to be 8-byte aligned
    msg = msg + b' ' * (8 - len(msg) % 8)  # Padding with spaces
    ct = cipher.encrypt(msg)
    return ct

def decrypt(ct, key):
    cipher = DES.new(key, DES.MODE_ECB)
    pt = cipher.decrypt(ct)
    return pt

def main():
    key = get_random_bytes(8)
    message = input("Enter the message: ")# Random 8-byte key
    msg = message.encode()  # Message to encrypt (must be 8-byte aligned)

    # Encryption
    ct = encrypt(msg, key)
    print(f"DES encryption for {msg} is: {ct.hex()}")

    # Decryption
    pt = decrypt(ct, key)
    print(f"DES decryption for {ct.hex()} is: {pt.decode().strip()}")
    # The strip() is to remove padding spaces

if __name__ == "__main__":
    main()
