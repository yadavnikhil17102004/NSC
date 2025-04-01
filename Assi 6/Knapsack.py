from random import randint
from sympy import mod_inverse
from math import gcd

def generate_superincreasing_sequence(length):
    sequence = [randint(1, 10)]
    for _ in range(length - 1):
        sequence.append(sum(sequence) + randint(1, 10))
    return sequence

def generate_modulus(sequence):
    return sum(sequence) + randint(1, 10)

def generate_multiplier(modulus):
    while True:
        w = randint(2, modulus - 1)
        if gcd(w, modulus) == 1:  # Ensure w is coprime to modulus
            return w

def generate_public_key(private_sequence, modulus, multiplier):
    return [(multiplier * elem) % modulus for elem in private_sequence]

def encrypt_message(message, public_key):
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    ciphertext = sum(int(bit) * public_key[i] for i, bit in enumerate(binary_message))
    return ciphertext, len(binary_message)  # Return message length for proper decryption

def decrypt_message(ciphertext, private_sequence, modulus, multiplier, message_length):
    w_inverse = mod_inverse(multiplier, modulus)
    decrypted_sum = (ciphertext * w_inverse) % modulus
    
    # Solve the subset-sum problem
    decrypted_bits = ''
    for elem in reversed(private_sequence):
        if decrypted_sum >= elem:
            decrypted_bits = '1' + decrypted_bits
            decrypted_sum -= elem
        else:
            decrypted_bits = '0' + decrypted_bits
    
    # Ensure proper length (in case of padding issues)
    decrypted_bits = decrypted_bits.zfill(message_length)
    
    # Convert binary back to text
    decrypted_text = ''.join(chr(int(decrypted_bits[i:i+8], 2)) for i in range(0, len(decrypted_bits), 8))
    return decrypted_text

def main():
    length = 128  # Must be large enough to encode binary data
    private_sequence = generate_superincreasing_sequence(length)
    modulus = generate_modulus(private_sequence)
    multiplier = generate_multiplier(modulus)
    public_key = generate_public_key(private_sequence, modulus, multiplier)
    
    message = "Hello, Knapsack!"
    print("Original message:", message)
    
    ciphertext, msg_length = encrypt_message(message, public_key)
    print("Encrypted message:", ciphertext)
    
    decrypted_message = decrypt_message(ciphertext, private_sequence, modulus, multiplier, msg_length)
    print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()
