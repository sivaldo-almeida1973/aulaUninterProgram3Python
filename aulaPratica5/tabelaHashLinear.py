# Função para calcular o valor hash de uma sigla usando os dois primeiros caracteres
def hashFuncSigla(k, n):
    k = list(k)  # Converte a string em uma lista de caracteres
    return (ord(k[0]) + ord(k[1])) % n  # Soma os valores ASCII dos dois primeiros caracteres e aplica o módulo n

# Função para resolver colisões na tabela hash usando tentativa linear
def tentativaLinear(k, n, pos, tabelaHash):
  tentativa = pos  # Inicia a tentativa na posição calculada pelo hash
  while (tabelaHash[tentativa] != None):  # Enquanto a posição estiver ocupada
    tentativa += 1  # Avança para a próxima posição
    if tentativa == n:  # Se chegar ao fim da tabela
      tentativa = 0  # Volta para o início
    if tentativa == pos:  # Se voltar à posição inicial
      tentativa = -1  # Indica que não há espaço disponível
      break
  return tentativa  # Retorna a nova posição ou -1 se não encontrou

# Função para remover um elemento da tabela hash com tentativa linear
def tentativaLinearDel(k, n, pos, tabelaHash):
  tentativa = pos  # Inicia a tentativa na posição calculada pelo hash
  while (tabelaHash[tentativa] != k):  # Enquanto não encontrar o elemento
    tentativa += 1  # Avança para a próxima posição
    if tentativa == n:  # Se chegar ao fim da tabela
      tentativa = 0  # Volta para o início
    if tentativa == pos:  # Se voltar à posição inicial
      tentativa = -1  # Indica que o elemento não foi encontrado
      break
  return tentativa  # Retorna a posição do elemento ou -1 se não encontrou

# Programa principal
n = 10  # Define o tamanho da tabela hash
tabelaHash = [None] * n  # Inicializa a tabela hash com None

while True:  # Loop infinito para o menu de opções
  print('1 - Inserir na tabela hash')
  print('2 - Remover na tabela hash')
  print('3 - Listar a tabela hash')
  print('4 - Sair')

  op = int(input("Escolha uma opção:"))  # Solicita a opção do usuário
  if op == 1:  # Opção de inserção
    chave = input('Digite a sigla de um estado: ')  # Solicita a sigla para inserção
    pos = hashFuncSigla(chave, n)  # Calcula a posição hash
    if tabelaHash[pos] == None:  # Se a posição estiver livre
        tabelaHash[pos] = chave  # Insere a sigla
    else:  # Se ocorrer colisão
        pos = tentativaLinear(chave, n, pos, tabelaHash)  # Resolve a colisão
        if pos != -1:  # Se encontrou posição
          tabelaHash[pos] = chave  # Insere a sigla
        else:  # Se a tabela estiver cheia
          print('Tabela hash cheia. Impossível inserir!')
  elif op == 2:  # Opção de remoção
    chave = input('Digite o que deseja remover: ')  # Solicita a sigla para remoção
    pos = hashFuncSigla(chave, n)  # Calcula a posição hash
    if tabelaHash[pos] == chave:  # Se a sigla estiver na posição calculada
        tabelaHash[pos] = None  # Remove a sigla
    else:  # Se ocorrer colisão
        pos = tentativaLinearDel(chave, n, pos, tabelaHash)  # Tenta localizar a sigla
        if pos != -1:  # Se encontrou a sigla
          tabelaHash[pos] = None  # Remove a sigla
        else:  # Se não encontrou a sigla
            print('Valor não localizado para a remoção!')
  elif op == 3:  # Opção de listagem
      print(tabelaHash)  # Exibe a tabela hash
  elif op == 4:  # Opção de saída
    print('Encerrando...')  # Mensagem de encerramento
    break  # Encerra o loop
  else:  # Opção inválida
    print("Selecione outra opção!\n")  # Solicita uma nova opção
