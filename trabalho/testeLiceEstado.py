# Classe para representar um estado na lista encadeada
class Estado:
    def __init__(self, sigla, nome):
        self.sigla = sigla  # Sigla do estado
        self.nome = nome  # Nome completo do estado
        self.proximo = None  # Ponteiro para o próximo estado na lista

# Classe para representar a lista encadeada de estados
class ListaDeEstados:
    def __init__(self):
        self.inicio = None  # Referência para o início da lista

    # Insere um estado no início da lista
    def inserir_inicio(self, sigla, nome):
        novo_estado = Estado(sigla, nome)  # Cria um novo estado
        novo_estado.proximo = self.inicio  # Aponta o novo estado para o atual primeiro estado
        self.inicio = novo_estado  # Atualiza o início da lista para o novo estado

    # Imprime todos os estados da lista
    def imprimir_lista(self):
        atual = self.inicio  # Começa pelo primeiro estado da lista
        if not atual:
            print("None")  # Se a lista estiver vazia, imprime "None"
        while atual:  # Enquanto houver estados na lista...
            print(f'{atual.sigla}', end=' -> ')  # Imprime a sigla do estado
            atual = atual.proximo  # Move para o próximo estado
        if self.inicio:
            print('None')  # Indica o final da lista

# Classe para a tabela hash de estados
class TabelaHashEstados:
    def __init__(self, tamanho=10):
        self.tamanho = tamanho  # Define o tamanho da tabela hash
        self.tabela = [ListaDeEstados() for _ in range(tamanho)]  # Cria uma lista de listas encadeadas

    # Função hash modificada
    def calcular_hash(self, sigla):
        return 7 if sigla == 'DF' else sum(ord(char) for char in sigla) % self.tamanho  # Calcula a posição na tabela hash

    # Insere um estado na tabela hash
    def inserir_estado(self, sigla, nome):
        indice = self.calcular_hash(sigla)  # Calcula o índice na tabela hash
        self.tabela[indice].inserir_inicio(sigla, nome)  # Insere o estado na lista encadeada correspondente

    # Imprime a tabela hash
    def imprimir_tabela(self):
        for i, lista in enumerate(self.tabela):  # Para cada posição na tabela hash...
            print(f'Posição {i}:', end=' ')  # Imprime o índice da posição
            lista.imprimir_lista()  # Imprime a lista de estados na posição

# Criação da tabela hash
tabela_hash_estados = TabelaHashEstados()

# H. Impressão da tabela hash antes de inserir qualquer informação
print("Impressão da tabela hash antes de inserir qualquer informação:")
tabela_hash_estados.imprimir_tabela()  # Imprime a tabela hash vazia

# Lista de estados e o Distrito Federal
lista_estados = [
    ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'),
    ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'),
    ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')
]

# I. Inserção dos estados na tabela hash
for sigla, nome in lista_estados:
    tabela_hash_estados.inserir_estado(sigla, nome)  # Insere cada estado na tabela hash

# Impressão da tabela hash após inserir os estados
print("\nImpressão da tabela hash após inserir os estados:")
tabela_hash_estados.imprimir_tabela()  # Imprime a tabela hash com os estados

# J. Inserção do estado fictício
estado_ficticio = ('BK', 'Bruno Kostiuk')
tabela_hash_estados.inserir_estado(*estado_ficticio)  # Insere o estado fictício na tabela hash

# Impressão da tabela hash após inserir o estado fictício
print("\nImpressão da tabela hash após inserir os estados e o estado fictício:")
tabela_hash_estados.imprimir_tabela()  # Impri
