def mergeSort(dados):
    # Verifica se a lista tem mais de um elemento
    if len(dados) > 1:
        # Divide a lista ao meio
        meio = len(dados)//2
        esquerda = dados[:meio]
        direita = dados[meio:]

        # Ordena as duas metades
        mergeSort(esquerda)
        mergeSort(direita)

        # Mescla as duas metades ordenadas
        i = j = k = 0
        # Enquanto houver elementos em ambas as metades
        while i < len(esquerda) and j < len(direita):
            # Escolhe o menor elemento e coloca na lista original
            if esquerda[i] < direita[j]:
                dados[k] = esquerda[i]
                i += 1
            else:
                dados[k] = direita[j]
                j += 1
            k += 1

        # Se sobrarem elementos na metade esquerda, adiciona à lista
        while i < len(esquerda):
            dados[k] = esquerda[i]
            i += 1
            k += 1

        # Se sobrarem elementos na metade direita, adiciona à lista
        while j < len(direita):
            dados[k] = direita[j]
            j += 1
            k += 1

# Programa principal
dados = [54, 26, 93, 17, 77, 31, 44, 55]
mergeSort(dados)
print(dados)  # Saída: [17, 26, 31, 44, 54, 55, 77, 93]
