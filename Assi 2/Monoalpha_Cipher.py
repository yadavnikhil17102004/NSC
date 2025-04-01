
import string

def monoalphabetic_cipher(char):
    alpha = {'a': 'y', 'b': 'z', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u', 'g': 't', 'h': 's', 'i': 'r', 'j': 'q', 'k': 'p', 'l': 'o', 'm': 'n',
            'n': 'm', 'o': 'l', 'p': 'k', 'q': 'j', 'r': 'i', 's': 'h', 't': 'g', 'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c', 'y': 'b', 'z': 'a'
            }
    return alpha.get(char,char)

str = input("\n Enter String..\n")
str2 = ''.join(monoalphabetic_cipher(char) for char in str)

print("\n Before encription: ", str)
print("\n After encription: ", str2, "\n")

