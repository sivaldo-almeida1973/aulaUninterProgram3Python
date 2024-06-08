#Exercicio 01

def Exercicio1(dados):
    for i in range(0, len(dados)/2, 1):
        dados[i] = i*2

#O loop é executado n/2 vezes
#T(n) = n/2 = O(n)
#Resposta = O(n)

#==============================================
#laco aninhado dentro de outro laço(PA-constante)
def Exercicio2(dados):
    for i in range(0, len(dados), 1):
        dados[i] =  i + 1
    for i in range(0, len(dados), 1):
        dados[i] = i - 1

#T(n) = n + n = O(n)
#Resposta = O(n)


#===============================================
#laco aninhado dentro de outro laço(PA-constante)
#sempre que um executar o outro irá tambem
def Exercicio3(dados):
    for i in range(0, len(dados), 1):
        for j in range(0, len(dados), 1):
            dados[i] = dados[j] + 1

#T(n) = n * n = O(n²)
#Resposta = O(n²)

#=============================================
def Exercicio4(dados):
    for i in range(0, len(dados), 1):
        for j in range(i, len(dados), 1):
            dados[i] = dados[j] + 1


#codigo identico ao de cima com exceção da 3º
# linha(i no lugar do 0)

# i = 0, j=0, n= 4
# i = 1, j=1, n= 3
# i = 2, j=2, n= 2
# i = 3, j=3, n= 1

#O(n²)
#PA de -1
#Resposta = O(n²)
#=================================================


def Exercicio5(dados):
    for i in range(0, len(dados), 1):
        for j in range(0, len(dados), 1):
               for k in range(0, 9000000, 1):
                 dados[i] = dados[j] + 1


#T(n) = 9000000 * n * n = O(n²)

#Resposta = O(n²)

#==============================================


#Exercicio 6
def Exercicio6(dados):
    for i in range(1, i * i, 1):
        print(i)

#complexidade
#x = 1, 1 < n
#x = 2, 4 < n         x² <= n
#x = 3, 9 < n         x   >=
#x = 4, 16 < n
#x = 5, 25 < n


#======================================

def Exercicio7(dados, n=None):
    if (n == 0):
        return
    Exercicio7(n/2)
    print(n)

#T(n0= log/2n = O(logn))

#comlexidade dividir para conquistar

#=============================================









