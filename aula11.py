
## EXERCÍCIOS
# 1)para cada numero de 0 a 4, imprima a soma dos anteriores
# a ele (positivos)

'''
vamos escrever os números anteriores (positivos) a cada um e sua soma
0: nenhum -> 0
1: 0      -> 0
2: 1,0    -> 1
3: 2,1,0  -> 3
4: 3,2,1,0-> 6
'''
# soma=0
# # lembrando que range(5) = [0,1,2,3,4]
# for i in range(5): #para cada numero de 0 a 4
#     print(i)
#     soma+=i  #igual a soma=soma+i , ou seja, eu pego o que eu tinha e adiciono um número



# 2) # imprima apenas o quinto elemento da sequencia
# fibonacci (onde um novo elemento é a soma dos 2 anteriores,
# e por definição tem como primeiro o 0, e segundo o 1)

# fibonacci é a soma dos 2 números anteriores: 0,1,1,2,3,5,8,13,21
# anterior=0
# atual=1
# for i in range(3,6): #[3,4,5]
#     soma=anterior+atual
#     anterior=atual
#     atual=soma
#
# #este print só vai ser executado quando o for acabar
# print(atual)


# 3)Faça um programa em loop que imprima esta imagem:
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
# o range, se eu não disser o contrário, começa do 0
estrela="*"
#print(estrela*10)  #eu posso multiplicar strings

#
# for i in range(1,10):#[1,2,3,4,5,6,7,8,9] = 9 itens
#     #o primeiro i vale 1
#     if i<=5:
#         print(estrela*i)
#     else:
#         # quando i for 6, imprime 4 estrelas
#         # quando i for 7, imprime 3 estrelas
#         # quando i for 8, imprime 2 estrelas
#         # quando i for 9, imprime 1 estrela
#         print(estrela* (10-i) )
# #paramos na "metade" (quinto elemento)


## EXERCÍCIOS
# 1) agora, refaça o exercício acima, sendo que o número de linhas vai ser um número escolhido pelo usuário

# 2) imprima a tabuada do número 5, de 0 e 10, inclusive. Depois, adapte o programa para receber dois números do usuário: o de início e o de fim

# 3) faça um programa que imprima a soma dos números inteiros positivos de 1 a 100, inclusive

# 4) Calcular o fatorial de um número inteiro positivo



