from Crypto.Playfair_cipher import *


# Playfair Cipher Tests:

def test_verify_input_plaintext(plaintext, key):
    returned_values = verify_input_plaintext(plaintext, key)

    if not returned_values:
        print("Error (keyword is missing) in", verify_input_plaintext.__name__)
        return False

    for value in returned_values:
        for char in value:
            if char.isspace() or char.isupper():
                print(verify_input_plaintext.__name__, "function returned a character that is not supported."
                                                       "Value with error:", char)
                print("Returned values:", returned_values)
                return False
    return True


def test_verify_input_ciphertext(ciphertext, keyword):
    returned_values = verify_input_plaintext(ciphertext, keyword)

    if not returned_values:
        print("Error in", verify_input_ciphertext.__name__)
        return False

    for value in returned_values:
        for char in value:
            if char.isspace() or char.isupper():
                print(verify_input_ciphertext.__name__, "function returned a character that is not supported."
                                                        "Value with error:", char)
                print("Returned values:", returned_values)
                return False
    return True


# TODO: Add encryption parameters
def test_playfair_cipher(text_in_pairs, key_table, decrypt=False):
    cipher_in_pairs = playfair_cipher(text_in_pairs, key_table, decrypt)

    if not cipher_in_pairs:
        # Error handling inside the method
        return False

    if len(cipher_in_pairs) != len(text_in_pairs):
        print("ERROR: On function", test_playfair_cipher.__name__, end=". ")
        print("The returned list is not of the same size as the input.")
        print("text_in_pairs:", text_in_pairs)
        print("cipher_in_pairs:", cipher_in_pairs)
        return False
    return True


def test_make_key_table(key):
    ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    table = make_key_table(key)
    # print(table)
    # The table must be 5x5 and contain only lower cases letters
    if len(table) != 5:
        print(make_key_table.__name__, "function is returning a list that is not 5x5 in size.")
        return False

    for row in table:
        if len(row) != 5:
            print(make_key_table.__name__, "function is returning a list that is not 5x5 in size.")
            return False
        for char in row:
            if not char.isalpha() or not char.islower():
                print(make_key_table.__name__, "function is returning a non letter character of an upper case letter."
                                               "Value with error:", row)
                return False

            try:
                ALPHABET.remove(char)
            except ValueError:
                print("ERROR in function", make_key_table.__name__, "\nThe letter", char, "appeared more than once.")
                print("Table:")
                for i in table:
                    print(i)
                return False

    if len(ALPHABET) == 0 or not (len(ALPHABET) == 1 and ALPHABET[0] == 'j'):
        print(ALPHABET)
        print("ERROR: The table returned from the", make_key_table.__name__, "function doesn't fit the whole alphabet.")
        return False

    # Also, the table must contain every character of the key
    # I've seen this code for the same purpose and I want to test it later:
    # result = all(elem in list1 for elem in list2)
    for char in key:
        found = False

        for row in table:
            if char in row:
                found = True
        if not found:
            print("ERROR:", make_key_table.__name__, "function is returning a table that doesn't contain every letter"
                                                     "of the key. Missing character:", char)
            print("Table:")
            for row in table:
                print(row)
            return False
    return True


def test_make_pairs_from_plaintext(plaintext):
    pairs = make_pairs_from_plaintext(plaintext)

    # print(pairs)
    # NOTE: currently not checking if the plaintext is entirely allocated into the pairs
    for pair in pairs:
        # The plaintext must be separated into pair, always
        if len(pair) != 2:
            print(make_pairs_from_plaintext.__name__,
                  "function is returning something other than a pair. Value with error:", pair)
            return False
        # And the pair cannot have the same letter twice
        if pair[0] == pair[1]:
            # But if the repeated letter is the special inserted, there's no much to do...
            # This is, for example, if we have a word that (for some reason) ends up with Q and have an even length
            # In this case the algorithm would make a pair of QQ.
            if pair[0] != 'q':
                print(make_pairs_from_plaintext.__name__,
                      "function is returning a pair with repeated letters. Value with error:",
                      pair)
                return False
    return True


def test_make_pairs_from_ciphertext(ciphertext):
    ciphertext_pairs = make_pairs_from_ciphertext(ciphertext)
    #print("ciphertext_pairs:", ciphertext_pairs)
    for pair in ciphertext_pairs:
        if len(pair) != 2:
            print("THIS IS NOT A PAIR:", pair)
            return False
    return True


def test_row_rule(pair, first_element_indexes, second_element_indexes, key_table, decrypt=False):
    cipher_pair = row_rule(pair, first_element_indexes, second_element_indexes, key_table, decrypt)

    if not cipher_pair:
        # Error handling inside the function
        return False
    if len(cipher_pair) != 2:
        print("ERROR: On function", row_rule.__name__, end=". ")
        print("The returned value is not a pair.")
        print("Inputted pair:", pair)
        print("Cipher pair:", cipher_pair)
        return False
    return True


def test_column_rule(pair, key_table, first_element_indexes, second_element_indexes, decrypt=False):
    cipher_pair = column_rule(pair, key_table, first_element_indexes, second_element_indexes, decrypt)

    if not cipher_pair:
        # Error handling inside the function
        return False
    if len(cipher_pair) != 2:
        print("ERROR: On function", column_rule.__name__, end=". ")
        print("The returned value is not a pair.")
        print("Inputted pair:", pair)
        print("Cipher pair:", cipher_pair)
        return False
    return True


def test_rectangle_rule(pair, key_table, first_element_indexes, second_element_indexes):
    cipher_pair = rectangle_rule(pair, key_table, first_element_indexes, second_element_indexes)

    if not cipher_pair:
        # Error handling inside the function
        return False
    if len(cipher_pair) != 2:
        print("ERROR: On function", rectangle_rule.__name__, end=". ")
        print("The returned value is not a pair.")
        print("Inputted pair:", pair)
        print("Cipher pair:", cipher_pair)
        return False
    return True


def test_playfair_decrypt():
    # test
    pass


# # #    Verify Input    # # #
def do_verify_input_tests():
    plaintext = "tttest with some words TEST  "
    ciphertext = "prprptdtqzlroqmcazuskyzltp"
    key = "ChuCHU COM BaNaNa"

    print(test_verify_input_plaintext.__name__, "|", test_verify_input_plaintext(plaintext, key))
    print(test_verify_input_ciphertext.__name__, "|", test_verify_input_ciphertext(ciphertext, key))


# # #    Make Key Table    # # #
def do_make_key_table_tests():
    key = "chuchucombanana"
    key_table = make_key_table(key)
    expected_key_table = [['c', 'h', 'u', 'o', 'm'],
                          ['b', 'a', 'n', 'd', 'e'],
                          ['f', 'g', 'i', 'k', 'l'],
                          ['p', 'q', 'r', 's', 't'],
                          ['v', 'w', 'x', 'y', 'z']]

    # print("KEY TABLE:", key_table)
    print(test_make_key_table.__name__, "|", test_make_key_table(key))
    print("Key Table is correct:", expected_key_table == key_table)


# # #    Make Pairs    # # #
def do_make_pairs_tests():
    plaintext = "tttsestwithsomewordstest"
    plaintext_pairs = make_pairs_from_plaintext(plaintext)
    expected_plaintext_pairs = [['t', 'q'], ['t', 'q'], ['t', 's'], ['e', 's'], ['t', 'w'],
                                ['i', 't'], ['h', 's'], ['o', 'm'], ['e', 'w'], ['o', 'r'],
                                ['d', 's'], ['t', 'e'], ['s', 't']]

    # print(plaintext_pairs)
    print(make_pairs_from_plaintext.__name__, "|", test_make_pairs_from_plaintext(plaintext))
    print("Plaintext pairs are correct:", expected_plaintext_pairs == plaintext_pairs)

    # # #    Make pairs from Ciphertext    # # # #
    ciphertext = "prprptdtqzlroqmcazuskyzltp"
    ciphertext_pairs = make_pairs_from_ciphertext(ciphertext)
    expected_ciphertext_pairs = [['p', 'r'], ['p', 'r'], ['p', 't'], ['d', 't'], ['q', 'z'],
                                 ['l', 'r'], ['o', 'q'], ['m', 'c'], ['a', 'z'], ['u', 's'],
                                 ['k', 'y'], ['z', 'l'], ['t', 'p']]

    print(test_make_pairs_from_ciphertext.__name__, "|", test_make_pairs_from_ciphertext(ciphertext))
    print("Ciphertext Pairs are correct:", expected_ciphertext_pairs == ciphertext_pairs)


# # #    Rules    # # #

# # #    Row Rule in Encryption    # # #
def do_row_rule_encryption_tests():
    first_element_indexes = [0, 0]
    second_element_indexes = [0, 2]
    pair = ['c', 'u']
    key_table = [['c', 'h', 'u', 'o', 'm'],
                 ['b', 'a', 'n', 'd', 'e'],
                 ['f', 'g', 'i', 'k', 'l'],
                 ['p', 'q', 'r', 's', 't'],
                 ['v', 'w', 'x', 'y', 'z']]

    expected_pair_row = ['h', 'o']
    pair_row = row_rule(pair, first_element_indexes, second_element_indexes, key_table)

    print(row_rule.__name__, "|", test_row_rule(pair, first_element_indexes, second_element_indexes, key_table))
    print("Row Rule (encryption) is correct:", expected_pair_row == pair_row)


# # #    Row Rule in Decryption    # # #
def do_row_rule_decryption_tests():
    pair = ['p', 'r']
    first_element_indexes = [3, 0]
    second_element_indexes = [3, 2]
    key_table = [['c', 'h', 'u', 'o', 'm'],
                 ['b', 'a', 'n', 'd', 'e'],
                 ['f', 'g', 'i', 'k', 'l'],
                 ['p', 'q', 'r', 's', 't'],
                 ['v', 'w', 'x', 'y', 'z']]

    expected_pair_row = ['t', 'q']
    pair_row = row_rule(pair, first_element_indexes, second_element_indexes, key_table, decrypt=True)

    print(row_rule.__name__, "|", test_row_rule(pair, first_element_indexes, second_element_indexes, key_table,
                                                decrypt=True))
    print("Row Rule (decryption) is correct:", expected_pair_row == pair_row)


# # #    Column Rule in Encryption    # # #
def do_column_rule_encryption_tests():
    first_element_indexes = [0, 1]
    second_element_indexes = [2, 1]
    pair = ['h', 'g']
    key_table = [['c', 'h', 'u', 'o', 'm'],
                 ['b', 'a', 'n', 'd', 'e'],
                 ['f', 'g', 'i', 'k', 'l'],
                 ['p', 'q', 'r', 's', 't'],
                 ['v', 'w', 'x', 'y', 'z']]

    expected_pair_column = ['a', 'q']
    pair_column = column_rule(pair, key_table, first_element_indexes, second_element_indexes)

    print(column_rule.__name__, "|", test_column_rule(pair, key_table, first_element_indexes, second_element_indexes))
    print("Column Rule (encryption) is correct:", expected_pair_column == pair_column)


# # #    Column Rule in Decryption    # # #
def do_column_rule_decryption_tests():
    first_element_indexes = [1, 4]
    second_element_indexes = [2, 4]
    pair = ['e', 'l']
    key_table = [['c', 'h', 'u', 'o', 'm'],
                 ['b', 'a', 'n', 'd', 'e'],
                 ['f', 'g', 'i', 'k', 'l'],
                 ['p', 'q', 'r', 's', 't'],
                 ['v', 'w', 'x', 'y', 'z']]

    expected_pair_column = ['m', 'e']
    pair_column = column_rule(pair, key_table, first_element_indexes, second_element_indexes, decrypt=True)

    print(column_rule.__name__, "|", test_column_rule(pair, key_table, first_element_indexes, second_element_indexes,
                                                      decrypt=True))
    print("Column Rule (decryption) is correct:", expected_pair_column == pair_column)


# # #    Rectangle Rule in Encryption    # # #
def do_rectangle_rule_encryption_tests():
    first_element_indexes = [0, 0]
    second_element_indexes = [2, 2]
    pair = ['c', 'i']
    key_table = [['c', 'h', 'u', 'o', 'm'],
                 ['b', 'a', 'n', 'd', 'e'],
                 ['f', 'g', 'i', 'k', 'l'],
                 ['p', 'q', 'r', 's', 't'],
                 ['v', 'w', 'x', 'y', 'z']]

    expected_pair_rectangle = ['u', 'f']
    pair_rectangle = rectangle_rule(pair, key_table, first_element_indexes, second_element_indexes)

    print(rectangle_rule.__name__, "|",
          test_rectangle_rule(pair, key_table, first_element_indexes, second_element_indexes))
    print("Rectangle Rule (encryption) is correct:", expected_pair_rectangle == pair_rectangle)


# # #    Rectangle Rule in Decryption    # # #
def do_rectangle_rule_decryption_tests():
    first_element_indexes = [0, 2]
    second_element_indexes = [2, 0]
    pair = ['u', 'f']
    key_table = [['c', 'h', 'u', 'o', 'm'],
                 ['b', 'a', 'n', 'd', 'e'],
                 ['f', 'g', 'i', 'k', 'l'],
                 ['p', 'q', 'r', 's', 't'],
                 ['v', 'w', 'x', 'y', 'z']]

    expected_pair_rectangle = ['c', 'i']
    pair_rectangle = rectangle_rule(pair, key_table, first_element_indexes, second_element_indexes)

    print(rectangle_rule.__name__, "|",
          test_rectangle_rule(pair, key_table, first_element_indexes, second_element_indexes))
    print("Rectangle Rule (decryption) is correct:", expected_pair_rectangle == pair_rectangle)


# # #    Playfair Cipher Encryption    # # #
def do_playfair_cipher_tests():

    key_table = [['c', 'h', 'u', 'o', 'm'],
                 ['b', 'a', 'n', 'd', 'e'],
                 ['f', 'g', 'i', 'k', 'l'],
                 ['p', 'q', 'r', 's', 't'],
                 ['v', 'w', 'x', 'y', 'z']]

    plaintext_to_cipher_pairs = [['t', 'q'], ['t', 'q'], ['t', 's'], ['e', 's'], ['t', 'w'],
                                 ['i', 't'], ['h', 's'], ['o', 'm'], ['e', 'w'], ['o', 'r'],
                                 ['d', 's'], ['t', 'e'], ['s', 't']]
    expected_plaintext_pairs = [['t', 'q'], ['t', 'q'], ['t', 's'], ['e', 's'], ['t', 'w'],
                                ['i', 't'], ['h', 's'], ['o', 'm'], ['e', 'w'], ['o', 'r'],
                                ['d', 's'], ['t', 'e'], ['s', 't']]
    print("plaintext_to_cipher_pairs:\n", plaintext_to_cipher_pairs)
    print("expected_plaintext_pairs:\n", expected_plaintext_pairs)

    ciphertext_to_plaintext_pairs = [['p', 'r'], ['p', 'r'], ['p', 't'], ['d', 't'], ['q', 'z'],
                                     ['l', 'r'], ['o', 'q'], ['m', 'c'], ['a', 'z'], ['u', 's'],
                                     ['k', 'y'], ['z', 'l'], ['t', 'p']]
    expected_ciphertext_pairs = [['p', 'r'], ['p', 'r'], ['p', 't'], ['d', 't'], ['q', 'z'],
                                 ['l', 'r'], ['o', 'q'], ['m', 'c'], ['a', 'z'], ['u', 's'],
                                 ['k', 'y'], ['z', 'l'], ['t', 'p']]
    print("ciphertext_to_plaintext_pairs:\n", ciphertext_to_plaintext_pairs)
    print("expected_ciphertext_pairs:\n", expected_ciphertext_pairs)
    
    print(test_playfair_cipher.__name__, "(encryption) |", test_playfair_cipher(plaintext_to_cipher_pairs, key_table))
    print("Playfair Cipher (encryption) is correct:", expected_ciphertext_pairs == plaintext_to_cipher_pairs)

    print(test_playfair_cipher.__name__, "(decryption) |", test_playfair_cipher(ciphertext_to_plaintext_pairs,
                                                                                key_table, decrypt=True))
    print("Playfair Cipher (decryption) is correct:", expected_plaintext_pairs == ciphertext_to_plaintext_pairs)


def do_encrypt_tests():

    key = "ChuCHU COM BaNaNa"
    plaintext = "tttsest with some words TEST  "
    expected_ciphertext = "prprptdtqzlroqmcazuskyzltp"

    print("playfair_encrypt_test:", expected_ciphertext == encrypt(plaintext, key))


def do_decrypt_tests():

    key = "ChuCHU COM BaNaNa"
    ciphertext = "prprptdtqzlroqmcazuskyzltp"
    expected_plaintext = "tqtqtsestwithsomewordstest"

    print("playfair_decrypt_test:", expected_plaintext == decrypt(ciphertext, key))


do_verify_input_tests()
do_make_pairs_tests()
do_make_key_table_tests()

do_row_rule_encryption_tests()
do_row_rule_decryption_tests()

do_column_rule_encryption_tests()
do_column_rule_decryption_tests()

do_rectangle_rule_encryption_tests()
do_rectangle_rule_decryption_tests()

do_playfair_cipher_tests()

do_encrypt_tests()
do_decrypt_tests()
