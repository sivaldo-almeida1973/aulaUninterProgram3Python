
# Classe para representar cada elemento da lista encadeada
class ElementoDaListaSimples:
    # Construtor para inicializar o elemento com um dado e sem um próximo elemento
    def __init__(self, dado):
        self.dado = dado  # Armazena o dado fornecido
        self.proximo = None  # Inicialmente, não há um próximo elemento

    # Método especial para representar o elemento como uma string
    def __repr__(self):
        return self.dado  # Retorna o dado quando o elemento é impresso

# Classe para criar e manipular a lista encadeada simples
class ListaEncadeadaSimples:
    # Construtor para inicializar a lista encadeada
    def __init__(self, nodos=None):
        self.head = None  # Inicializa o primeiro elemento da lista como None
        # Se uma lista de nodos é fornecida, preenche a lista encadeada com esses nodos
        if nodos is not None:
            nodo = ElementoDaListaSimples(dado=nodos.pop(0))  # Cria o primeiro elemento
            self.head = nodo  # Define o primeiro elemento como cabeça da lista
            for elem in nodos:  # Para cada dado restante na lista de nodos
                nodo.proximo = ElementoDaListaSimples(dado=elem)  # Cria um novo elemento e o conecta ao anterior
                nodo = nodo.proximo  # Move para o próximo elemento

    # Método especial para representar a lista encadeada como uma string
    def __repr__(self):
        nodo = self.head  # Começa pelo primeiro elemento
        nodos = []  # Lista para armazenar os dados dos elementos
        while nodo is not None:  # Enquanto existirem elementos na lista
            nodos.append(nodo.dado)  # Adiciona o dado do elemento atual à lista
            nodo = nodo.proximo  # Move para o próximo elemento
        nodos.append("None")  # Adiciona "None" ao final para representar o fim da lista
        return " -> ".join(nodos)  # Retorna uma string com os dados dos elementos conectados por '->'

    # Método para permitir a iteração sobre a lista encadeada
    def __iter__(self):
        nodo = self.head  # Começa pelo primeiro elemento
        while nodo is not None:  # Enquanto existirem elementos
            yield nodo  # Retorna o elemento atual e pausa a execução
            nodo = nodo.proximo  # Move para o próximo elemento

    # Método para inserir um novo elemento no início da lista
    def inserirNoInicio(self, nodo):
        nodo.proximo = self.head  # Conecta o novo elemento ao primeiro elemento atual
        self.head = nodo  # Define o novo elemento como o primeiro da lista

    # Método para inserir um novo elemento no final da lista
    def inserirNoFinal(self, nodo):
        if self.head is None:  # Se a lista estiver vazia
            self.head = nodo  # O novo elemento é o primeiro da lista
            return
        # Se a lista não estiver vazia, percorre até encontrar o último elemento
        nodo_atual = self.head
        while nodo_atual.proximo != None:
            nodo_atual = nodo_atual.proximo
        nodo_atual.proximo = nodo  # Conecta o novo elemento ao final da lista

    # Método para deletar um elemento com um dado específico
    def deletar(self, dado):
        if self.head is None:  # Se a lista estiver vazia, lança uma exceção
            raise Exception("A lista está vazia!")
        if self.head.dado == dado:  # Se o dado a ser deletado estiver no primeiro elemento
            self.head = self.head.proximo  # Remove o primeiro elemento
            return
        nodo_anterior = self.head
        for nodo in self:  # Percorre a lista em busca do dado
            if nodo.dado == dado:  # Se encontrar o dado
                nodo_anterior.proximo = nodo.proximo  # Remove o elemento da lista
                return
            nodo_anterior = nodo  # Atualiza o elemento anterior
        # Se o dado não for encontrado, lança uma exceção
        raise Exception("Nó com o dado '%s' não foi econtrado." % dado)

# Cria uma lista encadeada simples sem elementos
Teste = ListaEncadeadaSimples()

# Insere um elemento com o dado '40' no início da lista
Teste.inserirNoInicio(ElementoDaListaSimples('40'))
# Continuação da inserção de elementos na lista encadeada
Teste.inserirNoInicio(ElementoDaListaSimples('4'))  # Insere '4' no início da lista
Teste.inserirNoInicio(ElementoDaListaSimples('15')) # Insere '15' no início da lista
Teste.inserirNoInicio(ElementoDaListaSimples('7'))  # Insere '7' no início da lista

# Continuação da inserção de elementos no final da lista
Teste.inserirNoFinal(ElementoDaListaSimples('12'))  # Insere '12' no final da lista
Teste.inserirNoFinal(ElementoDaListaSimples('24'))  # Insere '24' no final da lista

# Varre a lista e imprime cada elemento seguido por ' -> '
for nodo in Teste:
  print(nodo, end=' -> ')
print('None')  # Imprime 'None' no final para indicar o fim da lista

# Deleta o elemento com o dado '4' da lista
Teste.deletar('4')

# Varre a lista novamente e imprime cada elemento após a deleção
for nodo in Teste:
  print(nodo, end=' -> ')
print('None')  # Imprime 'None' no final para indicar o fim da lista
