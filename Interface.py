from tkinter import *
from tkinter.ttk import *
from Crypto import Caesar_cipher, One_time_pad, Playfair_cipher, Hill_cipher

'''
import des
import Three_des
import AES
'''
import Vigenère_cipher

master_key = ""

# TODO: Passar essas funções para o Main.py
def encrypt():
    # Função para encrypt a mensagem original

    text_ciphertext_message.delete("1.0", END)
    label_alert.configure(text="")

    if combo_cipher.get() == "Cesar":
        original_message = text_plaintext_message.get("1.0", END)
        original_message = original_message.replace("\n", "")
        if entry_key.get().isdigit():
            key = int(entry_key.get())
            crypted_message = Caesar_cipher.caesar_cipher(original_message, key)
            text_ciphertext_message.insert(END, crypted_message)
        else:
            label_alert.configure(text="Escreva a penas números no campo Chave");

    elif combo_cipher.get() == "Hill":
        original_message = text_plaintext_message.get("1.0", END)
        original_message = original_message.replace("\n", "")
        key = Hill_cipher.make_key(entry_key.get())
        crypted_message = Hill_cipher.encrypt(original_message, key)
        text_ciphertext_message.insert(END, crypted_message)

    elif combo_cipher.get() == "Vigenère":
        original_message = text_plaintext_message.get("1.0", END)
        original_message = original_message.replace("\n", "")
        key = entry_key.get()
        crypted_message = Vigenère_cipher.encrypt(original_message, key)
        text_ciphertext_message.insert(END, crypted_message)

    elif combo_cipher.get() == "Playfair":
        original_message = text_plaintext_message.get("1.0", END)
        original_message = original_message.replace("\n", "")
        key = entry_key.get()
        crypted_message = Playfair_cipher.encrypt(original_message, key)
        text_ciphertext_message.insert(END, crypted_message)

    elif combo_cipher.get() == "One Time Pad":
        original_message = text_plaintext_message.get("1.0", END)
        original_message = original_message.replace("\n", "")
        crypted_message, key = One_time_pad.encrypt(original_message)
        global master_key
        master_key = ''.join(key)
        text_ciphertext_message.insert(END, crypted_message)

'''
    elif combo_cipher.get() == "DES - ECB":
        original_message = text_plaintext_message.get("1.0", END)
        original_message = original_message.replace("\n", "")
        key = entry_key.get()
        crypted_message = des.ecb(key, original_message, 1)
        text_ciphertext_message.insert(END, crypted_message)

    elif combo_cipher.get() == "DES - CBC":
        original_message = text_plaintext_message.get("1.0", END)
        original_message = original_message.replace("\n", "")
        key = entry_key.get()
        crypted_message = des.cbc(key, original_message, 1)
        text_ciphertext_message.insert(END, crypted_message)

    elif combo_cipher.get() == "DES - CFB":
        original_message = text_plaintext_message.get("1.0", END)
        original_message = original_message.replace("\n", "")
        key = entry_key.get()
        crypted_message = des.cfb(key, original_message, 1)
        text_ciphertext_message.insert(END, crypted_message)

    elif combo_cipher.get() == "DES - OFB":
        original_message = text_plaintext_message.get("1.0", END)
        original_message = original_message.replace("\n", "")
        key = entry_key.get()
        crypted_message = des.ofb(key, original_message, 1)
        text_ciphertext_message.insert(END, crypted_message)

    elif combo_cipher.get() == "DES - CTR":
        original_message = text_plaintext_message.get("1.0", END)
        original_message = original_message.replace("\n", "")
        key = entry_key.get()
        crypted_message = des.ctr(key, original_message, 1)
        text_ciphertext_message.insert(END, crypted_message)

    elif combo_cipher.get() == "3DES - ECB":
        original_message = text_plaintext_message.get("1.0", END)
        original_message = original_message.replace("\n", "")
        key = entry_key.get()
        crypted_message = Three_des.ecb(key, original_message, 1)
        text_ciphertext_message.insert(END, crypted_message)

    elif combo_cipher.get() == "3DES - CBC":
        original_message = text_plaintext_message.get("1.0", END)
        original_message = original_message.replace("\n", "")
        key = entry_key.get()
        crypted_message = Three_des.cbc(key, original_message, 1)
        text_ciphertext_message.insert(END, crypted_message)

    elif combo_cipher.get() == "3DES - CFB":
        original_message = text_plaintext_message.get("1.0", END)
        original_message = original_message.replace("\n", "")
        key = entry_key.get()
        crypted_message = Three_des.cfb(key, original_message, 1)
        text_ciphertext_message.insert(END, crypted_message)

    elif combo_cipher.get() == "3DES - OFB":
        original_message = text_plaintext_message.get("1.0", END)
        original_message = original_message.replace("\n", "")
        key = entry_key.get()
        crypted_message = Three_des.ofb(key, original_message, 1)
        text_ciphertext_message.insert(END, crypted_message)

    elif combo_cipher.get() == "3DES - CTR":
        original_message = text_plaintext_message.get("1.0", END)
        original_message = original_message.replace("\n", "")
        key = entry_key.get()
        crypted_message = Three_des.ctr(key, original_message, 1)
        text_ciphertext_message.insert(END, crypted_message)

    elif combo_cipher.get() == "AES - ECB":
        original_message = text_plaintext_message.get("1.0", END)
        original_message = original_message.replace("\n", "")
        key = entry_key.get()
        crypted_message = AES.ecb(key, original_message, 1)
        text_ciphertext_message.insert(END, crypted_message)

    elif combo_cipher.get() == "AES - CBC":
        original_message = text_plaintext_message.get("1.0", END)
        original_message = original_message.replace("\n", "")
        key = entry_key.get()
        crypted_message = AES.cbc(key, original_message, 1)
        text_ciphertext_message.insert(END, crypted_message)

    elif combo_cipher.get() == "AES - CFB":
        original_message = text_plaintext_message.get("1.0", END)
        original_message = original_message.replace("\n", "")
        key = entry_key.get()
        crypted_message = AES.cfb(key, original_message, 1)
        text_ciphertext_message.insert(END, crypted_message)

    elif combo_cipher.get() == "AES - OFB":
        original_message = text_plaintext_message.get("1.0", END)
        original_message = original_message.replace("\n", "")
        key = entry_key.get()
        crypted_message = AES.ofb(key, original_message, 1)
        text_ciphertext_message.insert(END, crypted_message)

    elif combo_cipher.get() == "AES - CTR":
        original_message = text_plaintext_message.get("1.0", END)
        original_message = original_message.replace("\n", "")
        key = entry_key.get()
        crypted_message = AES.ctr(key, original_message, 1)
        text_ciphertext_message.insert(END, crypted_message)
'''
def decrypt():
    # Função para decrypt a mensagem
    text_plaintext_message.delete("1.0", END)
    label_alert.configure(text="")

    if combo_cipher.get() == "Cesar":
        crypted_message = text_ciphertext_message.get("1.0", END)
        crypted_message = crypted_message.replace("\n", "")
        if entry_key.get().isdigit():
            key = int(entry_key.get()) * -1
            original_message = Caesar_cipher.caesar_cipher(crypted_message, key)
            text_plaintext_message.insert(END, original_message)
        else:
            label_alert.configure(text="Escreva a penas números no campo Chave")

    elif combo_cipher.get() == "Hill":
        crypted_message = text_ciphertext_message.get("1.0", END)
        crypted_message = crypted_message.replace("\n", "")
        key = Hill_cipher.make_key(entry_key.get())
        original_message = Hill_cipher.decrypt(crypted_message, key)
        text_plaintext_message.insert(END, original_message)

    elif combo_cipher.get() == "Vigenère":
        crypted_message = text_ciphertext_message.get("1.0", END)
        crypted_message = crypted_message.replace("\n", "")
        key = entry_key.get()
        original_message = Vigenère_cipher.decrypt(crypted_message, key)
        text_plaintext_message.insert(END, original_message)

    elif combo_cipher.get() == "Playfair":
        crypted_message = text_ciphertext_message.get("1.0", END)
        crypted_message = crypted_message.replace("\n", "")
        key = entry_key.get()
        original_message = Playfair_cipher.decrypt(crypted_message, key)
        text_plaintext_message.insert(END, original_message)

    elif combo_cipher.get() == "One Time Pad":
        crypted_message = text_ciphertext_message.get("1.0", END)
        crypted_message = crypted_message.replace("\n", "")
        global master_key
        original_message = One_time_pad.decrypt(crypted_message, master_key)
        text_plaintext_message.insert(END, original_message)
    '''
    elif combo_cipher.get() == "DES - ECB":
        crypted_message = text_ciphertext_message.get("1.0", END)
        crypted_message = crypted_message.replace("\n", "")
        key = entry_key.get()
        original_message = des.ecb(key, crypted_message, 0)
        text_plaintext_message.insert(END, original_message)

    elif combo_cipher.get() == "DES - CBC":
        crypted_message = text_ciphertext_message.get("1.0", END)
        crypted_message = crypted_message.replace("\n", "")
        key = entry_key.get()
        original_message = des.cbc(key, crypted_message, 0)
        text_plaintext_message.insert(END, original_message)

    elif combo_cipher.get() == "DES - CFB":
        crypted_message = text_ciphertext_message.get("1.0", END)
        crypted_message = crypted_message.replace("\n", "")
        key = entry_key.get()
        original_message = des.cfb(key, crypted_message, 0)
        text_plaintext_message.insert(END, original_message)

    elif combo_cipher.get() == "DES - OFB":
        crypted_message = text_ciphertext_message.get("1.0", END)
        crypted_message = crypted_message.replace("\n", "")
        key = entry_key.get()
        original_message = des.ofb(key, crypted_message, 0)
        text_plaintext_message.insert(END, original_message)

    elif combo_cipher.get() == "DES - CTR":
        crypted_message = text_ciphertext_message.get("1.0", END)
        crypted_message = crypted_message.replace("\n", "")
        key = entry_key.get()
        original_message = des.ctr(key, crypted_message, 0)
        text_plaintext_message.insert(END, original_message)

    elif combo_cipher.get() == "3DES - ECB":
        crypted_message = text_ciphertext_message.get("1.0", END)
        crypted_message = crypted_message.replace("\n", "")
        key = entry_key.get()
        original_message = Three_des.ecb(key, crypted_message, 0)
        text_plaintext_message.insert(END, original_message)

    elif combo_cipher.get() == "3DES - CBC":
        crypted_message = text_ciphertext_message.get("1.0", END)
        crypted_message = crypted_message.replace("\n", "")
        key = entry_key.get()
        original_message = Three_des.cbc(key, crypted_message, 0)
        text_plaintext_message.insert(END, original_message)

    elif combo_cipher.get() == "3DES - CFB":
        crypted_message = text_ciphertext_message.get("1.0", END)
        crypted_message = crypted_message.replace("\n", "")
        key = entry_key.get()
        original_message = Three_des.cfb(key, crypted_message, 0)
        text_plaintext_message.insert(END, original_message)

    elif combo_cipher.get() == "3DES - OFB":
        crypted_message = text_ciphertext_message.get("1.0", END)
        crypted_message = crypted_message.replace("\n", "")
        key = entry_key.get()
        original_message = Three_des.ofb(key, crypted_message, 0)
        text_plaintext_message.insert(END, original_message)

    elif combo_cipher.get() == "3DES - CTR":
        crypted_message = text_ciphertext_message.get("1.0", END)
        crypted_message = crypted_message.replace("\n", "")
        key = entry_key.get()
        original_message = Three_des.ctr(key, crypted_message, 0)
        text_plaintext_message.insert(END, original_message)

    elif combo_cipher.get() == "AES - ECB":
        crypted_message = text_ciphertext_message.get("1.0", END)
        crypted_message = crypted_message.replace("\n", "")
        key = entry_key.get()
        original_message = AES.ecb(key, crypted_message, 0)
        text_plaintext_message.insert(END, original_message)

    elif combo_cipher.get() == "AES - CBC":
        crypted_message = text_ciphertext_message.get("1.0", END)
        crypted_message = crypted_message.replace("\n", "")
        key = entry_key.get()
        original_message = AES.cbc(key, crypted_message, 0)
        text_plaintext_message.insert(END, original_message)

    elif combo_cipher.get() == "AES - CFB":
        crypted_message = text_ciphertext_message.get("1.0", END)
        crypted_message = crypted_message.replace("\n", "")
        key = entry_key.get()
        original_message = AES.cfb(key, crypted_message, 0)
        text_plaintext_message.insert(END, original_message)

    elif combo_cipher.get() == "AES - OFB":
        crypted_message = text_ciphertext_message.get("1.0", END)
        crypted_message = crypted_message.replace("\n", "")
        key = entry_key.get()
        original_message = AES.ofb(key, crypted_message, 0)
        text_plaintext_message.insert(END, original_message)

    elif combo_cipher.get() == "AES - CTR":
        crypted_message = text_ciphertext_message.get("1.0", END)
        crypted_message = crypted_message.replace("\n", "")
        key = entry_key.get()
        original_message = AES.ctr(key, crypted_message, 0)
        text_plaintext_message.insert(END, original_message)

'''
def enviar():
    # Função para enviar mensagem criptografada
    label_key.configure("Envia mensagem cufrada")


window = Tk()
window.title("encryptor")
window.geometry('250x600')

label_cipher = Label(window, text="Cifra")
label_cipher.grid(column=0, row=0)

combo_cipher = Combobox(window, width=37)
combo_cipher['values'] = ("Cesar", "Hill", "Vigenère", "Playfair", "One Time Pad", "DES - ECB",
                          "DES - CBC", "DES - CFB", "DES - OFB", "DES - CTR","3DES - ECB", "3DES - CBC",
                          "3DES - CFB", "3DES - OFB", "3DES - CTR", "AES - ECB", "AES - CBC", "AES - CFB",
                          "AES - OFB", "AES - CTR")
combo_cipher.current(0)  # set the selected item
combo_cipher.grid(column=0, row=1)

label_key_size = Label(window, text="Tamanho da Chave")
label_key_size.grid(column=0, row=2)

combo_key_size = Combobox(window, width=37)
combo_key_size['values'] = ("128", "192", "256")
combo_key_size.current(0)  # set the selected item
combo_key_size.grid(column=0, row=3)

label_key = Label(window, text="Chave")
label_key.grid(column=0, row=4)

entry_key = Entry(window, width=40)
entry_key.grid(column=0, row=5)

label_plaintext_message = Label(window, text="Mensagem em texto plano")
label_plaintext_message.grid(column=0, row=6)

text_plaintext_message = Text(window, width=30, height=10)
text_plaintext_message.grid(column=0, row=7)

button_encrypt = Button(window, text="Encriptar", command=encrypt)
button_encrypt.grid(column=0, row=8)

label_ciphertext_message = Label(window, text="Mensagem Cifrada")
label_ciphertext_message.grid(column=0, row=9)

text_ciphertext_message = Text(window, width=30, height=10)
text_ciphertext_message.grid(column=0, row=10)


button_decrypt = Button(window, text="Decriptar", command=decrypt)
button_decrypt.grid(column=0, row=11)

button_send = Button(window, text="Enviar", command=enviar)
button_send.grid(column=0, row=12)

label_alert = Label(window, text="")
label_alert.grid(column=0, row=13)

window.mainloop()
