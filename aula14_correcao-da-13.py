
# EXERCÍCIOS
# 1) completar o exercício anterior ( falta forçar para que seja um número inteiro positivo)

# 2) faça um programa que imprima a soma dos números inteiros positivos de 1 a 100, inclusive
# faça este exercício uma vez utilizando o for, e outra utilizando o while

# 3) Solicite dois número ao usuário,
# sendo que o segundo deverá ser obrigatoriamente
# maior que o primeiro


# 4) solicite 2 números ao usuário.
# Para cada número do 1 ao primeiro número,
# faça a tabuada dele do 0 até o segundo número
# n1=float(input("Diga um número inteiro"))
# while n1//1!=n1:
#     print("Você não digitou um número inteiro")
#     n1 = float(input("Diga um número inteiro"))
#
# n2 = float(input("Diga outro número inteiro"))
# while n2//1!=n2:
#     print("Você não digitou um número inteiro")
#     n2 = float(input("Diga outro número inteiro"))
#
# n1=int(n1)
# n2=int(n2)
#
# #vamos começar com o que já fizemos antes
# # para cada número do 1 ao n1:
# for i in range(1,n1+1):
#     pass
# # para cada número do 0 ao n2:
# for j in range(n2+1):
#     pass
#
# #agora, juntando os 2:
# for i in range(1,n1+1):
#     print("Tabuada do",i,", de 0 a",n2,":")
#     for j in range(n2+1):  #quando não digita nada, o começo é 0 e o passo é 1
#         #primeiro finaliza o loop de dentro para depois continuar o loop de fora
#         print(f"{i}*{j}=",i*j)
#     print()

# 5)imprima a tabuada do número 5, de 0 e 10, inclusive.
# Depois, adapte o programa para receber dois números do usuário: o de início e o de fim
# ao resolver esta questão:
# for i in range(n1,n2+1,1): #o range só aceita números inteiros
#     print(5*i)
# # precebemos que n1 não pode ser maior que n2 nesta configuração
# ## temos 2 formas de resolver: OU travar para que n2 seja maior que n1
# ## OU fazer um if, e escrever o range de acordo
# EXERCÍCIO: fazer as duas opções

# 6) faça um programa que imprima apenas os números pares no intervalo de n1 (inclusive) até n2 (exclusive)
# onde n1 e n2 são números dados pelo usuário, e deverão ser inteiros. Além disto, n2 deve ser maior que n1

# 7) faça um programa que, ao usuário digitar um número, obrigatoriamente inteiro,
# imprima os 20 números subsequentes
# Caso, após estes 20 número, o último ainda seja negativo,
# dizer quanto falta para chegar a 0

# n = float(input("Diga um número inteiro: "))
# while n//1 != n:
#     print("Você não digitou um número inteiro")
#     n = float(input("Diga um número inteiro: "))
# n=int(n)
#
# for i in range(n+1,n+21): #exemplo com n=0: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#     #n += 1
#     print(i)
# if i<0: #eu fiz meu range variar conforme meu número inicial. Portanto , o 'i' final já é o que eu quero
#     print(f"Falta {i*(-1)} para chegar a 0")
# ############
#
# n = int(input("Diga um número inteiro: "))
# for i in range(20):
#     n+=1
#     print(n)
# if n<0:  #eu alterei meu número inicial
#     print(f"Falta {n*(-1)} para chegar a 0")
# ##############
#
# n = int(input("Diga um número inteiro: "))
# for i in range(1,21): #esse range sempre vai ser:[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#     print(n+i)
# if n+i<0:  #eu não alterei meu número inicial
#     print(f"Falta {(n+i)*(-1)} para chegar a 0")

# 8) faça um programa que solicite ao usuário um número N obrigatoriamente inteiro entre 1 e 20
# este número N vai ser a quantidade de novos números a serem digitados pelo usuário
# ao terminar de digitar estes N números, o programa deverá imprimir:
# ## o maior valor
# ## o menor valor
# ## a soma de todos os valores
# ## a média de todos os valores
# ## quantos porcento dos valores foram positivos
# ## quantos porcento dos valores foram negativos


# n = float(input("Digite um numero inteiro entre 1 e 20: "))
# while n//1 != n or n < 1 or n > 20:
#     print("O numero precisa ser inteiro e entre 1 e 20!")
#     if n//1 != n: print("Você não digitou número inteiro")
#     n = float(input("Digite um numero inteiro entre 1 e 20: "))
#
# N = int(n)
#
# #maior = 0  # float("-inf")
# #menor = 0  # float("inf")
# soma = 0
# #media = 0
# positivos = 0
# negativos = 0
# for i in range(N):
#     n_interacao = float(input(f"Digite o {i+1}º de {N} numeros: "))
#     soma += n_interacao
#     media = soma/n  #media+=n_interacao/n
#     if i == 0:
#         maior = n_interacao
#         menor = n_interacao
#     else:
#         if n_interacao > maior: maior = n_interacao
#         if n_interacao < menor: menor = n_interacao
#
#     if n_interacao >= 0: positivos += 1
#     else: negativos += 1
#
# prcPositivos = (positivos * 100) / n
# prcNegativos = (negativos * 100) / n
# print("Dos {} numeros digitados {:.2f}% foram positivos".format(n, prcPositivos))
# print("Dos {} numeros digitados {:.2f}% foram negativos".format(n, prcNegativos))
# print("O maior numero lido foi {}".format(maior))
# print("O menor numero lido foi {}".format(menor))
# print("A soma de todos os {} valores digitados é {}".format(n, soma))
# print("A media de todos os {} valores digitados é {:.2f}".format(n, media))

# exemplo: 3 números: -1,1,0
### soma = 0
### media = 0
### maior = 1
### menor = -1
### %neg = 33.34%
### %pos = 66.67%


# 9) Imprima o n-ésimo número da sequencia de fibonacci, sendo N um número inteiro positivo dado pelo usuário
# fibonacci = soma dos 2 últimos termos. Ex: 0 1 1 2 3 5 8 13 21...
# n = float(input("Diga um número inteiro positivo: "))
# while n//1 != n or n<0:
#     print("Você não digitou um número inteiro positivo")
#     n = float(input("Diga um número inteiro positivo: "))
# n=int(n)
'''
começando:
#sequencia = 0,1
ultimo=1
penultimo=0
soma=1
#
sequencia= 0,1,1
ultimo = 1 (soma)
penutimo = 1 (era o último)
soma = ultimo+penultimo = 1+1=2
#
sequencia= 0,1,1,2
ultimo = 2 (soma)
penultimo = 1 (ultimo)
soma = ultimo+penultimo = 2+1 =3
#
sequencia = 0,1,1,2,3

'''
resposta=0
ultimo=1
penultimo=0

###versão for
# for i in range(3,n+1):
#     resposta = ultimo+penultimo #na primeira rodada, vou estar calculando meu 3º elemento
#     penultimo = ultimo
#     ultimo = resposta

#as duas principais diferenças básicas do while pro for, é que no while a gente
# tem que criar o contador fora, e incrementar manualmente esse contador

##versão while
# i=3
# while i<=n: #no while, como eu posso colocar a igualdade, eu não preciso do n+1
#     resposta = ultimo+penultimo #na primeira rodada, vou estar calculando meu 3º elemento
#     penultimo = ultimo
#     ultimo = resposta
#     i+=1
#
# if n==1:
#     print(f"O {n}º elemento de fibonacci é 0")
# elif n==2:
#     print(f"O {n}º elemento de fibonacci é 1")
# else:
#     print(f"O {n}º elemento de fibonacci é {resposta}")


###EXERCÍCIOS

# 1) Solicite um número N ao usuário e force com que seja inteiro, positivo e ímpar.
# Depois, solicite uma letra ao usuário
# Imprima N linhas, onde na primeira linha seja impressa esta letra N vezes, na segunda N-1 vezes e por aí vai
#Obs: lembrando que "f"*5 = "fffff"
# Ex: N=5, letra="f"
# Resposta:
# fffff
# ffff
# fff
# ff
# f



# 2) Solicite um número do usuário e force para que seja decimal e negativo.
# Caso o número digitado não atenda a alguma condição, diga exatamente qual condição não foi satisfeita
# imprima os números inteiros entre ele e sua metade






### RESPOSTAS:
#1)
# n=float(input("diga um número inteiro, positivo e ímpar"))
# while n//1!=n or n<0 or n%2==0:
#     print("Este número não atende às condições desejadas")
#     n = float(input("diga um número inteiro, positivo e ímpar"))
# letra=input("por favor, digite apenas uma letra")
# n=int(n)
# for i in range(n,0,-1):
#     print(letra*i)


#2)
# n=float(input("diga um número decimal e negativo"))
# while n//1==n or n>=0:
#     if n//1==n and n>=0:
#         print("você digitou um número inteiro e positivo.")
#     elif n//1==n:
#         print("você digitou um número inteiro")
#     else:
#         print("Você digitou um número positivo.")
#     n = float(input("diga um número decimal e negativo"))
#
#
# for i in range(int(n),int(n/2)):  #como o número é negativo, esta ordem de início e fim é inversa a que normalmente usamos. Se fosse positivo, teria que ser ao contrário
#     print(i)