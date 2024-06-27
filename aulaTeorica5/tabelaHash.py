# Função para calcular a posição na tabela hash com base nas duas primeiras letras da sigla
def hashFuncSigla(k, n):
    k = list(k)  # Converte a string da sigla em uma lista de caracteres
    return (ord(k[0]) + ord(k[1])) % n  # Soma os valores ASCII dos dois primeiros caracteres e aplica o módulo n

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
        if tabelaHash[pos] == None:  # Verifica se a posição está vazia
             tabelaHash.insert(pos, chave)  # Insere a sigla na posição calculada
        else:
          print('Já existe um dado neste lugar!')  # Avisa se a posição já estiver ocupada
    elif op == 2:  # Opção 2: Remover na tabela hash
        chave = input('Digite a sigla do estado que deseja remover: ')  # Solicita a sigla para remoção
        pos = hashFuncSigla(chave, n)  # Calcula a posição para a sigla
        if tabelaHash[pos] == chave:  # Verifica se a sigla está na posição calculada
          tabelaHash.pop(pos)  # Remove a sigla da posição
        else:
          print('Valor não localizado para a remoção!')  # Avisa se a sigla não for encontrada
    elif op == 3:  # Opção 3: Listar a tabela hash
        print(tabelaHash)  # Imprime a tabela hash
    elif op == 4:  # Opção 4: Sair
      print('Encerrando...')  # Mensagem de encerramento
      break  # Sai do loop
    else:  # Caso seja digitada uma opção inválida
      print("Selecione outra opção!\n")  # Solicita que o usuário selecione outra opção
