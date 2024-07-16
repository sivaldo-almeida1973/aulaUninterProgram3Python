class Paciente:
    def __init__(self, id, tipo):
        self.id = id
        self.tipo = tipo
        self.proximo = None    # Referência ao próximo paciente na fila.

class FilaDeEspera:
    def __init__(self):
        self.primeiro = None   # Primeiro paciente da fila.

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

    def adicionar_paciente(self, tipo, id):
        novo_paciente = Paciente(id, tipo)
        if tipo == 'V':
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
        print("1 - Adicionar paciente")
        print("2 - Exibir fila")
        print("3 - Atender paciente")
        print("4 - Encerrar")
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            tipo = input("Informe o tipo do cartão (A para amarelo, V para verde): ").upper()
            if tipo in ['A', 'V']:
                id = input(f"Informe o número do cartão {tipo} (padrão {id_amarelo if tipo == 'A' else id_verde}): ")
                if not id.isdigit():
                    print("Número inválido! Usando o padrão.")
                    id = id_amarelo if tipo == 'A' else id_verde
                else:
                    id = int(id)
                if tipo == 'A':
                    id_amarelo = max(id_amarelo, id + 1)
                elif tipo == 'V':
                    id_verde = max(id_verde, id + 1)
                fila_espera.adicionar_paciente(tipo, id)
                print(f'Paciente com cartão {tipo} número {id} foi adicionado à fila.')
            else:
                print("Tipo inválido!")
        elif escolha == '2':
            fila_espera.exibir_fila()
        elif escolha == '3':
            fila_espera.atender_primeiro_paciente()
            fila_espera.exibir_fila()
        elif escolha == '4':
            print('Programa encerrado.')
            break

# Executa o programa
executar_programa()
