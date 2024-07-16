# Classe que representa um paciente na fila de espera.
class Paciente:
    def __init__(self, id, tipo):
        self.id = id
        self.tipo = tipo
        self.proximo = None    # Referência ao próximo paciente na fila.

# Classe que gerencia a fila de espera dos pacientes.
class FilaDeEspera:
    def __init__(self):
        self.primeiro = None   # Primeiro paciente da fila.

    # Método para adicionar um paciente ao final da fila.
    def adicionar_no_final(self, paciente):
        if not self.primeiro:  # Se a fila estiver vazia...
            self.primeiro = paciente  # ...o paciente se torna o primeiro da fila.
        else:  # Se a fila não estiver vazia...
            atual = self.primeiro  # Começa a percorrer a fila a partir do primeiro paciente.
            while atual.proximo:  # Enquanto houver um próximo paciente...
                atual = atual.proximo  # ...move para o próximo paciente.
            atual.proximo = paciente  # Adiciona o paciente ao final da fila.

    # Método para adicionar um paciente com prioridade (antes dos pacientes verdes).
    def adicionar_com_prioridade(self, paciente):
        if not self.primeiro or self.primeiro.tipo == 'V':  # Se a fila estiver vazia ou o primeiro paciente for verde...
            paciente.proximo = self.primeiro  # ...o paciente é adicionado no início da fila.
            self.primeiro = paciente
        else:  # Se a fila não estiver vazia e o primeiro paciente não for verde...
            atual = self.primeiro  # Começa a percorrer a fila a partir do primeiro paciente.
            while atual.proximo and atual.proximo.tipo != 'V':  # Enquanto o próximo paciente não for verde...
                atual = atual.proximo  # ...move para o próximo paciente.
            paciente.proximo = atual.proximo  # Adiciona o paciente antes do primeiro paciente verde.
            atual.proximo = paciente

    # Método para adicionar um paciente à fila, decidindo se é com ou sem prioridade.
    def adicionar_paciente(self, tipo, id):
        novo_paciente = Paciente(id, tipo)  # Cria um novo paciente com o tipo e id fornecidos.
        if tipo == 'V':  # Se o tipo do paciente for verde...
            self.adicionar_no_final(novo_paciente)  # ...adiciona no final da fila.
        elif tipo == 'A':  # Se o tipo do paciente for amarelo...
            self.adicionar_com_prioridade(novo_paciente)  # ...adiciona com prioridade.

    # Método para exibir todos os pacientes na fila.
    def exibir_fila(self):
        atual = self.primeiro  # Começa a percorrer a fila a partir do primeiro paciente.
        print("Fila -> ", end="")  # Inicia a impressão da fila.
        while atual:  # Enquanto houver um paciente...
            print(f"[{atual.tipo},{atual.id}] ", end="")  # ...imprime o tipo e o id do paciente.
            atual = atual.proximo  # Move para o próximo paciente.
        print()  # Quebra de linha após imprimir todos os pacientes.

    # Método para chamar o primeiro paciente da fila para atendimento.
    def atender_primeiro_paciente(self):
        if self.primeiro:  # Se houver um paciente na fila...
            chamado = self.primeiro  # ...o primeiro paciente é referenciado.
            print(f'Chamando paciente com cartão {chamado.tipo} número {chamado.id}')  # Imprime a chamada para atendimento.
            self.primeiro = chamado.proximo  # Remove o paciente chamado da fila.
            chamado.proximo = None
        else:  # Se não houver pacientes na fila...
            print('A fila está vazia.')  # ...imprime uma mensagem informando que a fila está vazia.

# Função principal que executa o programa.
def executar_programa():
    fila_espera = FilaDeEspera()  # Cria uma nova fila de espera.
    id_amarelo = 201  # Define o id inicial para pacientes amarelos.
    id_verde = 1       # Define o id inicial para pacientes verdes.
    while True:
        print("\nOpções:")
        print("1 - Adicionar paciente")
        print("2 - Exibir fila")
        print("3 - Atender paciente")
        print("4 - Encerrar")
        escolha = input("Escolha uma opção: ")
        if escolha == '1':  # Se a escolha for 1...
            tipo = input("Informe o tipo do cartão (A para amarelo, V para verde): ").upper()  # ...solicita o tipo do cartão.
            if tipo == 'A':
                id = id_amarelo  # ...usa o próximo id amarelo disponível.
                id_amarelo += 1  # Incrementa o id amarelo para o próximo paciente.
            elif tipo == 'V':
                id = id_verde  # ...usa o próximo id verde disponível.
                id_verde += 1  # Incrementa o id verde para o próximo paciente.
            else:
                print("Tipo inválido!")  # ...imprime uma mensagem de erro.
                continue  # Retorna ao início do loop de opções.
            fila_espera.adicionar_paciente(tipo, id)  # Adiciona o novo paciente à fila.
            print(f'Paciente com cartão {tipo} número {id} foi adicionado à fila.')  # Imprime uma confirmação.
        elif escolha == '2':
            fila_espera.exibir_fila()  # ...exibe todos os pacientes na fila.
        elif escolha == '3':
            fila_espera.atender_primeiro_paciente()  # ...chama o primeiro paciente para atendimento.
            fila_espera.exibir_fila()  # Exibe a fila após chamar um paciente.
        elif escolha == '4':
            print('Programa encerrado.')
            break  # Sai do loop de opções, encerrando o programa.
        else:  # Se a escolha fornecida não for válida...
            print("Opção inválida!")

executar_programa()  # Inicia a execução do programa.
