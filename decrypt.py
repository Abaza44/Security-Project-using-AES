from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64


def aes_decrypt(cipher_b64: str, key_b64: str, iv_b64: str):
    cipher = base64.b64decode(cipher_b64)
    key = base64.b64decode(key_b64)
    iv = base64.b64decode(iv_b64)

    cipher_obj = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher_obj.decrypt(cipher)

    return unpad(decrypted, AES.block_size).decode()



cipher_in = input("Enter Ciphertext (Base64): ")
key_in = input("Enter Key (Base64): ")
iv_in = input("Enter IV (Base64): ")

try:
    original = aes_decrypt(cipher_in, key_in, iv_in)
    print("\n Original Text:", original)
    
except Exception as e:
    print("\n Error:", e)
