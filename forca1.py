# -*- coding: utf-8 -*-

import turtle               # Usa a biblioteca de turtle graphics
window = turtle.Screen()    # cria uma janela
window.bgcolor("lightblue")
window.title("Poligonos")

w = turtle.Screen()
t = turtle.Turtle()
t.penup()
t.pen(shown=False)
t.goto(-300, -50)
t.pendown()
t.left(90)
t.fd(250)
t.right(90)
t.fd(100)
t.right(90)
t.fd(50)


from random import choice

arq=open("palavras.txt", encoding="utf-8")
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
        