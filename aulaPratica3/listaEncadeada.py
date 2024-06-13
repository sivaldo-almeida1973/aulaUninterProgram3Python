# Classe para representar cada elemento da lista encadeada
class ElementoDaListaSimples:
    # Construtor que inicializa um novo elemento
    def __init__(self, dado):
        self.dado = dado  # Armazena o valor do elemento
        self.proximo = None  # Inicializa o próximo elemento como None

    # Método especial para definir a representação em string do elemento
    def __repr__(self):
        return self.dado  # Retorna o valor do elemento como string

# Classe para representar a lista encadeada como um todo
class ListaEncadeadaSimples:
    # Construtor que inicializa a lista encadeada
    def __init__(self, nodos=None):
        self.head = None  # Inicializa a cabeça da lista como None
        # Se uma lista de nodos é fornecida, preenche a lista encadeada
        if nodos is not None:
            nodo = ElementoDaListaSimples(dado=nodos.pop(0))  # Cria o primeiro elemento
            self.head = nodo  # Define o primeiro elemento como cabeça da lista
            # Para cada elemento na lista fornecida, cria um novo elemento e o conecta ao anterior
            for elem in nodos:
                nodo.proximo = ElementoDaListaSimples(dado=elem)
                nodo = nodo.proximo

    # Método especial para definir a representação em string da lista encadeada
    def __repr__(self):
        nodo = self.head  # Começa pela cabeça da lista
        nodos = []  # Lista para armazenar os valores dos elementos
        # Enquanto existirem elementos na lista, adiciona seus valores à lista de nodos
        while nodo is not None:
            nodos.append(nodo.dado)
            nodo = nodo.proximo
        nodos.append("None")  # Adiciona "None" ao final para indicar o fim da lista
        return " -> ".join(nodos)  # Retorna a representação em string da lista

    # Método para iterar sobre a lista encadeada
    def __iter__(self):
        nodo = self.head  # Começa pela cabeça da lista
        # Enquanto existirem elementos, gera cada um deles
        while nodo is not None:
            yield nodo
            nodo = nodo.proximo

    # Método para inserir um novo elemento no início da lista
    def inserirNoInicio(self, nodo):
        nodo.proximo = self.head  # Conecta o novo elemento ao primeiro elemento atual
        self.head = nodo  # Define o novo elemento como a nova cabeça da lista

    # Método para inserir um novo elemento no final da lista
    def inserirNoFinal(self, nodo):
        if self.head is None:
            self.head = nodo  # Se a lista está vazia, define o novo elemento como cabeça
            return
        # Caso contrário, percorre a lista até encontrar o último elemento
        nodo_atual = self.head
        while nodo_atual.proximo is not None:
            nodo_atual = nodo_atual.proximo
        # Conecta o novo elemento ao final da lista
        nodo_atual.proximo = nodo

    # Método para deletar um elemento com um valor específico da lista
    def deletar(self, dado):
        if self.head is None:
            raise Exception("A lista está vazia!")  # Lança uma exceção se a lista está vazia

        # Se o elemento a ser deletado é a cabeça da lista, redefine a cabeça
        if self.head.dado == dado:
            self.head = self.head.proximo
            return

        # Caso contrário, percorre a lista até encontrar o elemento a ser deletado
        nodo_anterior = self.head
        for nodo in self:
            if nodo.dado == dado:
                nodo_anterior.proximo = nodo.proximo  # Remove o elemento da lista
                return
            nodo_anterior = nodo

        # Se o elemento não foi encontrado, lança uma exceção
        raise Exception(f"Nó com o dado '{dado}' não foi encontrado.")
# Cria uma instância da ListaEncadeadaSimples chamada Teste
Teste = ListaEncadeadaSimples()

# Loop infinito para manter o programa rodando até que o usuário decida sair
while True:
  # Imprime o menu de opções para o usuário
  print('1 - Inserir na início da lista encadeada')
  print('2 - Inserir na final da lista encadeada')
  print('3 - Remover da lista encadeada')
  print('4 - Imprimir a lista encadeada')
  print('5 - Sair')

  # Solicita ao usuário que escolha uma opção e armazena na variável 'op'
  op = int(input("Escolha uma opção:"))
  # Se a opção for 1, solicita um dado e insere no início da lista
  if op == 1:
    dado = input('Qual número deseja inserir?')
    Teste.inserirNoInicio(ElementoDaListaSimples(dado))
  # Se a opção for 2, solicita um dado e insere no final da lista
  if op == 2:
    dado = input('Qual número deseja inserir?')
    Teste.inserirNoFinal(ElementoDaListaSimples(dado))
  # Se a opção for 3, solicita um dado e remove da lista
  elif op == 3:
    dado = input('Qual número deseja remover?')
    Teste.deletar(dado)
  # Se a opção for 4, percorre a lista e imprime cada elemento
  elif op == 4:
    for nodo in Teste:
      print(nodo, end=' -> ')
    print('None')  # Imprime 'None' no final para indicar o fim da lista
  # Se a opção for 5, encerra o loop e o programa
  elif op == 5:
    print('Encerrando...')
    break
  # Se nenhuma das opções anteriores for escolhida, pede para selecionar outra opção
  else:
    print("Selecione outra opção!\n")
