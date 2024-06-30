class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.head = None


    def inserir(self, novo_nodo):
        if not self.head:
            self.head = novo_nodo
        else:
            atual = self.head
            anterior = None
            # Encontrar a posição correta para inserção com base na cor e número.
            while atual:
                if atual.cor == 'A' and novo_nodo.cor == 'V':
                    anterior = atual
                    atual = atual.proximo
                elif atual.cor == novo_nodo.cor and novo_nodo.numero > atual.numero:
                    anterior = atual
                    atual = atual.proximo
                else:
                    break
            # Inserir o novo nodo na posição correta.
            novo_nodo.proximo = atual
            if anterior:
                anterior.proximo = novo_nodo
            else:
                self.head = novo_nodo
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
            print(f'Chamando paciente com cartão {chamado.cor}{chamado.numero}')
            self.head = chamado.proximo
            chamado.proximo = None
        else:
            print('Não há pacientes na fila')

# Função para criar um novo nodo e inserir na lista.
def criarEInserir(fila):
    cor = input('Informe a cor do cartão (A/V): ').upper()
    numero = int(input('Informe o número do cartão: '))
    novo_nodo = Nodo(numero, cor)
    fila.inserir(novo_nodo)

# Exemplo de uso da classe ListaEncadeada para criar a fila de triagem.
fila = ListaEncadeada()
while True:
    print('1 - Adicionar paciente a fila')
    print('2 - Mostrar pacientes na fila')
    print('3 - Chamar paciente')
    print('4 - Sair')
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        criarEInserir(fila)
    elif opcao == '2':
        fila.mostrarFila()
    elif opcao == '3':
        fila.chamarPaciente()
    elif opcao == '4':
        break
    else:
        print('Opção inválida')
