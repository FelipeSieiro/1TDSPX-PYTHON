## OBSERVAÇÃO:
# para fazer o case ser comparado com variáveis (ao invés de números fixos),
# tem que usar a condição if:
# num1=float(input("diga sua idade"))
# num2=float(input("diga idade de outro usuario"))
#
# match num1:
#     case 0: #só funciona para comparações com números fixos
#         print("o numero é 0")
#
#
# match num1:
#     case _ if num1==num2:
#         print("iguais")
#     case _ if num1>num2:
#         print("num1 maior que num2")
#     case _ if num1<num2:
#         print("num2 maior que num1")




'''Exercícios:
1)	Solicite um número do usuário.
Diga a menor nota de real que é maior que este número.
Caso não exista, diga “Não existe nota de real maior que este número”'''

# numero=float(input("Diga um número"))

# 200,100,50,20,10,5,2
# ex:100 -> Resposta: a menor nota de real que é MAIOR QUE este número é 200
# entre 200 e 100, entre 100 e 50, entre 50 e 20, entre 20 e 10
# entre 10 e 5, entre 5 e 2
# entre 2 e 0. Menor que 0. Maior que 200

## exemplos: -1, -1000000, 0, 100, 75.96, 500, 200, 200.5, 199, 2, 1
# print("TESTE COM MATCH")
# match numero:
#     case _ if 200<=numero: print("Não existe nota de real maior que {} ".format(numero))
#     case _ if 200>numero>=100: print("a menor nota de real que é MAIOR QUE {} é 200".format(numero))
#     case _ if 100 > numero >= 50:
#         print("a menor nota de real que é MAIOR QUE {} é 100".format(numero))
#     case _ if 50 > numero >= 20:
#         print("a menor nota de real que é MAIOR QUE {} é 50".format(numero))
#     case _ if 20 > numero >= 10:
#         print("a menor nota de real que é MAIOR QUE {} é 20".format(numero))
#     case _ if 10 > numero >= 5:
#         print("a menor nota de real que é MAIOR QUE {} é 10".format(numero))
#     case _ if 5 > numero >= 2:
#         print("a menor nota de real que é MAIOR QUE {} é 5".format(numero))
#     case _ if 2 > numero:
#         print("a menor nota de real que é MAIOR QUE {} é 2".format(numero))
#
# print ("TESTE COM IF")
# if numero>=200:
#     print("Não existe nota de real maior que {}".format(numero))
# elif 200>numero>=100:#numero<200 and numero>=100
#     print("a menor nota de real que é MAIOR QUE {} é 200".format(numero))
# elif 100>numero>=50:
#     print("a menor nota de real que é MAIOR QUE {} é 100".format(numero))
# elif 50>numero>=20:
#     print("a menor nota de real que é MAIOR QUE {} é 50".format(numero))
# elif 20>numero>=10:
#     print("a menor nota de real que é MAIOR QUE {} é 20".format(numero))
# elif 10>numero>=5:
#     print("a menor nota de real que é MAIOR QUE {} é 10".format(numero))
# elif 5>numero>=2:
#     print("a menor nota de real que é MAIOR QUE {} é 5".format(numero))
# elif 2>numero>=0:
#     print("a menor nota de real que é MAIOR QUE {} é 2".format(numero))
# else: #número negativo
#     print("este é um número negativo")



'''2)	Solicite um número ao usuário.
Diga se este número é igual a 0.
Se não for, diga se ele é par ou ímpar
'''
#
# if numero==0:
#     print("O número é 0")
# elif numero%2==0: #tem que ser elif para não entrar aqui quando o número for 0
#     print("ele é par")
# else:
#     print("ele é ímpar")

'''3)	Solicite 3 números ao usuário.
Diga o menor deles'''

# elif num1==num2>num3:
#     print()
# elif num1==num2<num3:
#     print()
#
# # é equivalente a:
# elif num1==num2:
#     if num2>num3:
#         print()
#     else:
#         print()

'''4)	Solicite ao usuário (separadamente) o mês do ano, e o dia atual.
 Diga em qual estação estamos
 (similar ao das notas)
 Completar!
'''

# https://codingbat.com/python



# LOOP (laços - ciclo)

## for (para cada) -> loop "pré-determinado" - condição de parada pré programada
## while (enquanto) -> loop "pós-determinado" - condição de parada que pode ser desconhecida

### situação onde você quer repetição de um conjunto de comandos
### até que uma situação se satisfaça

# range (alcance)
# parâmetros: início, fim, tamanho do passo
# se você não digitar nada, o começo é sempre 0
# se você não digitar nada, o passo é sempre 1
# ele para ANTES do fim (ou seja, NÃO INCLUI O FIM)

# range(10) #lista de números começando em 0, que crescem de 1 em 1, e terminam ANTES do 10

## pass significa "passe" , ou seja, "não faça nada"

for i in range(0,10,-2): #este numero é o nosso controlador. Ele é criado na hora do loop e assume valores diferentes, conforme a instrução
    if i%2==0: print(f"o numero {i} é par")
    else: pass#print(f"o numero {i} é ímpar")

print("fora do loop")

## EXERCÍCIOS
# 1)para cada numero de 0 a 4, imprima a soma dos anteriores com ele próprio (positivos)

# 2) # imprima apenas o quinto elemento da sequencia fibonacci (onde um novo elemento é a soma dos 2 anteriores)
