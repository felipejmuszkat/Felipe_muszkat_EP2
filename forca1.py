# -*- coding: utf-8 -*-

import turtle               # Usa a biblioteca de turtle graphics
window = turtle.Screen()    # cria uma janela
window.bgcolor("lightblue")
window.title("Poligonos")

w = turtle.Screen()
t = turtle.Turtle()

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
        

def desenhar_forca():
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
    
def cabeca():
    t.right(90)
    t.begin_fill()
    t.fillcolor("yellow")
    t.circle(20)
    t.end_fill()
    t.penup()
    t.goto(-200.00,110.00)
    
def corpo():
    t.left(90)
    t.pendown()
    t.fd(150)
    
def braco1():
    t.penup()
    t.goto(-200.00,80.00)
    t.pendown()
    t.left(45)
    t.fd(50)    
    
def braco2():
    t.goto(-200.00,80.00)
    t.right(90)
    t.fd(50)
        
def perna1():
    t.penup()
    t.goto(-200.00,-40.00)
    t.pendown()
    t.fd(50)

