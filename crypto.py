import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random

BLOCK_SIZE = 16


def pad(s): return s + (BLOCK_SIZE - len(s) %
                        BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)


def unpad(s): return s[:-ord(s[len(s) - 1:])]


password = input("Enter encryption password: ")


def encrypt(raw, password):
    private_key = hashlib.sha256(password.encode("utf-8")).digest()
    raw = pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw))


def decrypt(enc, password):
    private_key = hashlib.sha256(password.encode("utf-8")).digest()
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[16:]))


name = []
f = open('cyber.txt', 'r')
while True:
    s = f.readline()
    if s != '':
        encrypted = encrypt(s, password)
        name.append(encrypted)

    if s == '':  # check file end
        break
f.close()

f = open('cyber.txt', 'w')
f.write(str(name[0]))
f.write("\n")
f.write(str(name[1]))
f.close()

# เข้ารหัสโดยใช้password + original message จะได้ secret message
# encrypted = encrypt(name[0], password)
# print(encrypted)

# ถอดรหัสโดยใช้ password ที่ใส่ไป
# decrypted = decrypt(encrypted, password)
# print(bytes.decode(decrypted))

# ทดสอบเข้าและถอดรหัส
# for i in range(len(name)):
#     print("ID:", i, name[i])
# for i in range(len(name)):
#     d = decrypt(name[i], password)
#     print(bytes.decode(d))
