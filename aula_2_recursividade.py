# def fatorial_iterativo(n):
#     fat = 1
#     if n < 0:
#         return None
#     elif n == 0 or n == 1:
#         return fat
#     else:
#         for i in range(1, n+1):
#             fat *= i
#         return fat
#
# print(fatorial_iterativo(4))#result


#função recursiva====================
#
# def fatorial_recursivo(n):
#     fat = 1
#     if n < 0:
#         return None
#     elif n == 0 or n == 1:
#         return fat
#     else:  #executara 1º a funcao , depois a multiplicação e retorna
#         return n * fatorial_recursivo(n-1)
# print(fatorial_recursivo(5))#result


#implementar a serie de fibonacci no python

print('Trabalho de fibonacci')

n =int( input(" Digite um teto para a sequência de Fibonacci :"))
t1 = 1
t2 = 0
t3 = 0
t4 = []

while t1 <= n:
    t4.append(t1)
    t3 = t1 + t2
    t2 = t1
    t1 = t3

print(t4)
