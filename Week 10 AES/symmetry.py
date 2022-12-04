import requests
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.number import long_to_bytes, bytes_to_long

def encrypt_flag():
    url = "http://aes.cryptohack.org/symmetry/encrypt_flag/"
    r = requests.get(url)
    js = r.json()
    return bytes.fromhex(js["ciphertext"])

def encrypt(plaintext, iv):
    url = "http://aes.cryptohack.org/symmetry/encrypt/"
    url += plaintext.hex()
    url += "/"
    url += iv.hex()
    url += "/"
    r = requests.get(url)
    js = r.json()
    return bytes.fromhex(js["ciphertext"])

def xor(a, b):
    return long_to_bytes(bytes_to_long(a) ^ bytes_to_long(b))

res = encrypt_flag()
iv = res[:16]
flag_enc = res[16:]
l = len(flag_enc)

plaintext = b'\x00' * l

flag = xor(encrypt(plaintext, iv), flag_enc)

print(flag)