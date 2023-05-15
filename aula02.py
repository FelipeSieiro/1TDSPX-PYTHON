import math

# outros tipos de formatação
Minha_idade=30
Idade_alvo=50
Idade="30"
Tempo_ate_alvo= Idade_alvo - Minha_idade

# para pular linha na hora de printar: \n (pode ser utilizado dentro do text) ou print()
print("Anos até o alvo:",Tempo_ate_alvo,"anos")


print("\nAnos até o alvo: {} anos. \nIsto é porque hoje você tem {} anos"\
      .format(Tempo_ate_alvo,\
              Minha_idade))
#terceira opção
print("\nAnos até o alvo: {n1} anos. \nIsto é porque hoje você tem {n2} anos"\
      .format(n1=Tempo_ate_alvo,n2=Minha_idade))

#quarta opção: formatar dentro do texto -> colocar f antes das "
print(f"A minha idade é:{Minha_idade} anos. A idade alvo é {Idade_alvo} anos")





# casting #####################################################################################
numero_inteiro = 25
numero_float = 25.5
numero_em_string = "25.5"
var_booleana= True

# numero_inteiro_convertido_em_foat=float(numero_inteiro)
# print(type(numero_inteiro_convertido_em_foat))
# print(numero_inteiro_convertido_em_foat)

# numero_float_convertido_em_inteiro = int(numero_float)
# print("O tipo da variável numero_float_convertido_em_inteiro ({}) é:"\
#       .format(numero_float_convertido_em_inteiro),type(numero_float_convertido_em_inteiro))
# print(numero_float_convertido_em_inteiro)

# numero_em_string_convertido_para_float=float(numero_em_string)
# print(numero_em_string_convertido_para_float)

# print(type(numero_inteiro))
# print(type(numero_float))
# print(type(numero_em_string))
# print(type(var_booleana))

# obs: caso a string seja em formato de float ex: "25.5", você NÃO vai conseguir converter para inteiro
## primeiro terá que converter para float; e depois para inteiro




# input #####################################################################################
## é a forma com a qual pedimos dados do usuário
## o imput vem sempre como string

# idade_do_usuario = input("Digite a sua idade: ")
# print(type(idade_do_usuario))
# print(idade_do_usuario)
# #print(Idade_alvo - idade_do_usuario)  ##vai dar erro
#
# #temos que converter a entrada em inteiro
# idade_do_usuario_em_inteiro = int(idade_do_usuario)
# print(Idade_alvo - idade_do_usuario_em_inteiro)







# operadores aritméticos #####################################################################################
# + - * /
# ** (potenciação)           ## ^ é operador lóico XOR

##Lembrando que o python respeita a ordem matemática de execução de operações
### Ou seja, ** vem antes de / e *
### * e / vem antes de + e -
### caso queira dar prioridade a uma operação, utilizar ()
###Ex:
media= (Minha_idade + Idade_alvo)/2

'''
Atenção!!!:

# DIVISÃO INTEIRA -> //
# resto (módulo) -> %

módulo é apenas uma outra forma de se referir ao resto da divisão!
'''

## o resultado da divisão em python será SEMPRE float
print("divisao",10/5)
print("divisao",13/5)
print("divisão inteira",13//5)
print("resto (módulo)",13%5)

print("exemplo de potencia",5**2)

#raiz quadrada (square root - sqrt) -> está na biblioteca math
print("raiz quadrada de 25 =",math.sqrt(25))




# exercícios #####################################################################################

## faça um programa que:
### peça o nome do usuário 1
### peça o nome do usuário 2

### peça a idade do usuário 1
### peça a idade do usuário 2

### calcule a diferença de idade entre eles
### calcule a média de idade entre ele

### imprima estes resultados, colocando os nomes dos usuários


Primeiro_nome = input("Digite o nome do usuario 1 ")
Segundo_nome = input("Digite o nome do usuario 2 ")
#
# #o input e conversão para inteiro podem ser feitas de duas formas:
# # opção 1
# #Idade_usuario_1 = input("Digite a idade do usuario 1")
# #Idade_usuario_1_convertida=int(Idade_usuario_1)
# #opção 2:
Idade_usuario_1_convertida=int(input("Digite a idade do usuario {} ".format(Primeiro_nome)))
Idade_usuario_2_convertida=int(input("Digite a idade do usuario {} ".format((Segundo_nome))))

# print(Idade_usuario_1_convertida)
# print(type(Idade_usuario_1_convertida))

print("A diferença de idade entre {} e {} é de {} anos"\
      .format(Primeiro_nome,\
              Segundo_nome,\
              Idade_usuario_1_convertida-Idade_usuario_2_convertida))

soma_das_idades = Idade_usuario_1_convertida+Idade_usuario_2_convertida
media_de_idade = soma_das_idades /2

print("A media de idade entre {} e {} é de {} anos"\
      .format(Primeiro_nome,\
              Segundo_nome,\
              media_de_idade))