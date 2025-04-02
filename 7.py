tupla = [1,2,3,4,5]
lista_temp = list(tupla)
lista_temp[int(input("Casa da mundança (0/4 )"))] = int(input('Numero novo: '))
tupla = tuple(lista_temp)
print(tupla)