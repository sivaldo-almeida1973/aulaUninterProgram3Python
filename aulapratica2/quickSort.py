# Definição da função quickSort, que organiza os elementos de uma lista.
def quickSort(dados, inicio, fim):
    # Se o índice de início é menor que o de fim, ainda há elementos para ordenar.
    if inicio < fim:
        # A função partition é chamada para dividir a lista e encontrar a posição correta do pivô.
        posicao_de_particionamento = partition(dados, inicio, fim)
        # A função quickSort é chamada recursivamente para a sublista à esquerda do pivô.
        quickSort(dados, inicio, posicao_de_particionamento - 1)
        # A função quickSort é chamada recursivamente para a sublista à direita do pivô.
        quickSort(dados, posicao_de_particionamento + 1, fim)

# Definição da função partition, que particiona a lista e retorna a posição do pivô.
def partition(dados, inicio, fim):
    # O pivô é escolhido como o primeiro elemento da lista.
    pivo = dados[inicio]
    # 'esq' começa um índice à frente do início.
    esq = inicio + 1
    # 'dir' começa no índice de fim.
    dir = fim
    # A flag é usada para indicar se a partição está completa.
    flag = False
    # Enquanto a partição não estiver completa, o loop continua.
    while not flag:
        # Enquanto os elementos à esquerda do pivô forem menores ou iguais a ele, 'esq' é incrementado.
        while esq <= dir and dados[esq] <= pivo:
            esq = esq + 1
        # Enquanto os elementos à direita do pivô forem maiores ou iguais a ele, 'dir' é decrementado.
        while dados[dir] >= pivo and dir >= esq:
            dir = dir - 1
        # Se 'dir' é menor que 'esq', a partição está completa.
        if dir < esq:
            flag = True
        else:
            # Troca os elementos de 'esq' e 'dir'.
            temp = dados[esq]
            dados[esq] = dados[dir]
            dados[dir] = temp
    # Troca o pivô com o elemento na posição 'dir' para colocá-lo na posição correta.
    temp = dados[inicio]
    dados[inicio] = dados[dir]
    dados[dir] = temp
    # Retorna a posição do pivô após a partição.
    return dir

# Programa Principal
# Lista de dados a serem ordenados.
dados = [50, 25, 92, 16, 76, 30, 43, 54, 19]
# Chamada da função quickSort para ordenar a lista.
quickSort(dados, 0, len(dados) - 1)
# Imprime a lista ordenada.
print(dados)
