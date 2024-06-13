class ElementoDaListaSimples:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

    def __repr__(self):
        return self.dado

class ListaEncadeadaSimples:
    def __init__(self, nodos=None):
        self.head = None
        if nodos is not None:
            self.head = ElementoDaListaSimples(dado=nodos.pop(0))
            nodo_atual = self.head
            for elem in nodos:
                nodo_atual.proximo = ElementoDaListaSimples(dado=elem)
                nodo_atual = nodo_atual.proximo

    def __repr__(self):
        nodos = [nodo.dado for nodo in self] + ["None"]
        return " -> ".join(nodos)

    def __iter__(self):
        nodo_atual = self.head
        while nodo_atual is not None:
            yield nodo_atual
            nodo_atual = nodo_atual.proximo

    def inserir(self, dado, no_inicio=False):
        novo_nodo = ElementoDaListaSimples(dado)
        if no_inicio or not self.head:
            novo_nodo.proximo = self.head
            self.head = novo_nodo
        else:
            nodo_atual = self.head
            while nodo_atual.proximo:
                nodo_atual = nodo_atual.proximo
            nodo_atual.proximo = novo_nodo

    def deletar(self, dado):
        if not self.head:
            raise Exception("A lista está vazia!")

        if self.head.dado == dado:
            self.head = self.head.proximo
            return

        nodo_anterior = self.head
        for nodo in self:
            if nodo.dado == dado:
                nodo_anterior.proximo = nodo.proximo
                return
            nodo_anterior = nodo

        raise Exception(f"Nó com o dado '{dado}' não foi encontrado.")

def menu_lista_encadeada(lista):
    while True:
        print('1 - Inserir no início da lista encadeada')
        print('2 - Inserir no final da lista encadeada')
        print('3 - Remover da lista encadeada')
        print('4 - Imprimir a lista encadeada')
        print('5 - Sair')

        op = int(input("Escolha uma opção: "))
        if op == 1:
            dado = input('Qual número deseja inserir? ')
            lista.inserir(dado, no_inicio=True)
        elif op == 2:
            dado = input('Qual número deseja inserir? ')
            lista.inserir(dado)
        elif op == 3:
            dado = input('Qual número deseja remover? ')
            lista.deletar(dado)
        elif op == 4:
            print(lista)
        elif op == 5:
            print('Encerrando...')
            break
        else:
            print("Selecione outra opção!\n")

# Uso do código refatorado
Teste = ListaEncadeadaSimples()
menu_lista_encadeada(Teste)
