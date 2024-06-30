# Definição da classe Nodo, que representa cada paciente na fila.
class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero   # Número do cartão do paciente.
        self.cor = cor    # Cor do cartão do paciente (A para amarelo, V para verde).
        self.proximo = None # Referência ao próximo Nodo na fila.

# Definição da classe ListaEncadeada, que representa a fila de pacientes.
class ListaEncadeada:
    def __init__(self):
        self.head = None

 # Método para inserir um novo paciente na fila com base na cor e número do cartão.
    def inserir(self, novo_nodo):
        if not self.head:
            self.head = novo_nodo
        else:
            atual = self.head
            anterior = None
            while atual:
                if atual.cor == 'A' and novo_nodo.cor == 'V':
                    anterior = atual
                    atual = atual.proximo
                elif atual.cor == novo_nodo.cor and novo_nodo.numero > atual.numero:
                    anterior = atual
                    atual = atual.proximo
                else:
                    break
            novo_nodo.proximo = atual
            if anterior:
                anterior.proximo = novo_nodo
            else:
                self.head = novo_nodo

  # Método para exibir todos os pacientes na fila.
    def mostrarFila(self):
        atual = self.head
        print("Lista -> ", end="")
        while atual:
            print(f"[{atual.cor},{atual.numero}] ", end="")
            atual = atual.proximo
        print()

  # Método para chamar o próximo paciente da fila.
    def chamarPaciente(self):
        if self.head:
            chamado = self.head
            print(f"Atendendo o paciente cartão cor {chamado.cor} e número {chamado.numero}")
            self.head = chamado.proximo
            chamado.proximo = None
        else:
            print('Não há pacientes na fila')

# Função para criar um novo nodo e inserir na lista.
def criarEInserir(fila):
      # Solicita ao usuário a cor e o número do cartão e insere na fila.
    cor = input('Informe a cor do cartão (A/V): ').upper()
    numero = int(input('Informe o número do cartão: '))
    if cor == 'A' and numero < 201 or cor == 'V' and numero < 1:
        print('Número de cartão inválido para a cor informada.')
        return
    novo_nodo = Nodo(numero, cor)
    fila.inserir(novo_nodo)

# Exemplo de uso da classe ListaEncadeada para criar a fila de triagem.
# Loop principal do programa que exibe um menu e executa ações com base na escolha do usuário.
fila = ListaEncadeada()
while True:
    # Exibe as opções do menu.
    # Processa a entrada do usuário e chama a função correspondente.
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
