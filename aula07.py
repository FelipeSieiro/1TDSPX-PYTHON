## EXERCÍCIO 1
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

# # utilizando apenas if e else, faça um programa que peça a idade sua e de um colega e
# # seus respectivos nomes, e diga:
seu_nome = input("qual é o seu nome:")
nome_do_amigo = input("o nome do seu amigo:")
sua_idade = input("qual é a sua idade:")
#sua_idade = input("qual é a sua idade,{}:".format(seu_nome))
idade_do_amigo = input("qual é a idade do seu amigo:")
#idade_do_amigo = input(f"qual é a idade de {nome_do_amigo}:")

# 1) a diferença de idade entre vocês, chamando pelo nome, sem que a resposta seja
# um número negativo
sua_idade_float = float(sua_idade)
sua_idade_int = int(sua_idade_float)  #25

idade_do_amigo_float = float(idade_do_amigo)
idade_do_amigo_int = int(idade_do_amigo_float)

print(f"Seu nome é:{seu_nome}")
print(f"Nome do seu amigo é:{nome_do_amigo}")

#if e else são mutualmente excludentes
# ou seja: ou faze TUDO de um, ou faz TUDO do outro
# NUNCA faz os 2 ao mesmo tempo
# else signfica "todo o resto"

# 2) quantas vezes a pessoa mais velha é mais velha que a mais nova,
# limitando a resposta a 2 casas decimais

#lembrando que na divisão em python, o resultado é SEMPRE float
#as linhas abaixo não são necessárias, visto que o resultado da divisão já é float
#vezes_mais_velho_float = float(vezes_mais_velho)
#ele_vezes_mais_velho_foat = float(ele_vezes_mais_velho)
'''
temos 2 casos possíveis
usuário mais velho
amigo mais velho
'''

if sua_idade_int > idade_do_amigo_int:
    diferenca_idade = sua_idade_int - idade_do_amigo_int
    #print(diferenca_idade)
    print(f"Você é {diferenca_idade} anos mais velho que {nome_do_amigo}")
    vezes_mais_velho = sua_idade_float / idade_do_amigo_float
    print(f"Você é {vezes_mais_velho:.2f} vezes mais velho que seu amigo.")
    #print("Você é {:.2f} vezes mais velho que seu amigo.".format(vezes_mais_velho))

    # para limitar as casas decimais (com f na frente): {variável:.Xf}, onde X é o número de casas decimais
    # para limitar as casas decimais (com.format): {:.Xf}, onde X é o número de casas decimais

else:
    diferenca_idade = idade_do_amigo_int - sua_idade_int
    ele_vezes_mais_velho = idade_do_amigo_float / sua_idade_float
    print(f"{nome_do_amigo} é {diferenca_idade} anos mais velho que você.")
    print(f"Ele é {ele_vezes_mais_velho:.2f} vezes mais velho que você.")

# 3) para cada pessoa, diga:
# se ela for maior de idade, há quanto tempo ela fez 18 anos
# E quanto tempo falta para se aposentar
# (assumindo que a idade de aposentadoria é 75 anos);

'''
casos possíveis:
entre 18 e 75
maior que 75
'''
#if sua_idade_int >= 18 and sua_idade_int< 75:  #isto joga o caso de a idade ser >75 para o else
#por isto, é recomendável que os ifs sejam os mais simples possível (sem "and")
#if 75>sua_idade_int>=18:

###usuario
if sua_idade_int>=18:
    print(f"{seu_nome} é maior de idade!")
    print(f"{seu_nome} fez 18 anos de idade a {sua_idade_int - 18} anos atras.")
    if sua_idade_int<75:
        print(f"Faltam {75 - sua_idade_int} anos para {seu_nome} se aposentar!")
    else:
        print(f"{seu_nome} já se aposentou!")

else:  #entra aqui se a idade NÃO for maior ou igual a 18
    print(f"{seu_nome} ainda é menor de idade e falta {18 - sua_idade_int} anos para você ser maior de idade.")
    if sua_idade_int >= 12:
        print(f"{seu_nome} é um adolescente!")
    else:
        print(f"{seu_nome} é uma criança!")

### amigo
if idade_do_amigo_float>=18:
    print("Você é maior de idade!")
    print(f"Você fez 18 anos de idade a {idade_do_amigo_float - 18} anos atras.")
    if idade_do_amigo_float<75:
        print(f"Faltam {75 - idade_do_amigo_float} anos para você se aposentar!")
    else:
        print("você já se aposentou!")
else:
    print(f"Você ainda é menor de idade e falta {18 - idade_do_amigo_float} anos para você ser maior de idade.")
    if idade_do_amigo_float >= 12:
        print(f"Você é um adolescente!")
    else:
        print("você é uma criança!")
# b) se ela for menor de idade, quantos anos faltam para ela fazer 18 anos
# E se ela ainda é criança (menor de 12 anos) ou já é adolescente (maior ou igual a 12 anos)
'''
casos possíveis
entre 12 e 17
menor de 12
'''
print(f"Final!")

###################################################################
##### exemplos soltos ###################
## casting de float para int é ok!
#print(int(25.5))

## casting de string (que seja float) para float é ok!
#print(float("25.5"))
#print(float("vinte e cinco ponto cinco"))  #ERRO!

## casting de string (que seja int) para int é ok!
#print(int("25"))

## casting de string (que seja FLOAT) para int NÃO É OK!
#print(int("25.5"))
# você precisa ANTES converter para float, depois para int
# valor_input="25.5"
# valor_em_float=float(25.5)
# valor_em_int=int(valor_em_float)
# print(valor_em_int)

# print(4/2)  #vai ser um float (2.0)

# Dados três números pelo usuário, calcular sua média, e a razão entre o primeiro e o último
# obs: definir a resposta a 10 caracteres, sendo 3 decimais#
# num1 = float(input("Digite um número: "))
# num2 = float(input("Digite outro número: "))
# num3 = float(input("Digite mais um número: "))
# media = (num1 + num2 + num3) / 3
# razao = num1 / num3
# print(media)
# print("{:10.3f}".format(razao))

# print(2.5==0000002.50000000)
# idade_do_colega=20
# if idade_do_colega>18:
#     print("colega maior de idade")
#
# if idade_do_colega==20:
#     print("vinte")
#
# if idade_do_colega==18:
#     print("igual")
# else:  #só liga para o if da linha 42. ele não liga para os ifs da linha 36 e 39
#     #cada else só diz respeito a 1 if
#     print("diferente")
###################################################################

#EXERCÍCIO EXTRA:

'''
utilizando apenas if e else, faça um programa que peça a idade sua e de um colega e
seus respectivos nomes, e diga, colocando os nomes nas respostas:
1) se seus nomes possuem a mesma quantidade de letras
2) quantos porcento a idade do mais velho representa da idade do mais novo,
limitando a resposta a 1 casa decimal E 
a) se a pessoa mais velha é maior de idade
b) se a pessoa mais nova é uma criança (possui menos de 12 anos)
3) para cada pessoa, diga:
a) se ela for maior de idade, se ela já se aposentou OU quanto tempo falta para se aposentar
(assumindo que a idade de aposentadoria é 75 anos);
b) se ela for menor de idade, qual sua idade em meses

OBS: criem casos de teste para todas as possibilidades que vocês identificarem
'''