# Inicializa uma lista vazia chamada 'fila' que vai armazenar os elementos
fila = []
# Define o tamanho máximo da fila como 5
tam = 5

# Inicia um loop infinito que vai rodar até o usuário decidir sair
while True:
  # Imprime as opções disponíveis para o usuário
  print('1 - Inserir na fila')
  print('2 - Remover da fila')
  print('3 - Listar a fila')
  print('4 - Sair')

  # Pede ao usuário para escolher uma opção e armazena na variável 'op'
  op = int(input("Escolha uma opção:"))
  if op == 1:
    # Se a opção for 1, pede um número para inserir na fila
    dado = int(input('Qual número deseja inserir?'))
    # Verifica se a fila ainda tem espaço
    if len(fila) < tam:
      # Se tiver espaço, adiciona o número no final da fila
      fila.append(dado)
    else:
      # Se não tiver espaço, informa que a fila está cheia
      print('Fila cheia! Impossível inserir. ')
  elif op == 2:
    # Se a opção for 2, verifica se a fila não está vazia
    if len(fila) > 0:
      # Se não estiver vazia, remove o primeiro elemento da fila
      fila.pop(0)
    else:
      # Se estiver vazia, informa que não é possível remover
      print('Fila vazia! Impossível remover. ')
  elif op == 3:
    # Se a opção for 3, lista todos os elementos da fila
    for item in fila:
      print(item, end=' ')
    # Adiciona uma quebra de linha no final da listagem
    print('\n')
  elif op == 4:
    # Se a opção for 4, imprime uma mensagem de encerramento e sai do loop
    print('Encerrando...')
    break
  else:
    # Se o usuário escolher uma opção inválida, pede para tentar novamente
    print("Selecione outra opção!\n")
