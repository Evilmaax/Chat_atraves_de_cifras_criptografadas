from Crypto.Hill_cipher import *


def test_encrypt_decrypt():
    plaintext = "test"
    key = make_key("ddcf")
    ciphertext = encrypt(plaintext, key)
    print(ciphertext)
    decrypted = decrypt(ciphertext, key)
    print(decrypted)
    print(plaintext == decrypted)


def test_encrypt_decrypt():
    ciphertext = ""
    key = make_key("ddcf")
    decrypt(ciphertext, key)
