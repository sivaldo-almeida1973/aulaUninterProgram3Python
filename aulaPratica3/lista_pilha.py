# Definição da função push para inserir um elemento na pilha
def push(pilha, top, tam, dado):
  # Verifica se a pilha está cheia comparando o tamanho atual com o tamanho máximo
  if len(pilha) == tam:
    print('Pilha cheia! Impossível inserir. ')
  else:
    # Insere o elemento na posição do topo e atualiza o topo
    pilha.insert(top, dado)
    top += 1
    return pilha, top

# Definição da função pop para remover o elemento do topo da pilha
def pop(pilha, top):
  # Verifica se a pilha está vazia
  if len(pilha) == 0:
    print('Pilha vazia! Impossível remover. ')
  else:
    # Remove o elemento do topo e atualiza o topo
    del pilha[top]
    top -= 1
    return pilha, top

# Programa principal
top = 0  # Inicializa a variável que representa o topo da pilha
pilha = []  # Inicializa a pilha como uma lista vazia
tam = 5  # Define o tamanho máximo da pilha

# Loop principal do programa
while True:
  # Exibe o menu de opções
  print('1 - Inserir na pilha')
  print('2 - Remover da pilha')
  print('3 - Listar a pilha')
  print('4 - Sair')

  # Solicita ao usuário que escolha uma opção
  op = int(input("Escolha uma opção:"))
  if op == 1:
    # Opção para inserir um elemento na pilha
    dado = int(input('Qual número deseja inserir?'))
    push(pilha, top, tam, dado)
  elif op == 2:
    # Opção para remover um elemento da pilha
    pop(pilha, top)
  elif op == 3:
    # Opção para listar todos os elementos da pilha
    for item in pilha:
      print(item)
  elif op == 4:
    # Opção para encerrar o programa
    print('Encerrando...')
    break
  else:
    # Caso uma opção inválida seja escolhida
    print("Selecione outra opção!\n")
