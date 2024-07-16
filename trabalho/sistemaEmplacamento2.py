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
        while nodo_atual:
            print(nodo_atual.sigla, end=' -> ')
            nodo_atual = nodo_atual.proximo
        print('None')  # Indica o final da lista

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
            print(f'{i}:', end=' ')
            self.tabela[i].imprimir()

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

# Programa principal
tabela_hash = TabelaHash()

# H. Imprimir a tabela hash antes de inserir qualquer informação
print("SAÍDA VAZIA:")
tabela_hash.imprimir()

# Inserção dos estados na tabela hash
for sigla, nome in estados:
    tabela_hash.inserir(sigla, nome)

# I. Imprimir a tabela hash após inserir os 26 estados e o Distrito Federal - DF
print("\nSAÍDA COM ESTADOS E DF:")
tabela_hash.imprimir()

# Estado fictício para inserção
nome_ficticio = "Bruno Kostiuk"
sigla_ficticia = nome_ficticio.split()[0][0] + nome_ficticio.split()[-1][0]
tabela_hash.inserir(sigla_ficticia, nome_ficticio)

# J. Imprimir a tabela hash após inserir os 26 estados, Distrito Federal – DF e o estado fictício
print("\nSAÍDA COM ESTADOS, DF E ESTADO FICTÍCIO:")
tabela_hash.imprimir()
