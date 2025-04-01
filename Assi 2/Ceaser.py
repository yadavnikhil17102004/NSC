def caesar_cipher(text, key, mode='1'):
    result = ""

    if mode == '2':
        key = -key

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + key) % 26 + start)
        else:
            result += char

    return result

msg = input("Enter the message to encrypt or decrypt : ")
key = int(input("Enter the key: "))
mode = input("Enter mode ('encrypt(1)' or 'decrypt(2)'): ").lower()

output = caesar_cipher(msg, key, mode)
print(f"Output: {output}")

