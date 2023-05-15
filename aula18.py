## CONTINUAÇÃO DOS EXERCÍCIOS

# 2)criar uma função que solicite ao usuário e imprima na tela N
# números necessariamente inteiros, onde N inicialmente é um valor
# que você escolha
def solicita_numero(ordem,restricao):
    n=float(input(f"Diga o {ordem}º número {restricao}: "))
    return n

def solicita_e_verifica_numero(ordem,restricao):
    n=solicita_numero(ordem,restricao)
    if restricao=="inteiro":
        while n!=int(n):
            print(f"Você não digitou um número {restricao}")
            n=solicita_numero(ordem,restricao)
    elif restricao=="decimal":
        while True:
            if n!=int(n):break
            print(f"Você não digitou um número {restricao}")
            n=solicita_numero(ordem,restricao)
    #todo COMPLETAR AS OUTRAS RESTRIÇÕES
    return n
def numeros_do_usuario(n,restricao):
    print("Você vai ter que digitar",n,f"números {restricao}")
    for i in range(1,n+1): # exemplo com n=9: range=[1,2,3,4,5,6,7,8,9]
        numero_temporario=solicita_e_verifica_numero(i,restricao)
        print(numero_temporario)

# 3) adaptar a(s) nossa(s) funções para que, ao a pessoa alterar a condição no solicita_numero,
# esta condição seja satisfeita
# condições possíveis: pos/neg/int/float/par/ímpar/diferentes*


## EXERCÍCIOS

#1)a) crie uma função que retorne a soma E
# a multiplicação dos parâmetros (testar com no mínimo 5)

def soma_e_multiplicacao(*args): #possibilito o usuário a escrever quantos parâmetros ele quiser
    soma=0
    produto=1
    for i in args:
        soma+=i
        produto*=i
    return soma,produto

#1)b) modifique a função anterior para que ela receba como argumento
# o tipo de operação que queremos fazer (soma OU multiplicação)
# e retorne APENAS o que foi pedido

# def soma_e_multiplicacao(operacao,*args): #possibilito o usuário a escrever quantos parâmetros ele quiser
#     '''
#     Função que recebe uma lista de número, realiza e retorna o
#     resultado da operação escolhida
#     :param operacao: operação a ser realizada ('soma' ou 'multiplicação')
#     :param args: números para realizar a operação
#     :return: número contendo o resultado da operação
#     '''
#     if operacao=="soma":
#         soma = 0
#         for i in args:
#             soma += i
#         return soma
#     elif operacao=="produto":
#         produto = 1
#         for i in args:
#             produto *= i
#         return produto
#     else: return "Erro"
#
#
# resultado=soma_e_multiplicacao("soma",5,5,9,7,67,.85,999)
#
# print(soma_e_multiplicacao("soma",5,5,9,7,67,.85,999))
#

#2) crie uma função que receba 3 parâmetros: n, maior e menor.
# Essa função deve retornar se n está entre o maior e o menor

def maior_menor(n,maior,menor):
    return maior>n>menor

print(maior_menor(3,2,4))  #vai dar a resposta errada, pois a ordem está invertida


### EXERCÍCIOS ADICIONAIS

#1) escreva uma função que receba como argumento um número e retorne seu fatorial

#2) escreva uma função que solicite ao usuário um número e force para que ele seja positivo e inteiro,e retorne este número

#3) escreva uma função que chame combine as funções dos exercícios anteriores
# (ou seja, uma função sem parâmetros que utilize o retorno da segunda função como parâmetro da primeira)

#4) Crie uma função que receba uma palavra e retorne ela toda em letras maiúsculas

#5) Cria uma função que receba uma palavra e uma condição ('maiúscula' ou 'minúscula') e retorne a palavra na condição solicitada

#6) Crie uma função que receba 2 números (inicio e fim), e imprima os números pares neste intervalo (incluindo o início e fim)

#7) Crie uma função que receba 2 números e imprima sua soma, multiplicação, divisão e subtração.
# Estes prints deverão ser formatados para serem bem explícitos no que está sendo mostrado (incluindo os números originais);
# E esta função deverá estar devidamente documentada, explicando tudo o que ela realiza, seus parâmetros e possíveis retornos

