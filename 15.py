import time
precos = {
    'banana' : 4,
    'mamao' : 12,
    'universo observavel': 2.50
}

x = precos.keys()
print(x)
print('preço = ',precos[input('Qual deles? ')])

time.sleep(1.5)

precos[input('Objeto: ')] = int(input('Preço: '))
print (x)
print('preço = ',precos[input('Qual deles? ')])

time.sleep(1.5)

print(x)
precos.pop(input('Qual remover? '))
time.sleep(0.4)
print (x)
print('preço = ',precos[input('Qual deles? ')])

time.sleep(1.5)

for keyes, price in precos.items():
    print(f'Produto: {keyes}. Preço: {price}')

time.sleep(1.5)

tuplal = tuple(precos.items())
print(tuplal)