# -*- coding: utf-8 -*-
 #usando o turtle primeiro precisa desenhar a forca por meio de funções, depois faz o sorteio das palavras

import turtle               # Usa a biblioteca de turtle graphics
window = turtle.Screen()    # cria uma janela
window.bgcolor("lightblue")
window.title("Poligonos")


w = turtle.Screen()
t = turtle.Turtle()
t.penup()
t.goto(-300, -50)
t.pendown()
t.left(90)
t.fd(500)

from random import choice

arq=open("entrada.txt", encoding="utf-8")
lista=[]
for linha in arq.readlines():
    linha.strip()
    if linha!="":
        lista.append(linha)

sorteio = choice(lista)
print(sorteio)

x=len(sorteio)

for i in sorteio:
    if i =="":
        t.penup()
        t.fd(30)
        
        
        
        
        