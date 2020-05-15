from Crypto.Cipher import AES

iv = b'g\x8a;8\x08\xd4\xd9*w\xbf\xd2\xe0\xad.\xe9Q'


def ecb(chave, msg, op):
    if op == 1:
        cifra = AES.new(chave, AES.MODE_ECB)
        msg = cifra.encrypt(msg)
    else:
        decifra = AES.new(chave, AES.MODE_ECB)


def cbc(chave, msg, op):
    if op == 1:
        cifra = AES.new(chave, AES.MODE_CBC, iv)
        msg = cifra.encrypt(msg)
    else:
        decifra = AES.new(chave, AES.MODE_CBC, IV=iv)


def cfb(chave, msg, op):
    if op == 1:
        cifra = AES.new(chave, AES.MODE_CFB, iv)
        msg = cifra.encrypt(msg)
    else:
        decifra = AES.new(chave, AES.MODE_CFB, IV=iv)


def ofb(chave, msg, op):
    if op == 1:
        cifra = AES.new(chave, AES.MODE_OFB, iv)
        msg = cifra.encrypt(msg)
    else:
        decifra = AES.new(chave, AES.MODE_OFB, IV=iv)


def ctr(chave, msg, op):
    if op == 1:
        cifra = AES.new(chave, AES.MODE_CTR, nonce=b'', initial_value=iv)
        msg = cifra.encrypt(msg)
    else:
        decifra = AES.new(chave, AES.MODE_CTR, nonce=b'', initial_value=iv)