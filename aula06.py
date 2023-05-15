#https://codingbat.com/python

#exercício da aula anterior
## calcular o menor número de notas e moedas necessárias para pagar
# este custo mensal sem troco
# obs: sem utilizar condições ou repetições
#custo_mensal=266.66


# ESTRUTURAS CONDICIONAIS - simples (if) se
# if 1>0:#"condição"
#     print("é verdade")
#     print("1 é maior que 0")
#     maior_que_0=True
#     resultado=1+5+9

# comparação de igualdade é ==
# definição é =

#
# minha_idade=25
# idade_colega=35
# #print(minha_idade>idade_colega)
# # #aqui eu estou fora do if
# if minha_idade>idade_colega:
#     dierenca_de_idade= minha_idade-idade_colega
#     print(dierenca_de_idade)
#     if minha_idade>18:
#         print("sou maior de idade")
# print("final")
# #
#
# if minha_idade>idade_colega:
#     dierenca_de_idade= minha_idade-idade_colega
#     print(dierenca_de_idade)
# if minha_idade>18:
#     print("sou maior de idade")
#     print("final")
#
# #é diferente de:
# if minha_idade>idade_colega and minha_idade>18:
#     print ("sou mais velho e maior de idade")

# ELSE
minha_idade=35
idade_colega=35
if minha_idade>idade_colega:
    diferenca_de_idade= minha_idade-idade_colega
    print(diferenca_de_idade)
#eles são mutualmente excludentes
else: #não posso escrever nada
    diferenca_de_idade = idade_colega-minha_idade
    print(diferenca_de_idade)

variavel = 3
if variavel==2:
    #variavel_nova = variavel + 1
    # é diferente de
    variavel += 1 # é o mesmo que: variavel = variavel + 1
print(variavel)
if variavel==2:
    variavel=variavel+2
else:
    variavel+=5

print(variavel)


## EXERCÍCIO
'''
utilizando apenas if e else, faça um programa que peça a idade sua e de um colega e
seus respectivos nomes, e diga:
1) a diferença de idade entre vocês, chamando pelo nome, sem que a resposta seja
 um número negativo
2) quantas vezes a pessoa mais velha é mais velha que a mais nova,
limitando a resposta a 2 casas decimais
3) para cada pessoa, diga:
a) se ela for maior de idade, há quanto tempo ela fez 18 anos
    E quanto tempo falta para se aposentar
(assumindo que a idade de aposentadoria é 75 anos);
b) se ela for menor de idade, quantos anos faltam para ela fazer 18 anos
    E se ela ainda é criança (menor de 12 anos) ou já é adolescente (maior ou igual a 12 anos)
'''
