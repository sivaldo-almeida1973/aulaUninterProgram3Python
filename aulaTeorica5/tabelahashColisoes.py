# Função para calcular a posição na tabela hash com base nas duas primeiras letras da sigla
def hashFuncSigla(k, n):
    k = list(k)  # Converte a string da sigla em uma lista de caracteres
    return (ord(k[0]) + ord(k[1])) % n  # Soma os valores ASCII dos dois primeiros caracteres e aplica o módulo n

# Função para resolver colisões usando tentativa linear
def tentativaLinear(k, n, pos, tabelaHash):
  tentativa = pos  # Inicia a tentativa na posição calculada pela função hash
  while (tabelaHash[tentativa] != None):  # Enquanto a posição estiver ocupada
    tentativa += 1  # Avança para a próxima posição
    if tentativa == n:  # Se chegar ao final da tabela
      tentativa = 0  # Volta para o início da tabela
    if tentativa == pos:  # Se voltar à posição inicial
      tentativa = -1  # Indica que a tabela está cheia
      break  # Sai do loop
  return tentativa  # Retorna a nova posição ou -1 se a tabela estiver cheia

# Função para remover um elemento da tabela hash com tentativa linear
def tentativaLinearDel(k, n, pos, tabelaHash):
  tentativa = pos  # Inicia a tentativa na posição calculada pela função hash
  while (tabelaHash[tentativa] != k):  # Enquanto não encontrar o elemento
    tentativa += 1  # Avança para a próxima posição
    if tentativa == n:  # Se chegar ao final da tabela
      tentativa = 0  # Volta para o início da tabela
    if tentativa == pos:  # Se voltar à posição inicial
      tentativa = -1  # Indica que o elemento não foi encontrado
      break  # Sai do loop
  return tentativa  # Retorna a nova posição ou -1 se o elemento não foi encontrado

# Programa principal
n = 10  # Define o tamanho da tabela hash
tabelaHash = [None] * n  # Inicializa a tabela hash com 'None' em todas as posições

while True:  # Loop infinito para o menu de opções
  # Imprime as opções do menu
  print('1 - Inserir na tabela hash')
  print('2 - Remover na tabela hash')
  print('3 - Listar a tabela hash')
  print('4 - Sair')

  op = int(input("Escolha uma opção:"))  # Solicita ao usuário para escolher uma opção
  if op == 1:  # Opção 1: Inserir na tabela hash
    chave = input('Digite a sigla de um estado: ')  # Solicita a sigla do estado
    pos = hashFuncSigla(chave, n)  # Calcula a posição para a sigla
    if tabelaHash[pos] == None:  # Se a posição estiver vazia
        tabelaHash[pos] = chave  # Insere a sigla na posição calculada
    else:  # Se houver colisão
        pos = tentativaLinear(chave, n, pos, tabelaHash)  # Resolve a colisão com tentativa linear
        if pos != -1:  # Se encontrou uma posição livre
          tabelaHash[pos] = chave  # Insere a sigla na nova posição
        else:  # Se a tabela estiver cheia
          print('Tabela hash cheia. Impossível inserir!')  # Informa que não é possível inserir
  elif op == 2:  # Opção 2: Remover na tabela hash
    chave = input('Digite o que deseja remover: ')  # Solicita a sigla para remoção
    pos = hashFuncSigla(chave, n)  # Calcula a posição para a sigla
    if tabelaHash[pos] == chave:  # Se a sigla estiver na posição calculada
        tabelaHash[pos] = None  # Remove a sigla da posição
    else:  # Se houver colisão
        pos = tentativaLinearDel(chave, n, pos, tabelaHash)  # Resolve a colisão com tentativa linear para remoção
        if pos != -1:  # Se encontrou a sigla
          tabelaHash[pos] = None  # Remove a sigla da posição encontrada
        else:  # Se a sigla não foi encontrada
            print('Valor não localizado para a remoção!')  # Informa que a sigla não foi localizada
  elif op == 3:  # Opção 3: Listar a tabela hash
      print(tabelaHash)  # Imprime a tabela hash
  elif op == 4:  # Opção 4: Sair
    print('Encerrando...')  # Mensagem de encerramento
    break  # Sai do loop
  else:  # Se uma opção inválida for selecionada
    print("Selecione outra opção!\n")  # Solicita que o usuário selecione outra opção válida
