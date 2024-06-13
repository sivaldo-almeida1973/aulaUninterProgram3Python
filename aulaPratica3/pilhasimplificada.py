#VERSÃO SIMPLIFICADO DO PYTHON
pilha = []
tam = 5

while True:
  print('1 - Inserir na pilha')
  print('2 - Remover da pilha')
  print('3 - Listar a pilha')
  print('4 - Sair')

  op = int(input("Escolha uma opção:"))
  if op ==1:
    dado = int(input('Qual número deseja inserir?'))
    if len(pilha) < 5:
      pilha.append(dado)
    else:
      print('Pilha cheia! Impossível inserir. ')
  elif op == 2:
    if len(pilha) > 0:
      pilha.pop()
    else:
      print('Pilha vazia! Impossível remover. ')
  elif op == 3:
    pilha.reverse()
    for item in pilha:
      print(item)
  elif op == 4:
    print('Encerrando...')
    break
  else:
    print("Selecione outra opção!\n")
