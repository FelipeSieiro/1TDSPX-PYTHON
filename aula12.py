## EXERCÍCIOS
'''
*
**
***
****
*****
****
***
**
*
'''
# 1) agora, refaça o exercício acima, sendo que o número de linhas vai ser um número
# escolhido pelo usuário
# n=int(input("Diga um número ímpar posivito para a quantidade de linhas para a figura: "))
# #no nosso primeiro exemplo, n=9
# estrela="*"
# for i in range(1,n+1):
#     #o primeiro i vale 1
#     if i<=(n+1)/2: ##n//2 + 1
#         print(estrela*i)
#     else:
#         print(estrela* (n+1-i) )


### WHILE  (enquanto)
#damos a condição que tem que ser verdade para que continue
#esta condição tem que ser dada antes dele

#estrutura básica do while
# numero=0
# while numero<=5:  #é apenas uma comparação. Eu não altero o valor de número
#     #quando entra no loop, executa todas as linhas
#     print(numero)
#     #tenho que ter um incremento manual do meu contador
#     numero+=1
#
# #fora do loop
# print("fora do loop")
# print(numero)

'''
numero=0
->check da condição do loop: 0<=5? -> True -> entre no loop
    print(0)
    numero = 1
->check da condição do loop: 1<=5? -> True -> entra no loop
    print(1)
    numero = 2
->check da condição do loop: 2<=5? -> True -> entra no loop
    print(2)
    numero = 3
->check da condição do loop: 3<=5? -> True -> entra no loop
    print(3)
    numero = 4
->check da condição do loop: 4<=5? -> True -> entra no loop
    print(4)
    numero=5
->check da condição do loop: 5<=5? -> True -> entra no loop
    print(5)
    numero=6
->check da condição do loop: 6<=5? -> False -> acabou o loop

fora do loop:
print(numero) -> print(6)
'''

#n = int(input("Diga um número ímpar posivito para a quantidade de linhas para a figura: "))

'''forçar a ser ímpar'''
#ou seja, eu tenho que agir quando (enquanto) não for ímpar
# while n%2 == 0: #tenho que trabalhar a condição que eu não quero, até que ela seja o que quero
#     print("Este número é par. Por favor digite um número ímpar")
#     #é necessário ativamente alterar o valor da variável para que não seja um loop infinito
#     n = int(input("Diga um número ímpar posivito para a quantidade de linhas para a figura: "))
# print(n)

'''forçar a ser ímpar E positivo'''
# se o usuário digitar o que eu quero, eu não preciso fazer nada ex: 9

#só preciso interferir quando não for o que eu pedi
# o meu objetivo é ficar pedindo um número novo ao usuário ENQUANTO ele NÃO for o que quero

#enquanto a resposta for errada, pedir para alterar
# while (n%2==0 ) or (n<0):
#     print("Você não digitou um número nas condições que eu pedi")
#     n = int(input("Diga um número ímpar posivito para a quantidade de linhas para a figura: "))

'''forçar a ser ímpar E positivo, 
mas dizendo ao usuário exatamente o que está errado'''
#enquanto a resposta for errada, pedir para alterar
# while (n%2==0 ) or (n<0):
#     if n%2==0 and n<0:
#         print("Você digitou um número par E negativo")
#         n = int(input("Diga um número ímpar posivito para a quantidade de linhas para a figura: "))
#
#     elif n%2==0:
#         print("Você digitou um número par")
#         n = int(input("Diga um número ímpar posivito para a quantidade de linhas para a figura: "))
#
#     elif n<0:
#         print("Você digitou um número negativo")
#         n = int(input("Diga um número ímpar posivito para a quantidade de linhas para a figura: "))

#
# #loop enquanto o usuário quiser:
# resposta="sim"
# while resposta=="sim":
#     print("Vamos continuar")
#     resposta=input("Quer continuar? 'sim' ou 'não' ").lower()
#
# #é diferente de:
# resposta="sim"
# while resposta!="não":
#     print("Vamos continuar")
#     resposta=input("Quer continuar? 'sim' ou 'não' ").lower()

##### BREAK, PASS e CONTINUE
# break = quebra o loop-> sair do loop
# pass = passe (não faz nada)
# continue = avance o loop (ou seja, volta pro topo do loop). Não faz o que estiver abaixo dele no loop
#           No caso do for, avança o contador

# numero=0
#
# while numero<=5:  #é apenas uma comparação. Eu não altero o valor de número
#     print(numero)
#     if numero == 3: continue
#     print(numero)
#     numero += 1


# for i in range(5):
#     print("antes do if")
#     if i==3:continue
#     print("depois do if:")
#     print(i)
#     print()




### EXERCÍCIOS
# 1) imprima a tabuada do número 5, de 0 e 10, inclusive.
# Depois, adapte o programa para receber dois números do usuário: o de início e o de fim
# faça este exercício uma vez utilizando o for, e outra utilizando o while

# 2) faça um programa que imprima a soma dos números inteiros positivos de 1 a 100, inclusive
# faça este exercício uma vez utilizando o for, e outra utilizando o while

# 3) Solicitar um número obrigatoriamente inteiro positivo
# do usuário,
# e calcular seu fatorial
##fatorial de um número é a multiplicação dele com todos os que vieram antes dele (sem o 0)
## ex: 3! = 3*2*1 = 6
## ex: 0! = 1


# 4) Solicite dois número ao usuário,
# sendo que o segundo deverá ser obrigatoriamente
# maior que o primeiro

# 3) solicite 2 números ao usuário. Para cada número do 1 ao primeiro número, faça a tabuada dele do 0 até o segundo número