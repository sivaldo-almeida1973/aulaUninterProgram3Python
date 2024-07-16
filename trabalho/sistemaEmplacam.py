# Classe para representar um estado na lista encadeada
class Estado:
    def __init__(self, sigla, nome):
        self.sigla = sigla
        self.nome = nome
        self.proximo = None

# Classe para representar a lista encadeada de estados
class ListaDeEstados:
    def __init__(self):
        self.inicio = None

    # Insere um estado no início da lista
    def inserir_no_inicio(self, sigla, nome):
        novo_estado = Estado(sigla, nome)
        novo_estado.proximo = self.inicio
        self.inicio = novo_estado

    # Imprime todos os estados da lista
    def imprimir_lista(self):
        atual = self.inicio
        while atual:
            print(f'{atual.sigla}', end=' -> ')
            atual = atual.proximo
        print('None')  # Indica o final da lista

# Classe para a tabela hash de estados
class TabelaHashEstados:
    def __init__(self, tamanho=10):
        self.tamanho = tamanho
        self.tabela = [ListaDeEstados() for _ in range(tamanho)]

    # Função hash modificada
    def calcular_hash(self, sigla):
        return 7 if sigla == 'DF' else sum(ord(char) for char in sigla) % self.tamanho

    # Insere um estado na tabela hash
    def inserir_estado(self, sigla, nome):
        indice = self.calcular_hash(sigla)
        self.tabela[indice].inserir_no_inicio(sigla, nome)

    # Imprime a tabela hash
    def imprimir_tabela(self):
        for i, lista in enumerate(self.tabela):
            print(f'{i}:', end=' ')
            lista.imprimir_lista()

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

# Criação da tabela hash
tabela_hash_estados = TabelaHashEstados()

# Inserção dos estados na tabela hash
for sigla, nome in lista_estados:
    tabela_hash_estados.inserir_estado(sigla, nome)

# Estado fictício para inserção
nome_ficticio = "Bruno Kostiuk"
sigla_ficticia = nome_ficticio.split()[0][0] + nome_ficticio.split()[-1][0]
tabela_hash_estados.inserir_estado(sigla_ficticia, nome_ficticio)

# Impressão da tabela hash após inserção dos estados, do DF e do estado fictício
tabela_hash_estados.imprimir_tabela()
