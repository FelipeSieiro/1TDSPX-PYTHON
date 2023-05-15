
### EXERCÍCIOS
# 1) imprima a tabuada do número 5, de 0 e 10, inclusive.
# Depois, adapte o programa para receber dois números do usuário:
# o de início e o de fim
# faça este exercício uma vez utilizando o for,
# e outra utilizando o while


# quando o enunciado pede "a/o" soma, multiplicação, elemento, etc; quer dizer apenas o resultado final
## teria que imprimir todos, caso o enunciado pedisse todos os elementos, todas as somas, "até n-ésimo elemento", etc


#no for, a gente cria o contador na própria estrutura
# e ele avança com o contador automaticamente
# for i in range(0,10+1): #poderia ser range(11)
#     print(f"5x{i}=",5*i)
#
# #no while, temos que criar o contador fora; e avançar com ele manualmente
# print()
# numero=5
# c=0
# while c<=10:
#     print(f"5x{c}=", 5 * c)
#     c+=1

# n1=float(input("diga um número inteiro inicial da tabuada: "))
# n2=float(input("diga um número inteiro final da tabuada: "))
#
# while n1//1!=n1:
#     print("você não digitou um número inteiro")
#     n1 = float(input("diga um número inteiro inicial da tabuada: "))
# while n2//1!=n2:
#     print("você não digitou um número inteiro")
#     n2 = float(input("diga um número inteiro final da tabuada: "))

# while True:
#     n1 = float(input("diga um número inteiro inicial da tabuada: "))
#     if n1//1==n1: break
#     else:
#         print("você não digitou um número inteiro")
#         n1 = float(input("diga um número inteiro inicial da tabuada: "))

# n1=int(n1)
# n2=int(n2)
#
# # for i in range(n1,n2+1):
# #     print(f"5x{i}=",5*i)
#
# while n1<=n2:
#     print(f'5x{n1}=',5*n1)
#     n1+=1
#
#

# 3) Solicitar um número obrigatoriamente inteiro positivo
# do usuário,
# e calcular seu fatorial
##fatorial de um número é a multiplicação dele com todos os que vieram antes dele (sem o 0)
## ex: 3! = 3*2*1 = 6
## ex: 0! = 1

# n1=3
# fatorial=1
# for i in range(1,n1+1):
#     fatorial*=i
# print(fatorial)
#
# fatorial=1
# for i in range(n1,0,-1):
#     fatorial *= i
# print(fatorial)
# #
# i=1
# fatorial=1
# while i<=n1:
#     fatorial *= i
#     i+=1
# print(fatorial)
# #
# i=n1
# fatorial=1
# while i>=1: # ou i>0
#     fatorial*=i
#     i-=1
# print(fatorial)

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

# 7) faça um programa que, ao usuário digitar um número, obrigatoriamente inteiro, imprima os 20 números subsequentes
# Caso, após estes 20 número sejam negativos, dizer quanto falta para chegar a 0

# 8) faça um programa que solicite ao usuário um número N obrigatoriamente inteiro entre 1 e 20
# este número N vai ser a quantidade de novos números a serem digitados pelo usuário
# ao terminar de digitar estes N números, o programa deverá imprimir:
# ## o maior valor
# ## o menor valor
# ## a soma de todos os valores
# ## a média de todos os valores
# ## quantos porcento dos valores foram positivos
# ## quantos porcento dos valores foram negativos