from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import PKCS1_OAEP

def generate_large_prime():
    key = RSA.generate(2048)
    p = key.p
    q = key.q
    return p, q

def calculate_totient(p, q):
    return (p - 1) * (q - 1)

def generate_keys(p, q):
    n = p * q
    totient = calculate_totient(p, q)
    e = 65537
    d = pow(e, -1, totient)
    public_key = RSA.construct((n, e))
    private_key = RSA.construct((n, e, d))
    return public_key, private_key

def encrypt_message(message, public_key):
    cipher = PKCS1_OAEP.new(public_key)
    ciphertext = cipher.encrypt(message)
    return ciphertext

def decrypt_message(ciphertext, private_key):
    cipher = PKCS1_OAEP.new(private_key)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

def main():
    p, q = generate_large_prime()
    print("Generated primes p and q:\n", p, q)
    
    public_key, private_key = generate_keys(p, q)
    
    message = b"Hello, RSA!"
    print("\nOriginal message:\n", message)

    encrypted_message = encrypt_message(message, public_key)
    print("\nEncrypted message:\n", encrypted_message.hex())

    decrypted_message = decrypt_message(encrypted_message, private_key)
    print("\nDecrypted message:\n", decrypted_message.decode())

    
if __name__ == "__main__":
    main()