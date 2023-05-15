#correção dos exercícios ##############################################################
######### Observação: Resolver este exercício utilizando somente os comandos de entrada, saída e processamento de dados

# Exercício 1. Dado um numero pelo usuário, calcular o dobro e o quadrado
## obs: incluir na resposta o número dado pelo usuário

# print("digite um número")
# float_numero_original = float(input())
#
# float_numero_original = float(input('escolha um número: '))  # "5.1" -> 5.1
#
# dobro_numero_original = int(float_numero_original*2) #10 (eu nao vou ter na memória o valor original do dobro
# #
# dobro_numero_original_float=float_numero_original*2  #10.2
# dobro_numero_original_int=int(dobro_numero_original_float) #10
# #você vai ter os 2 em memória
#
# quadrado_numero_original = float_numero_original**2
#
# print("o dobro de {} é {}. E o quadrado dele é {}".format(int(float_numero_original),int(dobro_numero_original),quadrado_numero_original))
# #
#
# print(int(25.5))  #o python aceita
# print(int(float("25.5"))) #o python não aceita


# Exercício 2. Dados três números pelo usuário, calcular sua média,
# e a razão entre o primeiro e o último
# obs: definir a resposta a 10 caracteres, sendo 3 decimais
# media_3_numeros= 15.7895887954786589
#
# print("A média de 3 números é {:010.3f}%".format(media_3_numeros))
# print(f"A média de 3 números é {media_3_numeros:010.3f}")
#
# num_int = 25
# print("Numero {:05d}".format(num_int))
#sintaxe: {:'(opcional)com o que preencher''Num_caracteres_total'.'Num_caracteres_decimais'f}
#         {:                 0                    10             .           3             f}



# Exercício 3. Dado um numero pelo usuário, exibir o anterior e posterior
# (Ex: input=20, resposta=19 e 21)
# float_input=20

# print("anterior ={},posterior={}".format(float_input-1, float_input+1))

# Exercício 4. Dados dois numeros pelo usuário, calcular a potência entre eles


# Exercício 5. Dado um numero pelo usuário, exibir o proximo multiplo de 5
'''
Dica: para este problema, vocês vão precisar da // OU %
Exemplos:
Input: 8   -> Output: 10
Input: 15 ->  Output: 20
Input: 1  ->  Output: 5
Input: 89 ->  Output: 90'''














#fluxogramas | pseudocódigo ##############################################################

#exemplos teóricos:

## calcular a autonomia do automóvel do usuário
'''
o que é autonomia? -> quantidade de litros para percorrer uma distância (km/l)
precisamos de:
 - distância em km - ex:400
 - consumo em litros - ex:20
 - volume do tanque em litros, quanto tinha antes (em litros) -> solicitar a distância adequada
com isto, dividimos a distância pelo consumo
 - ex: 400/20 = 20km/l
 retornar ao usuário a resposta
'''
# distancia_percorrida_em_km = float(input("Diga quantos km você percorreu: "))
# consumo_em_l = float(input("Diga quantos litros de combustível você consumiu para percorrer {}km: ".format(distancia_percorrida_em_km)))
#
# print(f'A autonomia do seu veículo é de {distancia_percorrida_em_km/consumo_em_l} km/l')
#

## A partir da autonomia, calcular o custo mensal com gasolina do usuário
'''
quantas vezes você usa o carro por semana (trocar por mês) ->quantos km você roda quando usa o carro
  => pedir diretamente quantos km você usa por mês
qual a capacidade do tanque -> precisaria saber quanto do tanque você preenche por vez
  => pedir diretamente quantos litros você abastece por mês
autonomia do carro
_________________
quantos km anda -> precisa também da autonomia
quantos litros abastece quando vai ao posto
quantas vezes abastece -> 7 vezes/mes
 => pedir diretamente quantos litros abastece por mês

preço da gasolina = R$5/l
__________________
qual valor você paga por L de gasolina
quantos litro de gasolina você usa por mês
___________________
quantos KM,em média, por mês, você percorre
com a autonomia, calcular a quantidade de litros gastos

10km/l , 50km
  10 km - 1l
  50 km - Xl
10X = 50+1
x=50/10 = 5l

litros abastecidos *preço ->5l * 5R$/l = 25R$
'''
preco_gasolina = float(input("Qual valor que você paga por litro de gasolina ? (coloque só o valor, sem o R$)"))
litros_gasolina = float(input("Quantos litros de gasolina você usa por mês ?"))
consumo_mensal_gasolina = (preco_gasolina*litros_gasolina)
print(f"Você gasta R${consumo_mensal_gasolina} com gasolina por mês")



## calcular o menor número de notas necessárias para pagar este custo mensal