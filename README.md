
# Implementação de um chat cifrado em Python

Este projeto foi desenvolvido para a disciplina de Segurança em Tecnologia da Informação, do 7º semestre do curso de Ciências da Computação da Universidade de Santa Cruz do Sul. O projeto foi desenvolvido por mim e 2 colegas.

Nesta aplpicação  de uma aplicação de chat que utiliza diferentes
algoritmos criptográficos para a segurança das mensagens enviadas e recebidas,
permitindo ao usuário a seleção do algoritmo entre, Cifra de César, Vigenère, Hill,
Playfair One-time Pad, DES, 3DES e AES - sendo que estes 3 últimos possibilitam a
utilização de diversos modos de operação - e da chave, digitada em texto plano via
interface gráfica, no momento do envio de uma mensagem.

O desafio consistia em criar um sistema de troca de mensagens cifradas. Entre os requisitos havia a necessidade de implementar uma interface que permita cifrar e decifrar mensagens considerando diversos algoritmos. Após ser criptografada a mensagem deve ser enviada a um destinatário na rede que deverá conseguir decifrá-las usando a chave criptográfica. O destinatário também deve conseguir responder da mesma forma. 
A interface deve permitir ao usuário selecionar os seguintes métodos de criptografia:
* Cifra de César
* Cifra de Vigenère
* Cifra One-time pad
* Cifra Playflair
* cifra de Hill 
* Cifra DES
* Cifra 3DES (permitir ao usuário selecionar os modos: ECB,CBC,CFB,OFB,CTR)
* Cifra AES (permitir ao usuário selecionar os modos: ECB,CBC,CFB,OFB,CTR)

O código foi desenvolvido em Python 3.6
