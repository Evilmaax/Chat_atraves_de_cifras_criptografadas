from Crypto.Cipher import DES3

BLOCK_SIZE = 8
iv = b'\xbd\xbe"r\xca\x19"\xdd'


def ecb(chave, msg, op):
    if op == 1:
        cifra = DES3.new(chave, DES3.MODE_ECB)
        msg = cifra.encrypt(msg)
    else:
        decifra = DES3.new(chave, DES3.MODE_ECB)


def cbc(chave, msg, op):
    if op == 1:
        cifra = DES3.new(chave, DES3.MODE_CBC, iv)
        msg = cifra.encrypt(msg)
    else:
        decifra = DES3.new(chave, DES3.MODE_CBC, IV=iv)

def cfb(chave, msg, op):
    if op == 1:
        cifra = DES3.new(chave, DES3.MODE_CFB, iv)
        msg = cifra.encrypt(msg)
    else:
        decifra = DES3.new(chave, DES3.MODE_CFB, IV=iv)


def ofb(chave, msg, op):
    if op == 1:
        cifra = DES3.new(chave, DES3.MODE_OFB, iv)
        msg = cifra.encrypt(msg)
    else:
        decifra = DES3.new(chave, DES3.MODE_OFB, IV=iv)


def ctr(chave, msg, op):
    if op == 1:
        cifra = DES3.new(chave, DES3.MODE_CTR, nonce=b'', initial_value=iv)
        msg = cifra.encrypt(msg)
    else:
        decifra = DES3.new(chave, DES3.MODE_CTR, nonce=b'', initial_value=iv)