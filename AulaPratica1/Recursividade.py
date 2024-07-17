# #Fatorial iterativo
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
# print(fatorial_iterativo(5))



#-----------------fatorial recursivo----------------
def fatorial_recusivo(n):
    fat = 1
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return fat
    else:
        return n * fatorial_recusivo(n-1)

print(fatorial_recusivo(5))
