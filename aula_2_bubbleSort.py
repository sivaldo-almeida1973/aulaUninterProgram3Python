def bubbleSort(dados):
    tam = len(dados)
    for v in range(0, tam, 1):
        for i in range(0, tam-1, 1):
            if dados[i] > dados[i+1]:
                aux = dados[i]
                dados[i] = dados[i+1]
                dados[i+1] = aux


#programa principal
dados = [5,4,2,1,8]
bubbleSort(dados)
print(dados)
