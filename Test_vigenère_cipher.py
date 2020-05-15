from Vigenère_cipher import *
# TODO: Try https://docs.pytest.org/en/latest/


def test_get_key(plaintext, key):
    return False


def test_vigenere_encryption(plaintext, key):
    return False


def test_vigenere_decryption(ciphertext, key):
    return False


def do_get_key_tests():
    plaintext = "attackatdawn"
    key = "lemon"
    expected_key = "lemonlemonle"
    print(test_get_key.__name__, "|", test_get_key(plaintext, key))
    print(get_key.__name__, "is correct:", expected_key == get_key(plaintext, key))


def do_test_vigenere_encryption():
    plaintext = "attackatdawn"
    key = "lemon"
    expected_ciphertext = "lxfopvefrnhr"
    print(test_vigenere_encryption.__name__, "|", test_vigenere_encryption(plaintext, key))
    print(test_vigenere_encryption.__name__, "is correct:", expected_ciphertext == vigenere_encryption(plaintext, key))


def do_test_vigenere_decryption():
    ciphertext = "lxfopvefrnhr"
    key = "lemon"
    expected_plaintext = "attackatdawn"
    print(test_vigenere_decryption.__name__, "|", test_vigenere_decryption(ciphertext, key))
    print(test_vigenere_decryption.__name__, "is correct:", expected_plaintext == vigenere_decryption(ciphertext,
                                                                                                           key))


do_get_key_tests()
do_test_vigenere_encryption()
