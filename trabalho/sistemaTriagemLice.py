# Definição da classe Nodo, que representa cada paciente na fila.
class Nodo:

    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None    # referencia o próximo Nodo na fila.

# Definição da classe ListaEncadeada, que representa a fila de pacientes.
class ListaEncadeada:

    def __init__(self):
        self.head = None  # referencia a cabeça da lista (o primeiro Nodo).

    # Método para inserir um Nodo no final da fila (sem prioridade).
    def inserirSemPrioridade(self, novo_nodo):
        if not self.head:  # Se a lista estiver vazia...
            self.head = novo_nodo  # ...o novo nodo se torna a cabeça da lista.
        else:  # Se a lista não estiver vazia...
            atual = self.head  # Começa a percorrer a lista a partir da cabeça.


            while atual.proximo:  # Enquanto houver um próximo Nodo...
                atual = atual.proximo  # ...move para o próximo Nodo.
            atual.proximo = novo_nodo  # Insere o novo nodo no final da lista.

    # Método para inserir um Nodo na fila com prioridade (antes dos nodos com cor "V").
    def inserirComPrioridade(self, novo_nodo):
        if not self.head or self.head.cor == 'V':  # Se a lista estiver vazia ou o primeiro nodo for verde...
            novo_nodo.proximo = self.head  # ...insere o novo nodo no início da lista.
            self.head = novo_nodo
        else:  # Se a lista não estiver vazia e o primeiro nodo não for verde...
            atual = self.head  # Começa a percorrer a lista a partir da cabeça.
            while atual.proximo and atual.proximo.cor != 'V':  # Enquanto o próximo nodo não for verde...
                atual = atual.proximo  # ...move para o próximo Nodo.
            novo_nodo.proximo = atual.proximo  # Insere o novo nodo antes do primeiro nodo verde.
            atual.proximo = novo_nodo

    # Método para inserir um Nodo na fila, decidindo se é com ou sem prioridade.
    def inserir(self, cor, numero):
        novo_nodo = Nodo(numero, cor)  # Cria um novo Nodo com a cor e o número fornecidos.
        if cor == 'V':  # Se a cor do nodo for verde...
            self.inserirSemPrioridade(novo_nodo)  # ...chama o método para inserir sem prioridade.
        elif cor == 'A':  # Se a cor do nodo for amarela...
            self.inserirComPrioridade(novo_nodo)  # ...chama o método para inserir com prioridade.

    # Método para mostrar todos os Nodos da fila.
    def mostrarFila(self):
        atual = self.head  # Começa a percorrer a lista a partir da cabeça.
        print("Lista -> ", end="")  # Inicia a impressão da fila.
        while atual:  # Enquanto houver um Nodo...
            print(f"[{atual.cor},{atual.numero}] ", end="")  # ...imprime a cor e o número do Nodo.
            atual = atual.proximo  # Move para o próximo Nodo.
        print()  # Quebra de linha após imprimir todos os Nodos.

    # Método para chamar (atender) o primeiro paciente da fila.
    def chamarPaciente(self):
        if self.head:  # Se houver um paciente na fila...
            chamado = self.head  # ...o primeiro paciente é referenciado.
            print(f'Atendendo o paciente cartão cor {chamado.cor} e número {chamado.numero}')  # Imprime a chamada para atendimento.
            self.head = chamado.proximo  # Remove o paciente chamado da fila.
            chamado.proximo = None
        else:  # Se não houver pacientes na fila...
            print('Não há pacientes na fila')

# Função para exibir um menu interativo e permitir a gestão da fila de pacientes.
def menu():
    fila = ListaEncadeada()  # Cria uma nova fila de pacientes.
    numero_amarelo = 201
    numero_verde = 1
    while True:
        print("\nMenu:")  # Imprime as opções do menu.
        print("1 - Adicionar paciente à fila")
        print("2 - Mostrar pacientes na fila")
        print("3 - Chamar paciente")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':  # Se a opção for 1...
            cor = input("Digite a cor do cartão (A para amarelo, V para verde): ").upper()
            if cor == 'A':
                numero = numero_amarelo  # ...usa o próximo número amarelo disponível.
                numero_amarelo += 1  # Incrementa o número amarelo para o próximo paciente.
            elif cor == 'V':
                numero = numero_verde  # ...usa o próximo número verde disponível.
                numero_verde += 1  # Incrementa o número verde para o próximo paciente.
            else:  # Se a cor fornecida não for válida...
                print("Cor inválida!")
                continue  # Retorna ao início do loop do menu.
            fila.inserir(cor, numero)  # Insere o novo paciente na fila.
            print(f'Paciente com cartão {cor} número {numero} adicionado à fila.')
        elif opcao == '2':
            fila.mostrarFila()  # ...mostra todos os pacientes na fila.
        elif opcao == '3':
            fila.chamarPaciente()  # ...chama o próximo paciente para atendimento.
            fila.mostrarFila()  # Mostra a fila após chamar um paciente.
        elif opcao == '4':
            print('Encerrando o programa...')
            break  # Sai do loop do menu
        else:
            print("Opção inválida!")

menu()  # Chama a função menu para iniciar o programa
