# Classe para representar um elemento individual na lista encadeada
class Nodo:
    def __init__(self, sigla, nomeEstado):
        self.sigla = sigla  # A chave do elemento
        self.nomeEstado = nomeEstado  # O dado associado à chave
        self.proximo = None  # O ponteiro para o próximo elemento na lista

# Classe para representar uma lista encadeada simples
class ListaEncadeada:
    def __init__(self):
        self.head = None  # O início da lista

    # Método para inserir um novo elemento no início da lista
    def inserir(self, sigla, nomeEstado):
        novo_nodo = Nodo(sigla, nomeEstado)
        novo_nodo.proximo = self.head
        self.head = novo_nodo

    # Método para imprimir todos os elementos da lista
    def imprimir(self):
        nodo_atual = self.head
        if not nodo_atual:
            print("None", end=' ')
        while nodo_atual:
            print(nodo_atual.sigla, end=' ')
            nodo_atual = nodo_atual.proximo
        print()  # Quebra de linha para separar as listas

# Classe para representar a tabela hash
class TabelaHash:
    def __init__(self):
        self.tamanho = 10
        self.tabela = [ListaEncadeada() for _ in range(self.tamanho)]

    # Função hash conforme as regras do enunciado
    def hashFunc(self, sigla):
        if sigla == 'DF':
            return 7
        else:
            return (ord(sigla[0]) + ord(sigla[1])) % 10

    # Método para inserir um estado na tabela hash
    def inserir(self, sigla, nomeEstado):
        posicao = self.hashFunc(sigla)
        self.tabela[posicao].inserir(sigla, nomeEstado)

    # Método para imprimir a tabela hash
    def imprimir(self):
        for i in range(self.tamanho):
            print(f'Posição {i}:', end=' ')
            self.tabela[i].imprimir()

# Criação da tabela hash e impressão inicial
tabela_hash = TabelaHash()
print("Tabela Hash antes de inserir qualquer informação:")
tabela_hash.imprimir()

# Lista de estados e distrito federal com suas siglas e nomes
estados = [
    ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'),
    ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'),
    ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')
]

# Inserção dos estados na tabela hash
for sigla, nome in estados:
    tabela_hash.inserir(sigla, nome)

# Impressão da tabela hash após inserção dos estados
print("\nTabela Hash após inserir os estados:")
tabela_hash.imprimir()

# Inserção do estado fictício
estado_ficticio = ('EB', 'Eralice Baia')
tabela_hash.inserir(*estado_ficticio)

# Impressão da tabela hash após inserção do estado fictício
print("\nTabela Hash após inserir os estados e o estado fictício:")
tabela_hash.imprimir()
