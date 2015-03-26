# -*- coding: utf-8 -*-
 #usando o turtle primeiro precisa desenhar a forca por meio de funções, depois faz o sorteio das palavras

import turtle               # Usa a biblioteca de turtle graphics
window = turtle.Screen()    # cria uma janela
window.bgcolor("lightblue")
window.title("Poligonos")

from random import choice

arquivo = open (')

palavras=open("entrada.txt", encoding="utf-8")
ler=palavras.redlines()
lista=[]
for i in ler:
    linha=i.strip()
    if linha!="":
        lista.append(linha)
from random import choice
sorteio = choice(lista)
print(sorteio)

x=len(sorteio)

for i in sorteio:
    if i =="":
        penup()
        fd(30)
        