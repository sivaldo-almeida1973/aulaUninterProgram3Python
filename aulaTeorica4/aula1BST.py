class BST:
    # Construtor da classe BST.
    def __init__(self, dado=None):
        self.dado = dado  # Valor do nó.
        self.esquerda = None  # Referência para o filho esquerdo.
        self.direita = None  # Referência para o filho direito.

    # Método para inserir um novo valor na árvore.
    def inserir(self, dado):
        # Se o nó atual está vazio, insere o novo valor aqui.
        if (self.dado == None):
            self.dado = dado
        else:
            # Se o novo valor é menor que o valor do nó, insere na esquerda.
            if (dado < self.dado):
                # Se já existe um filho esquerdo, continua a inserção recursivamente.
                if (self.esquerda):
                    self.esquerda.inserir(dado)
                else:
                    # Se não há filho esquerdo, cria um novo nó com o valor.
                    self.esquerda = BST(dado)
            else:
                # Se o novo valor é maior ou igual, insere na direita.
                if(self.direita):
                    # Se já existe um filho direito, continua a inserção recursivamente.
                    self.direita.inserir(dado)
                else:
                    # Se não há filho direito, cria um novo nó com o valor.
                    self.direita = BST(dado)

    # Método para percorrer a árvore em ordem (esquerda, raiz, direita).
    def emOrdem(self, lst):
        # Visita a subárvore esquerda primeiro.
        if (self.esquerda):
            self.esquerda.emOrdem(lst)
        # Adiciona o valor do nó atual à lista.
        lst.append(self.dado)
        # Visita a subárvore direita.
        if (self.direita):
            self.direita.emOrdem(lst)
        # Retorna a lista com os valores em ordem.
        return lst

    # Método para percorrer a árvore em pré-ordem (raiz, esquerda, direita).
    def preOrdem(self, lst):
        # Adiciona o valor do nó atual à lista primeiro.
        lst.append(self.dado)
        # Visita a subárvore esquerda.
        if (self.esquerda):
            self.esquerda.preOrdem(lst)
        # Visita a subárvore direita.
        if (self.direita):
            self.direita.preOrdem(lst)
        # Retorna a lista com os valores em pré-ordem.
        return lst

    # Método para percorrer a árvore em pós-ordem (esquerda, direita, raiz).
    def posOrdem(self, lst):
        # Visita a subárvore esquerda primeiro.
        if (self.esquerda):
            self.esquerda.posOrdem(lst)
        # Visita a subárvore direita.
        if (self.direita):
            self.direita.posOrdem(lst)
        # Adiciona o valor do nó atual à lista por último.
        lst.append(self.dado)
        # Retorna a lista com os valores em pós-ordem.
        return lst

    # Método para percorrer a árvore por níveis (largura).
    def emNivel(self):
        nodoAtual = self  # Começa pelo nó raiz.
        lst = []  # Lista para armazenar os valores dos nós.
        fila = []  # Fila para organizar a ordem de visita dos nós.
        fila.insert(0,nodoAtual)  # Insere o nó raiz na fila.
        # Enquanto houver nós na fila, continua o percurso.
        while(len(fila) > 0):
            nodoAtual = fila.pop()  # Remove o nó da frente da fila.
            lst.append(nodoAtual.dado)  # Adiciona o valor do nó à lista.
            # Se há filho esquerdo, insere na fila.
            if(nodoAtual.esquerda):
                fila.insert(0,nodoAtual.esquerda)
            # Se há filho direito, insere na fila.
            if(nodoAtual.direita):
                fila.insert(0,nodoAtual.direita)
        # Retorna a lista com os valores dos nós por nível.
        return lst

# Criação de uma instância da árvore BST.
Teste = BST()

# Inserção de valores na árvore.
Teste.inserir(7)
Teste.inserir(4)
Teste.inserir(9)
Teste.inserir(0)
Teste.inserir(5)
Teste.inserir(8)

#          7
#        /  \
#      /     \
#     4        9
#    / \      /  \
#   0   5    8    13

print('Em ordem: ', Teste.emOrdem([]))
print('Em pré-ordem: ', Teste.preOrdem([]))
print('Em pós-ordem: ', Teste.posOrdem([]))

print('Em nível: ', Teste.emNivel())
