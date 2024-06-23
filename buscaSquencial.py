def buscaSequencial(dados, buscado):
    # Inicializa a variável 'achou' como 0 (não encontrado)
    achou = 0
    # Inicializa o índice 'i' como 0
    i = 0
    # Enquanto 'i' for menor que o tamanho de 'dados' e 'achou' for 0, continue
    while (((i < len(dados))) and (achou == 0)):
        # Se o elemento na posição 'i' for igual ao valor 'buscado'
        if (dados[i] == buscado):
            # Atualiza 'achou' para 1 (encontrado)
            achou = 1
        else:
            # Incrementa 'i' para verificar o próximo elemento
            i = i + 1
    # Se 'achou' for 0 após o loop, retorna -1 (não encontrado)
    if (achou == 0):
        return -1
    else:
        # Retorna a posição do elemento encontrado, ajustada para base 1
        return i + 1

# Programa principal
import random
# Gerando 10 valores únicos dentro de um intervalo de 0 até 9
dados = random.sample(range(10), 10)
# Exibe a lista 'dados'
print(dados)
# Solicita ao usuário para digitar o valor que deseja buscar
buscado = int(input('Digite o valor que deseja buscar: '))
# Chama a função buscaSequencial com 'dados' e 'buscado'
achou = buscaSequencial(dados, buscado)
# Se 'achou' for -1, o valor não foi encontrado
if (achou == -1):
    print('Valor não encontrado.')
else:
    # Se 'achou' não for -1, exibe a posição do valor encontrado
    print('Valor encontrado na posição {}'.format(achou))
