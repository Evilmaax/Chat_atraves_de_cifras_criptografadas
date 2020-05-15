'''
Limitations:
  - Only lower case letters are allowed;
  - Vigenère doesn't decrypt an encrypted text;
  TODO: Add decryption option
        Add verbose option for running scripts
'''

from Crypto.Cipher import AES
from Crypto.Cipher import DES

key = "testtesttesttest"

iv = "testtesttesttest"

print("encrypting", )

aes = AES.new(key, AES.MODE_CBC, iv)
plaintext = 'hello world 1234'
encd = aes.encrypt(plaintext)
print("AES", encd)

key = "testtest"
iv = "testtest"
#des = DES.new(key, DES.MODE_CBC)
des = DES.new(key, DES.MODE_OFB, iv)
#cipher = DES.new(key, DES.MODE_OFB)
#plaintext = 'hello world 1234'
plaintext = key
#encd = des.encrypt(plaintext)

encd = des.decrypt(plaintext)
print("DES", encd)

#msg = cipher.iv + cipher.encrypt(plaintext)
