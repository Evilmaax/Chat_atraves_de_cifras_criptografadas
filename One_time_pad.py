import sys
from collections import UserList
import secrets


# A circular list is needed in order to handle a shift of the later letters of the alphabet
class CircularList(UserList):

    def __getitem__(self, index):
        real_index = index % len(self.data)
        return super().__getitem__(real_index)


ALPHABET = CircularList(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])


def get_key(plaintext):

    # The key must to be as long as the plaintext and composed with random characters

    key = [secrets.choice(ALPHABET) for i in range(len(plaintext))]
    print("KEY: ", key)
    return key


def encrypt(plaintext):

    ciphertext = ''
    key = get_key(plaintext)
    # print(key)

    for pointer, plain_text_char in enumerate(plaintext):
        # Locates que index of the current plain text char
        plain_text_char_index = ALPHABET.index(plain_text_char)
        # Locates que index of the current key char
        key_char_index = ALPHABET.index(key[pointer])

        # Debug trash
        # print(ALPHABET[ALPHABET.index(plain_text_char)])
        # print(ALPHABET[ALPHABET.index(key[pointer])])
        # print(ALPHABET[top_letter_index + left_letter_index])
        ciphertext += ALPHABET[plain_text_char_index + key_char_index]

    return ciphertext, key


def decrypt(ciphertext, key):

    plaintext = ''
    for pointer, ciphertext_char in enumerate(ciphertext):
        # Locates que index of the current plain text char
        ciphertext_char_index = ALPHABET.index(ciphertext_char)
        # Locates que index of the current key char
        key_char_index = ALPHABET.index(key[pointer])

        # Debug trash
        # print(ALPHABET[ALPHABET.index(ciphertext_char)])
        # print(ALPHABET[ALPHABET.index(key[pointer])])
        # print(ALPHABET[top_letter_index + left_letter_index])
        plaintext += ALPHABET[ciphertext_char_index - key_char_index]

    return plaintext


def main():
    if sys.argv[1] == '-h':
        print("HELP!")
        plaintext = 'ATTACKATDAWN'.lower()
        expected_answer = 'LXFOPVEFRNHR'

        print("Plain Text: ", plaintext)
        print("Key: ", key)
        print("Expected Answer: ", expected_answer)

        print("The actual answer:", encrypt(plaintext))

    else:
        try:
            plaintext = sys.argv[1]
        except:
            e = sys.exc_info()#[0]
            print("ERROR: ", e)
            print("ARGS: ", sys.argv)
        else:
            plaintext = plaintext.replace(" ", "").lower()
            print('ENCRYPTED:')
            print(encrypt(plaintext))


if __name__ == '__main__':
    main()
