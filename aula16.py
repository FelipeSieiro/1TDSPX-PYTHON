### FUNÇÕES/PROCEDIMENTOS
# uma função RETORNA alguma coisa; um procedimento, não


#criando uma função (básica): def (definição)
'''sintaxe:
- função:
def nome_da_função(argumentos):
    instruções #quantas quiser
    [...]
    return variável(eis)

-procedimento:
def nome_da_função(argumentos):
    instruções #quantas quiser. Ex: print, salvar um arquivo, escrever no banco de dados, enviar uma chamada de api,chamar uma função, etc
    [...]

obs: o nome da função não pode ter espaços nem caracteres especiais (além do _ )
são as mesmas condições para nome de variável

obs2: um dos objetivos de agrupar suas linhas de código em funções é para
organizar seu código. Por isto, é uma boa prática adotada amplamente,
definir todas as funções no começo do código, e ir chamando conforme o necessário
Além disto, é bom dar nomes intuitivos para as funções

LEMBRANDO QUE: a definição TEM QUE VIR ANTES do chamado
(o python, por ser um linguagem interpretada, não possui void nem ponteiro)
'''



n=657.9648762159
# #print(f"{n:.2f}")
# numero=10
# #criando a função
def print_formatado(numero): #estou apenas definindo a função/procedimento. Não estou criando variáveis
    print(f"{numero:.2f}")


#executar (chamar) a função
# print_formatado(n) #aqui tem que ser uma variável já existente
#
# print_formatado(844.9854589845)

#
# #n1=float(input("Diga um número: "))
#
# def solicita_numero(condicao):
#     numero = float(input("Diga um número {}: "\
#                          .format(condicao)))
#     return numero
#
# def verifica_numero_par(numero):
#     while numero%2!=0:
#         print("Você não digitou um número par")
#         numero = solicita_numero('par')
#     return numero
#
# def solicita_numero_par():
#     numero_par=solicita_numero("par")
#     numero_par=verifica_numero_par(numero_par)
#     return numero_par
# n1=solicita_numero_par()


# podemos ter mais de um retorno
# def solicita_numero():
#     numero1 = float(input("Diga um número: "))
#     numero2 = float(input("Diga um outro número: "))
#     return numero1,numero2
# n1,n2=solicita_numero()



### EXERCÍCIOS
# 1) faça uma função que solicite 3 números necessariamente inteiros

# 2)criar uma função que solicite ao usuário e imprima na tela N
# números necessariamente inteiros, onde N inicialmente é um valor que você escolha


# 3) adaptar a(s) nossa(s) funções para que, ao a pessoa alterar a condição no solicita_numero,
# esta condição seja satisfeita
# condições possíveis: pos/neg/int/float/par/ímpar/diferentes*

# 4) isto que vocês fizeram funciona para combinação de condições?
## se não, como implementamos a escolha combinada?
