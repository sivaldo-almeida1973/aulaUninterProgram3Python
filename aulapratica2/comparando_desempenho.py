import time  # Importa o módulo time para medir o tempo de execução.
import random  # Importa o módulo random para gerar números aleatórios.

# Definição da função bubbleSort, que ordena uma lista de números.
def bubbleSort(dados):
  # 'tam' recebe o tamanho da lista 'dados'.
  tam = len(dados)
  # Loop externo que percorre toda a lista.
  for v in range(0, tam, 1):
    # Loop interno que compara elementos adjacentes.
    for i in range(0, tam-1, 1):
      # Se o elemento atual é maior que o próximo, eles são trocados.
      if dados[i] > dados[i+1]:
        # 'aux' armazena temporariamente o valor de 'dados[i]'.
        aux = dados[i]
        # O elemento atual recebe o valor do próximo.
        dados[i] = dados[i+1]
        # O próximo elemento recebe o valor armazenado em 'aux'.
        dados[i+1] = aux

# Programa Principal

# Cria uma lista vazia chamada 'dados'.
dados = []
# Preenche a lista 'dados' com 1000 números aleatórios entre 1 e 9999.
for i in range(0, 1000):
    n = random.randint(1, 9999)
    dados.append(n)
# A linha abaixo, se descomentada, imprimiria a lista 'dados' antes da ordenação.
# print(dados)

# Armazena o tempo atual em 'tic' antes de iniciar a ordenação.
tic = time.perf_counter()
# Chamada da função bubbleSort para ordenar a lista 'dados'.
bubbleSort(dados)
# Armazena o tempo atual em 'toc' após a conclusão da ordenação.
toc = time.perf_counter()

# Calcula a diferença entre 'toc' e 'tic' para determinar o tempo de execução e imprime o resultado.
print(f'Tempo: {toc - tic:0.4f} s')  # Imprime o tempo de execução do algoritmo em segundos.
