import os
from cryptography.fernet import Fernet
import binascii
print("Enter encryptedfile location to decrypt")
loc=input()
print("Enter the key")
key=input()
with open(loc,'rb') as loo:
    files= loo.read()
enc=Fernet(key).decrypt(files)
with open(loc,'wb') as wr:
    wr.write(enc)
print('File decrypted')
