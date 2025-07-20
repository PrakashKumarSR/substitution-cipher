import string
import random

chars=" "+string.punctuation+string.digits+string.ascii_lowercase+string.ascii_uppercase
chars=list(chars)
keys=chars.copy()

random.shuffle(keys)

#ENCRYPTION
plain_text=input("Enter the message to encrypt: ")
cipher_text=""

for letter in plain_text:
    index=chars.index(letter)
    cipher_text+=keys[index]

print(f"original message:{plain_text}")
print(f"encrpyted message:{cipher_text}")

#DECRYPTION
cipher_text=input("Enter the message to dencrypt: ")
plain_text=""

for letter in cipher_text:
    index=keys.index(letter)
    plain_text+=chars[index]

print(f"encrpyted message:{cipher_text}")
print(f"original message:{plain_text}")



