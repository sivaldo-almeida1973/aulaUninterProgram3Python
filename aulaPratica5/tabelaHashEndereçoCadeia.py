# Classe para representar um elemento individual na lista encadeada
class ElementoDaListaSimples:
    def __init__(self, chave=None, dado=None):
        self.chave = chave  # A chave do elemento
        self.dado = dado  # O dado associado à chave
        self.proximo = None  # O ponteiro para o próximo elemento na lista

# Classe para representar uma lista encadeada simples
class ListaEncadeadaSimples:
    def __init__(self):
        self.head = None  # O início da lista

    # Método para inserir um novo elemento no início da lista
    def inserir(self, chave, dado):
        nodo = ElementoDaListaSimples(chave, dado)  # Cria um novo elemento
        if self.head == None:  # Se a lista estiver vazia
            self.head = nodo  # O novo elemento é o início da lista
            return 0
        else:  # Se a lista não estiver vazia
            nodo.proximo = self.head  # O novo elemento aponta para o antigo início
            self.head = nodo  # O novo elemento se torna o novo início da lista
            return 0

    # Método para imprimir todos os elementos da lista
    def imprimir(self):
        temp = self.head  # Começa pelo início da lista
        while temp:  # Enquanto houver elementos
            print(f"{temp.chave}\t{temp.dado}")  # Imprime a chave e o dado
            temp = temp.proximo  # Move para o próximo elemento

# Classe para representar uma tabela hash usando listas encadeadas para resolver colisões
class TabelaHash:
    def __init__(self):
        self.tam = 10  # O tamanho da tabela hash
        self.length = 0  # O número de elementos na tabela
        self.h = [ListaEncadeadaSimples() for i in range(0, self.tam)]  # Inicializa as listas encadeadas

    # Função hash para calcular a posição de um elemento
    def hashFunc(self, k):
        k = list(k)  # Converte a chave em uma lista de caracteres
        return (ord(k[0]) + ord(k[1])) % self.tam  # Soma os valores ASCII dos dois primeiros caracteres e aplica o módulo

    # Método para inserir um novo elemento na tabela hash
    def inserir(self, chave, dado):
        pos = self.hashFunc(chave)  # Calcula a posição usando a função hash
        add = self.h[pos].inserir(chave, dado)  # Insere o elemento na lista encadeada correspondente

    # Método para imprimir todos os elementos da tabela hash
    def imprimir(self):
        for i in range(0, self.tam):  # Para cada lista encadeada na tabela
            self.h[i].imprimir()  # Imprime os elementos da lista

# Programa principal
Teste = TabelaHash()  # Cria uma nova tabela hash
while True:  # Loop infinito para o menu de opções
  print('1 - Inserir na tabela hash')
  print('2 - Remover na tabela hash')
  print('3 - Listar a tabela hash')
  print('4 - Sair')

  op = int(input("Escolha uma opção:"))  # Solicita a opção do usuário
  if op == 1:  # Se a opção for inserir
    chave = input('Digite a sigla de um estado: ')  # Solicita a chave
    dado = input('Digite o nome do estado: ')  # Solicita o dado
    Teste.inserir(chave, dado)  # Insere na tabela hash
  elif op == 2:
    chave = input('Digite o que deseja remover: ')
    # IMPLEMENTAR a remoção
  elif op == 3:  # Se a opção for listar
      Teste.imprimir()  # Imprime a tabela hash
  elif op == 4:  # Se a opção for sair
    print('Encerrando...')  # Mensagem de encerramento
    break  # Encerra o loop
  else:  # Se a opção for inválida
    print("Selecione outra opção!\n")  # Solicita uma nova opção
