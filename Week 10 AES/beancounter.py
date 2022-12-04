import requests
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.number import long_to_bytes, bytes_to_long


def encrypt():
    url = "http://aes.cryptohack.org/bean_counter/encrypt/"
    r = requests.get(url)
    js = r.json()
    return bytes.fromhex(js["encrypted"])

def xor(a, b):
    xored = b""
    for i in range(len(a)):
        xored += (a[i] ^ b[i]).to_bytes(1, byteorder = "big")

    return xored


f = open("29072.png", 'rb')
start = f.read(16)

encrypted = encrypt()

key = xor(start, encrypted[:16])

f.close()

f1 = open("bean_flag.png", 'wb')

rnd = len(encrypted) // 16

for i in range(rnd):
    f1.write(xor(key, encrypted[i * 16: (i + 1) * 16]))

f1.close()