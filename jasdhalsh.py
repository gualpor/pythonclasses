import re
nome = (input('Nome: '))
if re.match('^[A-Za-z]+$', nome):
    print('Seu nome é: ', nome)
else:
    print('Apenas letras por favor.')