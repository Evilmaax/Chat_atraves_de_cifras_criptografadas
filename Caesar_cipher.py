import sys
from collections import UserList


# Object that works like a circular list that is a List type (itertools.cycle returns a generator, not a list)
# A circular list is needed in order to handle a shift of the later letters of the alphabet
class CircularList(UserList):

    def __getitem__(self, index):
        real_index = index % len(self.data)
        return super().__getitem__(real_index)


print(sys.argv)

ALPHABET = CircularList(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])


def caesar_cipher(plaintext, shift):
    output_text = ''
    for index, char in enumerate(plaintext):
        output_text += ALPHABET[ALPHABET.index(char) + shift]

    return output_text

'''
# TODO: replace the for loop with a map() function
# map(plaintext.replace())

def shifter(char):
    print(char)
    print("shifter: ", ALPHABET[ALPHABET.index(char) + shift])
    return ALPHABET[ALPHABET.index(char) + shift]


def caesar_cipher(plaintext, shift):
    output_text = ''

    output_text = map(shifter, plaintext)
    print("output_text: ", output_text)
    return output_text
'''


def main():

    if sys.argv[1] == '-h':
        print("HELP!")
    else:
        try:
            shift = int(sys.argv[1])
        except ValueError:
            print("Oops!  That was no valid number.  Try again...\n"
                  "The correct syntax is: COMMAND shift 'text to encrypt'\n"
                  "like ./python Caesar_cipher 3 'test string'")

        try:
            plaintext = sys.argv[2]
        except:
            e = sys.exc_info()[0]
            print("ERROR: ", e)
            print("ARGS: ", sys.argv)

        print('ENCRYPTED:')
        print(caesar_cipher(plaintext, shift))


if __name__ == '__main__':
    main()
