class Paciente:
    def __init__(self, id, tipo):
        self.id = id  # Número do cartão
        self.tipo = tipo  # Cor do cartão
        self.proximo = None  # Ponteiro para o próximo nodo

class FilaDeEspera:
    def __init__(self):
        self.primeiro = None  # Ponteiro para a cabeça da lista

    def adicionar_no_final(self, paciente):
        if not self.primeiro:
            self.primeiro = paciente
        else:
            atual = self.primeiro
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = paciente

    def adicionar_com_prioridade(self, paciente):
        if not self.primeiro or self.primeiro.tipo == 'V':
            paciente.proximo = self.primeiro
            self.primeiro = paciente
        else:
            atual = self.primeiro
            while atual.proximo and atual.proximo.tipo != 'V':
                atual = atual.proximo
            paciente.proximo = atual.proximo
            atual.proximo = paciente

    def inserir(self, tipo, id):
        novo_paciente = Paciente(id, tipo)
        if not self.primeiro:
            self.primeiro = novo_paciente
        elif tipo == 'V':
            self.adicionar_no_final(novo_paciente)
        elif tipo == 'A':
            self.adicionar_com_prioridade(novo_paciente)

    def exibir_fila(self):
        atual = self.primeiro
        print("Fila -> ", end="")
        while atual:
            print(f"[{atual.tipo},{atual.id}] ", end="")
            atual = atual.proximo
        print()

    def atender_primeiro_paciente(self):
        if self.primeiro:
            chamado = self.primeiro
            print(f'Chamando paciente com cartão {chamado.tipo} número {chamado.id}')
            self.primeiro = chamado.proximo
            chamado.proximo = None
        else:
            print('A fila está vazia.')

    def fila_vazia(self):
        return self.primeiro is None

def executar_programa():
    fila_espera = FilaDeEspera()
    id_amarelo = 201
    id_verde = 1
    while True:
        print("\nOpções:")
        print("1 - Adicionar paciente a fila")
        print("2 - Mostrar pacientes na fila")
        print("3 - Chamar paciente")
        print("4 - Sair")
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            tipo = input("Informe a cor do cartão (A/V): ").upper()
            if tipo == 'A':
                id = id_amarelo
                id_amarelo += 1
            elif tipo == 'V':
                id = id_verde
                id_verde += 1
            else:
                print("Tipo inválido!")
                continue
            fila_espera.inserir(tipo, id)
            print(f'Paciente com cartão {tipo} número {id} foi adicionado à fila.')
        elif escolha == '2':
            fila_espera.exibir_fila()
        elif escolha == '3':
            fila_espera.atender_primeiro_paciente()
            fila_espera.exibir_fila()
        elif escolha == '4':
            print('Programa encerrado.')
            break
        else:
            print("Opção inválida! Por favor, escolha uma das opções disponíveis.")

# Executa o programa
executar_programa()
