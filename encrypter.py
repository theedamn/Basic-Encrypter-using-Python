import os
from cryptography.fernet import Fernet
print("Enter file location to encrypt")
loc=input()
with open(loc,'rb') as loo:
    files= loo.read()
key=Fernet.generate_key()
with open("key.txt","wb") as k:
    k.write(key)
enc=Fernet(key).encrypt(files)
with open(loc,'wb') as wr:
    wr.write(enc)
print('File encrypted')