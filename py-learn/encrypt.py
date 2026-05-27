import random
import string

chars = string.ascii_letters + string.digits + string.punctuation + " "

chars = list(chars)

key = chars.copy()

random.shuffle(key)

plain_text = input("Enter the text to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Original text: {plain_text}")
print(f"Encrypted text: {cipher_text}")

plain_text = ""
cipher_text = input("Enter the text to decrypt: ")

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Encrypted text: {cipher_text}")
print(f"Decrypted text: {plain_text}")
