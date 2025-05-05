def imprime_Nome(nome):
    print(f"Nome{nome}")

def repeticao(num):
    for x in range (1, num+1,1):
        for y in range (0,x):
            print(x, end=" ")


def vogais(texto):
     cont=0
     for x in range(len(texto)):
         if x in "aeiou":
            cont+=1

def estoques( produto, quantidade, valor):
    valortotal = quantidade * valor
    print(f"o total no seu estoque é {valortotal}")

def desafio(n):
    if n >0:
        return "p"
    elif n<0:
        return "n"
    else: return "z"

def receber (a, b):
    soma = a+b
    return soma

def receber2 (*itens):
     soma= sum (itens)
     print(soma)

def exercicio8 (texto):
    cont =0
    for x in range (len(texto)-1,-1,1):
       if texto [x] in "8":
           cont =x


def listas (desafio):
    novalista =[]
    for x in lista:
        if x not in novalista:
            novalista.append(x)
    print(nova lista)





