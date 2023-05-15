### ELIF (ou então....)

# num=0
# if num<0:
#     print("numero negativo, não nulo")
# elif num==0:
#     print("numero 0")
# else:
#     print("numero positivo,não nulo")

#exemplo 1:
# num1=10
# num2=20
# num3=15
#comparar o num3 com os outros 2
# if num3<num1:
#     print("n3 é o menor dentre todos ou igual a 1")
# elif num3==num1:
#     print("n3 é igual a n1")
# elif num3==num2:
#     print("n3 é igual a n2")
# elif num1<num3<num2 : #equivalente a num1<num3 and num3<num2
#     #entra aqui caso o 3 esteja entre 1 e 2
#     print("n3 está entre n1 e n2")
# elif num3>num2:
#     print("n3 é maior que os outros 2 numeros ou igual a n2")

# num1=float(input("diga um número"))
# num2=float(input("diga um outro número"))
# num3=float(input("diga um terceiro número"))

#comparar o num3 com os outros 2


#MATCH/CASE
# uma comparação de IGUALDADE
'''
sintaxe:

match variável:  #tente combinar a vairável com os casos
    case 'condição':  #comparação de igualdade
        ação
'''
# num=10
# match num:
#     case 0: print("o numero é 0")#comparando se o num é IGUAL a 0
#     case 1: print("o número é 1")
#     case 5: print("o número é 5")
#     case _: print("o número não é 0,nem 1, nem 5")#else


## utilizando comparação de DESIGUALDADE no match:
# num=10
# match num:
#     case 0:
#         print("o num é 0")
#     case _ if num>0:
#         print("o numero é maior que 0")


## OBSERVAÇÃO:
# para fazer o case ser comparado com variáveis (ao invés de números fixos), tem que usar a condição if:
# num1=float(input("diga sua idade"))
# # num2=float(input("diga idade de outro usuario"))
# #
# # match num1:
# #     case _ if num1==num2:
# #         print("iguais")
# #     case _ if num1>num2:
# #         print("num1 maior que num2")
# #     case _ if num1<num2:
# #         print("num2 maior que num1")

## pegue a idade de duas pessoas e diga se são iguais.
## Se não for, diga a diferença entre elas, sem que
## o número seja negativo (e sem usar abs)

























# 1) [0.25pt] Solicite o nome do usuário e de uma outra pessoa
# a. A partir de agora, todas as menções a cada um
# (usuário ou outra pessoa) deverão ser pelo nome
#
# 2) [1.5pt] Caso a quantidade de caracteres seja diferente,
# diga quantas vezes o nome maior
# (em quantidade de caracteres) é maior que o menor,
# utilizando um número inteiro
# e caso sejam iguais, diga apenas que são iguais



## Exercícios

'''Exercícios:
1)	Solicite um número do usuário.
Diga a menor nota de real que é maior que este número.
Caso não exista, diga “Este número é muito grande para ser pago com apenas 1 nota de real”
2)	Solicite um número ao usuário.
Diga se este número é igual a 0.
Se não for, diga se ele é par ou ímpar
3)	Solicite 3 números ao usuário.
Diga o menor deles
4)	Solicite ao usuário (separadamente) o mês do ano, e o dia atual.
 Diga em qual estação estamos
'''