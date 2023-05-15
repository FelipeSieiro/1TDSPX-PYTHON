##CORREÇÃO DA PROVA

'''Utilizando apenas os conceitos que foram ensinados nesta matéria até
 aqui, faça um programa que:'''

# 1)
# a) [1pt] Solicite dois números ao usuário: n1 e n2.
# Estes números deverão ser inteiros e n1 deve ser maior que n2.

print()
print("-"*20)
print("Questão 1")
#
n1=float(input("Diga um número inteiro"))
while n1//1!=n1:
    print("Você não digitou um número inteiro")
    n1 = float(input("Diga um número inteiro"))

n2=float(input("Diga um outro número inteiro, menor que o primeiro"))
while n2//1!=n2 or n2>=n1:
    print("Você não digitou um número inteiro ou digitou um número maior ou igual ao primeiro")
    n2 = float(input(f"Diga um outro número inteiro, menor que o {n1}"))
n1=int(n1)
n2=int(n2)




# b) [1pt] Realize e imprima a soma de todos os números de n1 (inclusive)
# até n2 (exclusive)

soma=0 #porque é o valor neutro da soma
for i in range(n1,n2,-1):  # ou range(n2+1,n1+1)
    soma+=i #soma=soma+i
print(soma)



# 2)
# a) [1.5pt] Solicite dois números ao usuário: n1 e n2.
# Estes números deverão ser positivos, inteiros e diferentes entre si.

print()
print("-"*20)
print("Questão 2")
n1=float(input("Diga um número inteiro positivo"))
while n1//1!=n1 or n1<0:
    print("Você não digitou um número inteiro positivo")
    n1 = float(input("Diga um número inteiro positivo"))

n2=float(input("Diga um número inteiro positivo diferente do primeiro"))
while n2//1!=n2 or n2<0 or n2==n1:
    print("Você não digitou um número inteiro positivo diferente do primeiro")
    n2 = float(input(f"Diga um número inteiro positivo diferente de {n1}"))

n1=int(n1)
n2=int(n2)

# b) [1.5pt] Utiliando uma estrutura de loops (laços),
# faça uma rotina que imprima os 5 números anterioes ao menor dos dois
# (entre n1 e n2),e os 6 posteriores ao maior


##OPÇÃO 1:
'''
n1=3 -> 2,1,0,-1,-2
n2=5 -> 6,7,8,9,10,11
# '''
# if n1<n2:
#     for i in range(n1-1,n1-6,-1):
#         print(i)
#
#     for i in range(n2+1,n2+7):
#         print(i)
# '''
# n1=5 -> 6,7,8,9,10,11
# n2=3 -> 2,1,0,-1,-2
# '''
# else:
#     for i in range(n1+1,n1+7):
#         print(i)
#     for i in range(n2-1,n2-6,-1):
#         print(i)
######### OPÇÃO 2:
if n1>n2:
    menor=n2
    maior=n1
else:
    menor=n1

    maior=n2
for i in range(maior+1,maior+7):
    print(i)
print()
for i in range(menor-1,menor-6,-1):
    print(i)

# 3)  Solicite dois números ao usuário: n1 e n2.
# a) [1.5pt] n1 deve ser par e positivo; e n2 deve ser ímpar e negativo.
# enquanto o usuário digitar um número que não antenda a estas condições,
# o programa deverá dizer exatamente qual característica do número não
# estava de acordo com o que foi solicitado


print()
print("-"*20)
print("Questão 3")

n1=float(input("Digite um número par e positivo"))
while n1%2!=0 or n1<0:
    if n1%2!=0 and n1<0:
        print("O numero que você digitou é impar E negativo")
        n1 = float(input("Digite um número par e positivo"))
    elif n1<0:
        print("O numero que você digitou é negativo")
        n1 = float(input("Digite um número par e positivo"))
    else:# n1%2!=0 (apenas ímpar)
        print("O numero que você digitou é impar")
        n1 = float(input("Digite um número par e positivo"))

# n2 deve ser ímpar e negativo.
n2=float(input("Digite um número ímpar e negativo"))
while True:
    if n2%2==1 and n2<0:break

    elif n2%2!=1 and n2>=0:
        print("Você digitou um número par E positivo")
        n2 = float(input("Digite um número ímpar e negativo"))

    elif n2%2!=1:
        print("Você digitou um número par")
        n2 = float(input("Digite um número ímpar e negativo"))
    else:
        print("Você digitou um número positivo")
        n2 = float(input("Digite um número ímpar e negativo"))


# b) [2pt] Caso algum dos dois (ou os dois) não sejam números inteiros,
# diga qual o número inteiro mais próximo a ele

if n1!=int(n1):
    if n1-int(n1)>=0.5:
        print(int(n1)+1)
    else:
        print(int(n1))
if n2!=int(n2):
    if n2-int(n2)>=0.5:
        print(int(n2)+1)
    else:
        print(int(n2))


# 4) [1.5pt] Escreva aqui, em forma de comentário em bloco, um exemplo de input(s) e output(s) para cada questão anterior


#
# --------------------
# Questão 1
# Diga um número inteiro5
# Diga um outro número inteiro, menor que o primeiro9
# Você não digitou um número inteiro ou digitou um número maior ou igual ao primeiro
# Diga um outro número inteiro, menor que o 5.04
# 5
#
# --------------------
# Questão 2
# Diga um número inteiro positivo-8
# Você não digitou um número inteiro positivo
# Diga um número inteiro positivo7
# Diga um número inteiro positivo diferente do primeiro7
# Você não digitou um número inteiro positivo diferente do primeiro
# Diga um número inteiro positivo diferente de 7.08
# 9
# 10
# 11
# 12
# 13
# 14
#
# 6
# 5
# 4
# 3
# 2
#
# --------------------
# Questão 3
# Digite um número par e positivo5
# O numero que você digitou é impar
# Digite um número par e positivo-5
# O numero que você digitou é impar E negativo
# Digite um número par e positivo6
# Digite um número ímpar e negativo-7
#
# Process finished with exit code 0
