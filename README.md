
# Implementação de um chat cifrado em Python

Este projeto foi desenvolvido para a disciplina de Segurança em Tecnologia da Informação, do 7º semestre do curso de Ciências da Computação da Universidade de Santa Cruz do Sul. O projeto foi desenvolvido por mim e 2 colegas.

O desafio consistia em criar um sistema de troca de mensagens cifradas. Entre os requisitos havia a necessidade de implementar uma interface que permita cifrar e decifrar mensagens considerando diversos algoritmos. Após ser criptografada a mensagem deve ser enviada a um destinatário na rede que deverá conseguir decifrá-las usando a chave criptográfica. O destinatário também deve conseguir responder da mesma forma. 

A interface deve permitir ao usuário selecionar, além da cifra, o tamanho da chave e a própria chave. Estão disponíveis os seguintes métodos de criptografia:

* Cifra de César
* Cifra de Vigenère
* Cifra One-time pad
* Cifra Playflair
* cifra de Hill 
* Cifra DES
* Cifra 3DES (permitir ao usuário selecionar os modos: ECB,CBC,CFB,OFB,CTR)
* Cifra AES (permitir ao usuário selecionar os modos: ECB,CBC,CFB,OFB,CTR)

O código foi desenvolvido em Python 3.6
