

def bubble_com_flag(dados):
     tam = len(dados)
     for v in range(0, tam, 1):
         flag = 0
         for i in range(0, tam - 1, 1):
               if dados[i] > dados[i + 1]:

                  aux = dados[i]
                  dados[i] = dados[i + 1]
                  dados[i + 1] = aux
                  flag = 1
         if flag == 0:
             return dados


dados = [9,5,7,3,1]

print(dados)
