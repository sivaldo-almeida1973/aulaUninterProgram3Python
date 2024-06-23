#Exercicio 1
def Exercicio1 (dados) :
  for i in range (0, len(dados)/2, 1) :
    dados [i] = i * 2

#Exercicio 2
def Exercicio2 (dados) :
  for i in range (0, len(dados) , 1):
    dados [i] = i + 1
  for i in range (0, len(dados) , 1):
    dados [i] = i - 1

#Exercicio 3
def Exercicio3 (dados) :
  for i in range(0, len(dados), 1) :
    for j in range(0, len(dados), 1) :
      dados[i] = dados[j] + 1

#Exercicio 4
def Exercicio4 (dados) :
  for i in range(0, len(dados), 1) :
    for j in range(i, len(dados), 1) :
      dados[i] = dados[j] + 1

#Exercicio 5
def Exercicio5 (dados) :
  for i in range(0, len(dados), 1) :
    for j in range(0, len(dados), 1) :
      for k in range(0, 9000000, 1) :
        dados[i] = dados [j] + 1

#Execicio 6
def Exercicio6 (dados) :
  for i in range(1, i*i, 1) :
    print(i)


#Exercicio 7
def Exercicio7 (dados) :
  if (n == 0) :
    return
  Exercicio7(n/2)
  print(n)

#Exercicio 8
def Exercicio8 (dadosA = [] dadosB = []) :
  sort(dadosB)
  for i in range(0, len(dadosA), 1) :
    if(busca(dadosB, i) >= 0)
      return i





