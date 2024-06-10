def bubbleSort(dados):
    # Determina o tamanho da lista
    tam = len(dados)
    # Loop externo para passar por toda a lista
    for v in range(tam):
        # Loop interno para comparar os elementos adjacentes
        for i in range(tam - 1):
            # Se o elemento atual é maior que o próximo
            if dados[i] > dados[i + 1]:
                # Troca os elementos de lugar
                aux = dados[i]
                dados[i] = dados[i + 1]
                dados[i + 1] = aux

# Programa principal
dados = [5, 4, 2, 1, 8]
bubbleSort(dados)
print(dados)  # Saída será a lista ordenada: [1, 2, 4, 5, 8]

# Aqui está o que cada parte do código faz:

# bubbleSort(dados): Define a função que ordenará a lista dados.
# tam = len(dados): Armazena o tamanho da lista dados.
# for v in range(tam): Inicia um loop que passará pela lista várias vezes.
# for i in range(tam - 1): Inicia um loop aninhado que compara elementos adjacentes.
# if dados[i] > dados[i + 1]: Verifica se o elemento atual é maior que o próximo.
# aux = dados[i]: Se for maior, armazena o elemento atual em uma variável auxiliar.
# dados[i] = dados[i + 1]: Atribui o próximo elemento à posição atual.
# dados[i + 1] = aux: Coloca o elemento armazenado na variável auxiliar na próxima posição.
# print(dados): Imprime a lista dados após a ordenação.
#
# O Bubble Sort é um algoritmo simples de ordenação que funciona “borbulhando” os maiores elementos para o final da lista através de sucessivas trocas. Embora seja fácil de entender e implementar, não é o mais eficiente para listas grandes, pois sua complexidade é de O(n2)
# , onde n
#  é o número de elementos na lista. Espero que isso ajude a esclarecer como o código funciona! Se tiver mais alguma dúvida ou precisar de mais ajuda, estou à disposição.
