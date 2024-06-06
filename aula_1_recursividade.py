"""
Algoritmo que realiza a busca sequencial em um vetor/lista.
Linguagem Python
Autor: Prof. Vinicius Pozzobon Borin
"""
#
# def buscaSequencial (dados, buscado):
#     achou = 0
#     i = 0
#     while (((i < len(dados))) and (achou == 0)):
#         if (dados[i] == buscado):
#          achou = 1
#         else:
#          i = i + 1
#     if (achou == 0):
#      return -1
#     else:
#       return i + 1
#
# #programa principal
# import random
# # gerando 10 valores dentro de um intervalo de 0 até 9
# dados = random.sample(range(10), 10)
# print(dados)
# buscado = int(input('Digite o valor que deseja buscar: '))
# achou = buscaSequencial(dados, buscado)
# if (achou == -1):
#  print('Valor não encontrado.')
# else:
#  print('Valor encontrado na posição {}'.format(achou))


"""
Algoritmo que realiza a busca binária em um vetor/lista.
Linguagem C/C++.
Autor: Prof. Vinicius Pozzobon Borin
"""
#Define a função buscaBinaria com quatro parâmetros: inicio, fim, dados
# (a lista onde a busca será realizada), e buscado (o valor a ser procurado na lista).

def buscaBinaria (inicio, fim, dados, buscado):
    #Inicia um loop while que continuará enquanto o índice inicio for menor ou igual ao índice fim.
    # Isso é usado para limitar a busca à parte da lista que ainda não foi verificada.
    while(inicio <= fim):
        #Calcula o índice do meio da parte da lista que está sendo pesquisada.
        # Isso é feito somando inicio e fim e dividindo por 2 ( int para garantir que o resultado seja um número inteiro).
        meio = int((inicio + fim)/2)
        #Verifica se o valor buscado é maior que o valor no meio da lista.
        # Se for, então o valor buscado deve estar na metade superior da lista.
        if (buscado > dados[meio]):
            #Ajusta o índice inicio para ser um acima do índice do meio,
            # pois o valor buscado não está na metade inferior da lista.
         inicio = meio + 1
            #Verifica se o valor buscado é menor que o valor no meio da lista.
            # Se for, então o valor buscado deve estar na metade inferior da lista.
        elif (buscado < dados[meio]):
            #  Ajusta o índice fim para ser um abaixo do índice do meio,
            #  pois o valor buscado não está na metade superior da lista.
         fim = meio - 1
            #Se o valor buscado não é nem maior nem menor que o valor no meio,
            # então ele deve ser igual, e a função retorna o índice do meio, que é onde o valor buscado foi encontrado.
        else:
         return meio
    return -1
#programa principal
import random
#gerando 10 valores dentro de um intervalo de 0 até 9
dados = random.sample(range(10), 10 )
#Gera uma lista dados com 10 valores únicos aleatórios dentro de um intervalo de 0 até 9.
dados.sort()
#Imprime a lista dados ordenada
print(dados)
#Pede ao usuário para digitar o valor que deseja buscar na lista e armazena esse valor na variável buscado.
buscado = int(input('Digite o valor que deseja buscar: '))
#Chama a função buscaBinaria com os parâmetros apropriados para iniciar a busca pelo valor buscado.
achou = buscaBinaria(0, len(dados), dados, buscado)
#Verifica se o valor retornado pela função buscaBinaria é -1, o que indica que o valor
# buscado não foi encontrado. Se não for -1, imprime a posição onde o valor foi encontrado na lista.
if (achou == -1):
 print('Valor não encontrado.')
else:
 print('Valor encontrado na posição {}'.format(achou))
