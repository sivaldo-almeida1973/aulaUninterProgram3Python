# Definição da função push para inserir um elemento no topo da pilha
def push(pilha, tam, dado):
  # Verifica se a pilha está cheia
  if len(pilha) >= tam:
    print('Pilha cheia! Impossível inserir.')
  else:
    # Insere o elemento no topo da pilha
    pilha.append(dado)

# Definição da função pop para remover o elemento do topo da pilha
def pop(pilha):
  # Verifica se a pilha está vazia
  if not pilha:
    print('Pilha vazia! Impossível remover.')
  else:
    # Remove e retorna o elemento do topo da pilha
    return pilha.pop()

# Programa principal
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
    # Loop para inserção contínua de elementos na pilha
    while True:
      # Solicita ao usuário um número para inserir na pilha
      dado = int(input('Qual número deseja inserir? (Digite -1 para parar): '))
      # Verifica se o usuário deseja parar a inserção
      if dado == -1:
        break
      # Chama a função push para inserir o elemento na pilha
      push(pilha, tam, dado)
  elif op == 2:
    while True:
        # Chama a função pop para remover o elemento do topo da pilha
        removido = pop\
          (pilha)

        if removido is not None:
            print(f'Elemento {removido} removido.')
        else:
            print('Não há mais elementos para remover.')

        # Pergunta ao usuário se ele deseja continuar removendo elementos
        continuar = input('Deseja remover outro elemento? (s/n): ')
        if continuar.lower() != 's':
            break
  elif op == 3:
    # Lista todos os elementos da pilha
    print('Elementos da pilha:')
    for item in reversed(pilha):
      print(item)
  elif op == 4:
    # Encerra o programa
    print('Encerrando...')
    break
  else:
    # Caso uma opção inválida seja escolhida
    print("Selecione outra opção!\n")
