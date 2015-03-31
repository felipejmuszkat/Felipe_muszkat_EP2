# -*- coding: utf-8 -*-

import turtle               # Usa a biblioteca de turtle graphics
from random import choice

# retorna a lista de palavras contidas no arquivo
def ler_palavras(nome="palavras.txt"):
    arq=open(nome, encoding="utf-8")
    lista=[]
    for linha in arq.readlines():
        linha = linha.strip()
        if len(linha) > 0:
            lista.append(linha.lower())
        
    return lista

# retorna uma palavra aleatoria da lista
def escolhe_palavra(lista):  
    return choice(lista)
        
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
    t.penup()
    t.goto(-200, 150)
    t.setheading(180)
    t.pendown()
    t.begin_fill()
    t.fillcolor("yellow")
    t.circle(20)
    t.end_fill()
    
def corpo():
    t.penup()
    t.goto(-200.00,110.00)
    t.setheading(270)
    t.pendown()
    t.fd(150)
    
def braco1():
    t.penup()
    t.goto(-200.00,80.00)
    t.setheading(270)
    t.pendown()
    t.left(45)
    t.fd(50)    
    
def braco2():
    t.penup()
    t.goto(-200.00,80.00)
    t.setheading(225)
    t.pendown()
    t.fd(50)
        
def perna1():
    t.penup()
    t.goto(-200.00,-40.00)
    t.setheading(225)
    t.pendown()
    t.fd(50)

def perna2():
    t.penup()
    t.goto(-200.00,-40.00)
    t.setheading(315)
    t.pendown()
    t.fd(50)
    
def tracinhos(palavra):
    t.penup()
    t.goto(-100, 0)
    t.setheading(0)
    for letra in palavra:
        t.pendown()
        if letra == " ":
            t.penup()
        t.fd(20)
        t.penup()
        t.fd(5)

def encontra_letra(palavra, letra):
    pos = {}
    i = 0
    for i in range(0, len(palavra)):
        if palavra[i] == letra:
            pos[i] = letra
        if letra in acentos.keys():
            for acento in acentos[letra]:
                if acento == palavra[i]:
                    pos[i] = acento

    return pos
    
w = turtle.Screen()
w.screensize(1200)
w.title("Forca")
t = turtle.Turtle()

acentos = {"a" : ["á", "à", "ã"], "e" : ["é", "ê"], "o" : ["ó", "ò", "õ", "ô"],"u" : ["ú","ù","û"], "i" : ["í","ì","î"]}
lista = ler_palavras()


while True:
    error = 0
    acertos = 0
    palavra = escolhe_palavra(lista)
    lista.remove(palavra)
    for letra in palavra:
        if letra == " ":
            acertos += 1

    desenhar_forca()
    tracinhos(palavra)
    chutadas = []
    while error < 6 and acertos < len(palavra):
        letra = w.textinput("Chute uma letra", "Escolha sua letra")
        if letra is None:
            break
        letra = letra.lower()
        if len(letra) > 1 or letra in chutadas:
            continue
        chutadas.append(letra)
        posicoes = encontra_letra(palavra, letra)
        if len(posicoes) == 0:
            t.penup()
            t.goto(-100 + 25 * error, 200)
            t.pendown()
            t.write(letra.upper(), font=('Arias', 14))
            if error == 0:
                cabeca()
            elif error == 1:
                corpo()
            elif error == 2:
                braco1()
            elif error == 3:
                braco2()
            elif error == 4:
                perna1()
            else:
                perna2()
            error += 1
        else:
            for p in posicoes.keys():
                t.penup()
                t.goto(-95 + 25 * p, 0)
                t.pendown()
                t.write(posicoes[p].upper(), font=('Arial', 14))
                acertos += 1
    op = w.textinput("Jogar novamente?", "Se quiser jogar novamente, escreva 1")
    if op != "1":
        break
    w.reset()
    t.reset()

w.bye() 
