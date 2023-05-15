#### CORREÇÃO DA PROVA
'''
Utilizando apenas os conceitos que foram ensinados nesta matéria até aqui, faça um programa que:
1)	[0.25pt] Solicite o nome do usuário e de uma outra pessoa
a.	A partir de agora, todas as menções a cada um (usuário ou outra pessoa) deverão ser pelo nome
2)	[1.5pt] Diga quantas vezes o nome maior (em quantidade de caracteres) é maior que o menor,
limitado a 3 casas decimais
3)	[0.25pt] Utilizando seus nomes, solicite suas alturas, em cm (ex: 185 cm)
4)	Supondo que a altura média de um jogador da NBA é de 2,1m, diga, para cada pessoa:
a.	[1pt] Se ela for mais alta que esta média, quantos centímetros ela é mais alta
b.	[2pts] Se ela for mais baixa que ou estiver nesta média, quantos porcento da altura
da média ela teria que ter a mais para chegar a esta média (limitado a 2 casas decimais)
5)	[0.25pt] Solicite agora, a idade de cada usuário
6)	[0.5pt] Diga se a idade dos dois é igual
a.	[1pt] Caso não seja igual, diga, utilizando um número inteiro positivo,
quantos anos o mais novo tem a menos que o mais velho
7)	[0.25pt] Diga a média de idade entre as 2 idades
8)	[3pts] O programa deve conter também, em forma de comentário em bloco,
exemplos de inputs e outputs para cada uma das condições possíveis que vocês identificaram
e programaram. Estes comentários podem ser tanto item a item, quanto ao final de tudo.

'''

# 1)[0.25pt] Solicite o nome do usuário e de uma outra pessoa
# a.A partir de agora, todas as menções a cada um (usuário ou outra pessoa) deverão ser pelo nome

nome_1 = input ("Diga o nome de um usuário: ")
nome_2 = input ("Diga o nome de um outro usuário: ")

# 2)[1.5pt] Diga quantas vezes o nome maior (em quantidade de caracteres) é maior que o menor,
# limitado a 3 casas decimais


#conta do lado de fora é sempre salva na memória
# (tem que ser nomes diferentes para um não substituir o outro)
#quantas_vezes = len(nome_1)/len(nome_2)
#quantas_vezes2 = len(nome_2) / len(nome_1)

# OU ENTRA NO IF
if len(nome_1)>len(nome_2):  #entra aqui se o nome do usuário 1 for maior que o nome do usuário 2
    quantas_vezes = len(nome_1)/len(nome_2)
    print("O nome {} tem {:.3f} vezes mais caracteres que o nome {}"\
          .format(nome_1,quantas_vezes,nome_2))

# OU ENTRA NO ELSE
else:  #entra aqui se o nome do usuário 1 NÃO for maior que o nome do usuário 2 (inclui a igualdade)
    quantas_vezes = len(nome_2) / len(nome_1)
    print("O nome {} tem {:.3f} vezes mais caracteres que o nome {}" \
          .format(nome_2, quantas_vezes, nome_1))
'''
aqui nós temos 3 possibilidades:
- nome1 > nome2  (vai entrar no if)
ex: Adalberto e Bruno
- nome1= nome2  (vai entrar no else)
ex: Paulo e Paula
- nome1< nome2  (vai entrar no else)
Ex: bruno e adalberto
'''


# 3)[0.25pt] Utilizando seus nomes, solicite suas alturas, em cm (ex: 185 cm)

altura1=int(input("{}, diga sua altura, em cm".format(nome_1)))
altura2=int(input(f"{nome_2}, diga sua altura, em cm"))

# 4)	Supondo que a altura média de um jogador da NBA é de 2,1m, diga, para cada pessoa:
media_nba_em_cm=210
# a.[1pt] Se ela for mais alta que esta média, quantos centímetros ela é mais alta
#usuario 1
if altura1>media_nba_em_cm:
    cm_mais_alto = altura1 - media_nba_em_cm
    print(f"{nome_1} tem {cm_mais_alto} cm a mais que a média da nba")
# b.[2pts] Se ela for mais baixa que ou estiver nesta média, quantos porcento da altura
# da média ela teria que ter a mais para chegar a esta média (limitado a 2 casas decimais)
else:
    cm_mais_baixo= media_nba_em_cm-altura1
    pctg = 100* (cm_mais_baixo/media_nba_em_cm)
    print("{} teria que ter {:.2f}% a mais, em relação à média, para chegar à média"\
          .format(nome_1,pctg))

#usuario 2
if altura2>media_nba_em_cm:
    cm_mais_alto = altura2 - media_nba_em_cm
    print(f"{nome_2} tem {cm_mais_alto} cm a mais que a média da nba")

else:
    cm_mais_baixo= media_nba_em_cm - altura2
    pctg = 100 * (cm_mais_baixo / media_nba_em_cm)
    print("{} teria que ter {:.2f}% a mais, em relação à média, para chegar à média" \
          .format(nome_2, pctg))

'''
casos possíveis:
altura de uma pessoa > média
ex: 211 -> entra no if -> 1cm mais alto
altura de uma pessoa == média
ex: 210 -> entra no else -> teria que ter 0% a mais
altura de uma pessoa < média
ex: 185 -> entra no else -> teria que ter 11.90% a mais
'''

#5)	[0.25pt] Solicite agora, a idade de cada usuário

idade1= int(input("{}, Diga quantos anos você tem ".format(nome_1)))
idade2= int(input("{}, Diga quantos anos você tem ".format(nome_2)))

# 6)	[0.5pt] Diga se a idade dos dois é igual
if idade1==idade2:
    print (f"A idade de {nome_1} e {nome_2} é igual")
# a.	[1pt] Caso não seja igual, diga, utilizando um número inteiro positivo,
# quantos anos o mais novo tem a menos que o mais velho
else:
    if idade1<idade2:
        dif_idade=idade2-idade1
        print("{} é {} anos mais novo que {}"\
              .format(nome_1,dif_idade,nome_2))
    else: #idade2<idade1
        dif_idade = idade1 - idade2
        print("{} é {} anos mais novo que {}" \
              .format(nome_2, dif_idade, nome_1))

'''
opções possíveis:
idade1 == idade2
ex: 18 e 18 -> primeiro if
idade1>idade2
ex: 21 e 18 -> R: 3-> segundo else
idade2>idade1
ex: 18 e 22 -> R: 4-> segundo if
'''

#7)	[0.25pt] Diga a média de idade entre as 2 idades
print("A média de idade entre {} e {} é de {} anos"\
      .format(nome_2,nome_1,(idade1+idade2)/2))
'''
ex: 30 e 20 anos, resposta: 25.0
'''


#
# ### comentários sobre a prova
# # código solto
# "a"=="b"  #o código vai ser executado, só não vai ser armazenado nem printado,etc
#
# # vezes e diferença
# ## vezes maior: pensar e multiplicação/divisão
# ## maior ou menor: pensar em soma e subtração
#
# # > sem len
# ## o python vai comprar quem vem depois na ordem alfabética ("bruno">"adaltberto)
#
# # else apenas para 1 if
# #if #if 1
# #if #if 2
# #else #apenas para o if 2
#
# # condição em uma linha
# nome1="Bruno"
# nome2= "Adalberto"
# #pass = passe (ou seja, não faz nada)
# #isto é usado porque você não pode deixar um if ou else sem ação
# if len(nome2)>len(nome1): print("nome 2 > nome 1")
# else: pass #print("nome 2 <= nome 1")
#
# # conselho: fazer as variáveis dentro dos if
# #pois se fizer fora, gasta memória e tempo de processamento
# #e, neste caso, elas podem ter o mesmo nome, pois é um ou outro
# '''
# if idade1>idade2:
#     dif=idade1-idade2
# else:
#     dif=idade2-idade1
# '''
#
# # testem o código!! pensem nos casos extremos
# # vão testando conforme forem escrevendo
# # (é mais fácil testar 1 função por vez do que 30 ao mesmo tempo)
