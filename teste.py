X = [6, 5, 2, 3, 4, 1]  # Lista inicial a ser ordenada
n = 0  # Contador de passagens pelo loop
troca = 1  # Variável de controle para verificar se houve trocas

# O loop continua enquanto não passar por toda a lista e enquanto houver trocas
while n <= len(X) and troca == 1:
    troca = 0  # Reseta a variável de controle de trocas
    # Loop interno que percorre a lista da primeira até a penúltima posição
    for i in range(0, len(X)-1, 1):
        # Se o elemento atual é maior que o próximo, eles são trocados
        if X[i] > X[i+1]:
            troca = 1  # Indica que uma troca ocorreu
            # Troca os elementos de lugar
            aux = X[i]
            X[i] = X[i+1]
            X[i+1] = aux
    n = n + 1  # Incrementa o contador de passagens


# Código gerado por IA. Examine e use com cuidado. Mais informações em perguntas frequentes.
# Aqui estão as razões pelas quais este código é um Bubble Sort:
#
# Comparação e Troca de Elementos Adjacentes: O algoritmo compara elementos adjacentes na lista (X[i] e X[i+1]) e os troca se estiverem na ordem incorreta (se X[i] > X[i+1]).
# Passagem pela Lista: O algoritmo faz várias passagens pela lista até que não haja mais trocas necessárias, indicando que a lista está ordenada.
# Variável de Controle de Trocas: A variável troca é usada para rastrear se alguma troca foi feita durante uma passagem. Se nenhuma troca for feita, o algoritmo conclui que a lista está ordenada e termina o loop.
# Eficiência: O Bubble Sort é conhecido por sua simplicidade, mas não é o mais eficiente para listas grandes, pois tem uma complexidade de tempo O(n²), onde n é o número de elementos na lista.
