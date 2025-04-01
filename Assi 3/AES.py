from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def pkcs7_pad(msg, block_size):
    # Calculate how much padding is needed
    padding_length = block_size - (len(msg) % block_size)
    # Create padding byte sequence (padding_length number of bytes with the value padding_length)
    padding = bytes([padding_length] * padding_length)
    return msg + padding

def pkcs7_unpad(padded_msg):
    # The last byte indicates the number of padding bytes
    padding_length = padded_msg[-1]
    # Remove the padding
    return padded_msg[:-padding_length]

def encrypt(msg, key):
    cipher = AES.new(key, AES.MODE_ECB)
    # Apply PKCS7 padding manually
    msg_padded = pkcs7_pad(msg, AES.block_size)
    ct = cipher.encrypt(msg_padded)
    return ct

def decrypt(ct, key):
    cipher = AES.new(key, AES.MODE_ECB)
    pt_padded = cipher.decrypt(ct)
    # Remove PKCS7 padding manually
    pt = pkcs7_unpad(pt_padded)
    return pt

def main():
    key = get_random_bytes(16)  # AES key size of 16 bytes (128-bit key)
    message = input("Enter the message : ")
    msg = message.encode()  # Message to encrypt

    # Encryption
    ct = encrypt(msg, key)
    print(f"AES encryption for {msg} is: {ct.hex()}")

    # Decryption
    pt = decrypt(ct, key)
    print(f"AES decryption for {ct.hex()} is: {pt.decode()}")

if __name__ == "__main__":
    main()
