#!/usr/bin/python3

from  Maquina import *

produtos=[
    "1 Refri",
    "2 Agua",
    "3 Chocolate",
    "4 Salgadinho"
    ]
produtos_valores=[
        5,
        3,
        8,
        7
        ]
def valor(escolha):
    return int(produtos_valores[escolha])

for i in range(len(produtos)):
    s=str(produtos[i])+" "+"R$"+ str(produtos_valores[i])+",00"   
    print (s)

escolha=input("Escolha o Produto:")
try:
    preco = valor(int(escolha)-1)
    if  preco != 0:
        valor_recebido=0
        while valor_recebido < preco:
            a=input("Insira uma nota valida: 2,5,10,20,50,100:")
            try:
                valor_recebido = valor_recebido + checar_nota(int(a),validas)
            except:
                print("Nota inserida inválida!!")
        print("valor inserido:",valor_recebido)
        troco=valor_recebido-preco        
        print("Troco:R$",troco)
        try:
            a=calcular_notas(troco)
            print("Notas:")
            for i in range(6):
                print ("\t",validas2[i]," X ",a[i])
        except:
            print("Máquina temporariamente sem troco.\nDevolvendo o valor inserido!!")
except:
    print("Escolha inválida!!")
