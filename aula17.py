## DOCUMENTAÇÃO (explicação/definição da função)

def print_formatado(numero):
    '''
    Função que imprime o número com exatamente 3 casas decimais
    :param numero: Float ou int
    :return: None (apenas imprime)
    '''
    print(f"{numero:.3f}")

def calcula_o_dobro(n):
    '''
    Função que calcula e retorna o dobro de um número
    :param n: Numeral
    :return dobro: O dobro de N
    '''
    dobro = 2*n
    return dobro

#print_formatado(2.956259856)

#valor=calcula_o_dobro(10)
#print(valor)



## *ARGS e **KWARGS (KeyWord Args)

def soma_de_todos_os_numeros(*args): #possibilito o usuário a escrever quantos parâmetros ele quiser
    soma=0
    for i in args:
        soma+=i
    return soma



def cadastro_intersses2(livro,filme): #extamente 1 livro E 1 filme, e nesta ordem
    print(livro,filme)

def cadastro_interesses(**kwargs): #possibilita o usuário a escrever quantos parâmetros ele quiser, porém OBRIGATORIAMENTE cada um tem que ter um nome
    print(kwargs)
#
# def procura_livro(**kwargs):
#     '''
#     Função que busca por:
#         autor, gênero do livro, ano de publicação e/ou país de publicação
#     :param kwargs:
#     :return:
#     '''
#
#
# procura_livro(autor="edgar alan poe")
# procura_livro(genero="romance")
# procura_livro(ano_publicacao=1895)
# procura_livro(pais_publicacao="Brasil")

#soma=soma_de_todos_os_numeros(1,2,3,4,5) #o * fica só na definição
#print(soma)

#cadastro_interesses(filme="harry potter",livro2="hobbit",livro1="senhor dos anéis")


## ARGUMENTOS PRÉ-DEFINIDOS
def calcula_o_dobro(n=0): #o python vai guardar dentro dele que n, incialmente, é 0. Se você escrever outra coisa, ele muda

    dobro = 2*n
    return dobro
# valor=calcula_o_dobro()  #n=0
# print(valor)  #eu tenho o valor na memória para utilizar depois, caso precise
# print(calcula_o_dobro())  #o valor do dobro não fica salvo na memória


##Exercícios

### EXERCÍCIOS
# 1) faça uma função que solicite 3 números necessariamente inteiros

def solicita_numero(ordem):
    n=float(input(f"Diga o {ordem}º número inteiro: "))
    return n

def solicita_e_verifica_numero_inteiro(ordem):#=float(input("Diga um número inteiro: "))):
    n=solicita_numero(ordem)
    while n!=int(n):
        print("Você não digitou um número inteiro")
        n=solicita_numero(ordem)
    return n

def tres_numeros_inteiros():
    n1 = solicita_e_verifica_numero_inteiro(1)
    n2 = solicita_e_verifica_numero_inteiro(2)
    n3 = solicita_e_verifica_numero_inteiro(3)

    return n1,n2,n3
#
# n1,n2,n3=tres_numeros_inteiros()
# print(n1)
# print(n2)
# print(n3)

# 2)criar uma função que solicite ao usuário e imprima na tela N
# números necessariamente inteiros, onde N inicialmente é um valor
# que você escolha

def numeros_do_usuario(n):
    print("Você vai ter que digitar",n,"números inteiros")
    for i in range(1,n+1): # exemplo com n=9: range=[1,2,3,4,5,6,7,8,9]
        numero_temporario=solicita_e_verifica_numero_inteiro(i)
        print(numero_temporario)

numeros_do_usuario(3)

# 2.1)
#agora, colocar a condição (inteiro) como variável

# 3) adaptar a(s) nossa(s) funções para que, ao a pessoa alterar a condição no solicita_numero,
# esta condição seja satisfeita
# condições possíveis: pos/neg/int/float/par/ímpar/diferentes*

# 4) isto que vocês fizeram funciona para combinação de condições?
## se não, como implementamos a escolha combinada?
