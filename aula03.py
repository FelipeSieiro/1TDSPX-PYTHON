# relembrar operadores matemáticos ##############################################################
# comentar várias linhas = ctrl + /
# operadores lógicos ##############################################################
'''
maior que >
menor que <
menor ou igual <=
maior ou igual >=
diferente !=
igualdade ==
'''

# print(0==0)
# print(0==0.0)
# print(0=="0")
#
# print( type(0) == type(0.0)  )
#
# print(type (0==0) )
# print(type(True))


minha_idade = 30
idade_do_colega = 35
#print("Eu sou mais velho que meu colega?",minha_idade>idade_do_colega)


# mais opções de formatação/funções em string ##############################################################

num = 23
# print(f"Número {num}")
# print(f"Número {num:5d}")
# print(f"Número {num:05d}")
# print(f"Número {num:>05d}")
# print(f"Número {num:<05d}")
# print("Número {:<05d}".format(num))
# print()
# print(f"Número:\n{num:^05d}")

# nome = 'FIAP'
# print(f"Nome = {nome:<10s}")

# nome_grande="FIAP COM MAIS DO QUE DEZ CARACTERES"
# print(f"Nome = {nome_grande:>.10}")
# print(f"Nome = {nome_grande:<.10}")
# print(f"Nome = {nome_grande:^.10}")

Num_float=12.0123456789
# print('{:>010f}'.format(Num_float))
# print('{:<10f}'.format(Num_float))
#print('{:.10f}'.format(Num_float))
# print('{:.1f}'.format(Num_float))
#print('{:*^10.2f}'.format(Num_float))

nome = "Computational Thinking using Python"
tamanho = len(nome) # Conta os caracteres da string
todas_maiusculas = nome.upper() # Converte tudo em maiúsculo
todas_minusculas = nome.lower() # Converte tudo em minúsculo
iniciais_maiusculas = nome.title() # Somente as iniciais em maiúsculo
print(f"{nome} possui {tamanho} caracteres")
print(f"Tudo maiúsculo: {todas_maiusculas}")
print(f"Tudo minúsculo: {todas_minusculas}")
print(f"Iniciais maiúsculas: { iniciais_maiusculas }")


#exercícios ##############################################################
######### Observação: Resolver este exercício utilizando somente os comandos de entrada, saída e processamento de dados

# Exercício 1. Dado um numero pelo usuário, calcular o dobro e o quadrado

# Exercício 2. Dados três números pelo usuário, calcular sua média, e a razão entre o primeiro e o último
# obs: definir a resposta a 10 caracteres, sendo 3 decimais

# Exercício 3. Dado um numero pelo usuário, exibir o anterior e posterior (Ex: input=20, resposta=19 e 21)

# Exercício 4. Dados dois numeros pelo usuário, calcular a potência entre eles

# Exercício 5. Dado um numero pelo usuário, exibir o proximo multiplo de 5
'''
Exemplos:
Input: 8   -> Output: 10
Input: 15 ->  Output: 20
Input: 1  ->  Output: 5
Input: 89 ->  Output: 90'''
