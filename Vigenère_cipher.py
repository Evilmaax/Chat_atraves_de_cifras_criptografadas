from sys import argv
from sys import exc_info
from collections import UserList


# A circular list is needed in order to handle a shift of the later letters of the alphabet
class CircularList(UserList):

    def __getitem__(self, index):
        real_index = index % len(self.data)
        return super().__getitem__(real_index)


ALPHABET = CircularList(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])


def get_key(plaintext, key):
    # Ensure the key is at least as long as the ciphertext
    while len(key) < len(plaintext):
        key = key + key

    # Truncates the key at the size of the text
    return key[0:len(plaintext)]


def vigenere_encryption(plaintext, key):

    ciphertext = ''
    key = get_key(plaintext, key)
    # print(key)

    for pointer, plain_text_char in enumerate(plaintext):
        # Locates que index of the current plain text char horizontally on the tabula recta
        top_letter_index = ALPHABET.index(plain_text_char)
        # Locates que index of the current key char vertically on the tabula recta
        left_letter_index = ALPHABET.index(key[pointer])

        # Debug trash
        # print(ALPHABET[ALPHABET.index(plain_text_char)])
        # print(ALPHABET[ALPHABET.index(key[pointer])])
        # print(ALPHABET[top_letter_index + left_letter_index])
        ciphertext += ALPHABET[top_letter_index + left_letter_index]

    return ciphertext


def vigenere_decryption(ciphertext, key):

    plaintext = ''
    key = get_key(ciphertext, key)
    # print(key)

    for pointer, ciphertext_char in enumerate(ciphertext):
        # Locates que index of the current plain text char horizontally on the tabula recta
        top_letter_index = ALPHABET.index(ciphertext_char)
        # Locates que index of the current key char vertically on the tabula recta
        left_letter_index = ALPHABET.index(key[pointer])

        # Debug trash
        # print(ALPHABET[ALPHABET.index(plain_text_char)])
        # print(ALPHABET[ALPHABET.index(key[pointer])])
        # print(ALPHABET[top_letter_index + left_letter_index])
        plaintext += ALPHABET[top_letter_index - left_letter_index]

    return plaintext


def encrypt(plaintext, key):
    key = get_key(plaintext, key)
    return vigenere_encryption(plaintext, key)


def decrypt(ciphertext, key):
    key = get_key(ciphertext, key)
    return vigenere_decryption(ciphertext, key)


def main():

    if argv[1] == '-h':
        print("HELP!")
        plaintext = 'ATTACKATDAWN'.lower()
        key = 'LEMON'.lower()
        expected_answer = 'LXFOPVEFRNHR'

        print("Plain Text: ", plaintext)
        print("Key: ", key)
        print("Expected Answer: ", expected_answer)

        print("The actual answer:", vigenere_encryption(plaintext, key))

    else:
        try:
            plaintext = argv[1]
            key = argv[2]
            print('ENCRYPTED:')
            print(vigenere_encryption(plaintext, key))
        except:
            e = exc_info()[0]
            print("ERROR: ", e)
            print("ARGS: ", argv)


if __name__ == '__main__':
    main()
