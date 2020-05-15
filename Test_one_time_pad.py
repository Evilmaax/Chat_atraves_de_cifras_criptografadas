from Crypto.One_time_pad import *


def test_get_key(plaintext):
    key = get_key(plaintext)
    if len(plaintext) == len(key):
        return True
    else:
        return False


def test_encrypt(plaintext):
    return False


def test_decrypt(ciphertext, key):
    return False


def do_test_get_key():
    plaintext = "textotesteparaonetimepad"
    print(test_get_key.__name__, "|", test_get_key(plaintext))
    print(test_get_key.__name__, "is correct:", len(get_key(plaintext)) == len(plaintext))
    print("\n"
          "======================================================================="
          "\n")


def do_test_encrypt_decrypt():
    plaintext = "textotesteparaonetimepad"
    print(test_encrypt.__name__, "|", test_encrypt(plaintext))
    ciphertext, key = encrypt(plaintext)
    print("Encrypted message:", ciphertext)
    print("Key:", key)
    print(test_decrypt.__name__, "|", test_decrypt(ciphertext, key))
    decrypted = decrypt(ciphertext, key)
    print("Decrypted message:", decrypted)
    print(test_encrypt.__name__, "is correct:", decrypted == plaintext)


do_test_get_key()
do_test_encrypt_decrypt()
