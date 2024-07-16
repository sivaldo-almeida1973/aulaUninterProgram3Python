class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero   # Número do cartão do paciente.
        self.cor = cor         # Cor do cartão do paciente (A para amarelo, V para verde).
        self.proximo = None    # Referência ao próximo Nodo na fila.

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

    def inserir(self, cor, numero):
        novo_nodo = Nodo(numero, cor)
        if cor == 'V':
            self.inserirSemPrioridade(novo_nodo)
        elif cor == 'A':
            self.inserirComPrioridade(novo_nodo)

    def mostrarFila(self):
        atual = self.head
        print("Lista -> ", end="")
        while atual:
            print(f"[{atual.cor},{atual.numero}] ", end="")
            atual = atual.proximo
        print()

    def chamarPaciente(self):
        if self.head:
            chamado = self.head
            print(f'Atendendo o paciente cartão cor {chamado.cor} e número {chamado.numero}')
            self.head = chamado.proximo
            chamado.proximo = None
        else:
            print('Não há pacientes na fila')

def menu():
    fila = ListaEncadeada()
    numero_amarelo = 201  # Numeração inicial para cartões amarelos (A)
    numero_verde = 1       # Numeração inicial para cartões verdes (V)
    while True:
        print("\nMenu:")
        print("1 - Adicionar paciente à fila")
        print("2 - Mostrar pacientes na fila")
        print("3 - Chamar paciente")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            cor = input("Digite a cor do cartão (A para amarelo, V para verde): ").upper()
            if cor == 'A':
                numero = numero_amarelo
                numero_amarelo += 1
            elif cor == 'V':
                numero = numero_verde
                numero_verde += 1
            else:
                print("Cor inválida!")
                continue
            fila.inserir(cor, numero)
            print(f'Paciente com cartão {cor} número {numero} adicionado à fila.')
        elif opcao == '2':
            fila.mostrarFila()
        elif opcao == '3':
            fila.chamarPaciente()
            fila.mostrarFila()  # Mostra a fila após chamar um paciente
        elif opcao == '4':
            print('Encerrando o programa...')
            break
        else:
            print("Opção inválida!")

menu()
