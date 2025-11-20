from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import base64


def aes_encrypt(plaintext: str):
    key = get_random_bytes(16) 
    iv = get_random_bytes(16)

    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad(plaintext.encode(), AES.block_size))

    cipher_b64 = base64.b64encode(encrypted).decode()
    key_b64 = base64.b64encode(key).decode()
    iv_b64 = base64.b64encode(iv).decode()

    return cipher_b64, key_b64, iv_b64



text = input("Enter text to encrypt: ")

cipher, key, iv = aes_encrypt(text)

print("\n=== Encryption Result ===")
print("Ciphertext (Base64):", cipher)
print("Key        (Base64):", key)
print("IV         (Base64):", iv)
print("=========================")