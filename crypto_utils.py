import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from binascii import unhexlify
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get AES key from .env (32-byte hex string)
KEY = unhexlify(os.getenv("AES_KEY"))

def encrypt_file(file_data):
    """Encrypt file using AES-CBC with random IV"""
    iv = get_random_bytes(16)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(file_data, AES.block_size))
    return iv + ciphertext

def decrypt_file(encrypted_data):
    """Decrypt file using AES-CBC"""
    iv = encrypted_data[:16]
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(encrypted_data[16:]), AES.block_size)
    return plaintext
