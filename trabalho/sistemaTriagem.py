class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.head = None

    def inserirSemPrioridade(self, novo_nodo):
        if not self.head:
            self.head = novo_nodo
        else:
            atual = self.head
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_nodo

    def inserirComPrioridade(self, novo_nodo):
        if not self.head or self.head.cor == 'V':
            novo_nodo.proximo = self.head
            self.head = novo_nodo
        else:
            atual = self.head
            while atual.proximo and atual.proximo.cor != 'V':
                atual = atual.proximo
            novo_nodo.proximo = atual.proximo
            atual.proximo = novo_nodo

    def inserir(self):
        cor = input('Informe a cor do cartão (A/V): ').upper()
        numero = int(input('Informe o número do cartão: '))
        novo_nodo = Nodo(numero, cor)
        if cor == 'A':
            self.inserirComPrioridade(novo_nodo)
        else:
            self.inserirSemPrioridade(novo_nodo)

    def mostrarFila(self):
        atual = self.head
        while atual:
            print(f'Cartão {atual.cor}{atual.numero}')
            atual = atual.proximo

    def chamarPaciente(self):
        if self.head:
            chamado = self.head
            print(f'Chamando paciente com cartão {chamado.cor}{chamado.numero}')
            print(f'Cliente da vez: Cartão {chamado.cor}{chamado.numero}')
            self.head = chamado.proximo
            chamado.proximo = None
        else:
            print('Não há pacientes na fila')
# Exemplo de uso da classe ListaEncadeada para criar a fila de triagem.
fila = ListaEncadeada()
while True:
    print('1 - Adicionar paciente a fila')
    print('2 - Mostrar pacientes na fila')
    print('3 - Chamar paciente')
    print('4 - Sair')
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        fila.inserir()
    elif opcao == '2':
        fila.mostrarFila()
    elif opcao == '3':
        fila.chamarPaciente()
    elif opcao == '4':
        break
    else:
        print('Opção inválida')
