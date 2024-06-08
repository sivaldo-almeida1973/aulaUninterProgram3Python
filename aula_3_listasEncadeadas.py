#Cria cada elemento da lista
class ElementoDaListaSimples:
# construtor de inicialização da classe
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
#__repr__ é um método especial do Python
#use-o para criar a maneira como objeto
#é mostrado fora da função print
    def __repr__(self):
        return self.dado

#Cria a lista encadeada simples
class ListaEncadeadaSimples:

    def __init__(self, nodos=None):
        self.head = None
        if nodos is not None:
            nodo = ElementoDaListaSimples(dado=nodos.pop(0))
            self.head = nodo
            for elem in nodos:
                nodo.proximo = ElementoDaListaSimples(dado=elem)
                nodo = nodo.proximo

    def __repr__(self):
        nodo = self.head
        nodos = []
        while nodo is not None:
            nodos.append(nodo.dado)
            nodo = nodo.proximo
        nodos.append("None")
        return " -> ".join(nodos)


    def inserirNoInicio(self, nodo):
        nodo.proximo = self.head


    def inserirNoFinal(self, nodo):
        if self.head is None:
            self.head = nodo
            return
        nodo_atual = self.head
        while nodo_atual.proximo != None:
            nodo_atual = nodo_atual.proximo
        nodo_atual.proximo = nodo
        return
