import time

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix)

time.sleep(0.5)
matrix2 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

print(matrix2[1][2])

time.sleep(0.5)

li1 = [1,2,3]
li2 = [4,5,6]
li3 = [7,8,9]
mat1 = [li1, li2, li3]
print(mat1)

time.sleep(0.5)
soma = sum(sum(linha)for linha in matrix)
print("soma= ",soma)

time.sleep(0.5)
x = 0
diagp = []
while x != len(matrix):
    diagp.append(matrix[x][x])
    x = x+1
print('diagonal principal = ',diagp)

time.sleep(0.5)
x = 2
y = 0
diagp = []
while x != -1:
    diagp.append(matrix[y][x])
    x = x-1
    y = y+1

print('diagonal secundária= ',diagp)

time.sleep(0.5)
matrix.sort(reverse=True)
print(matrix)
matrix.sort()

time.sleep(0.5)

soma = sum(sum(linha)for linha in matrix)
print("media= ",soma / len(matrix))

time.sleep(0.5)
print('maior = ',matrix[2][2])
print(f'menor = {matrix[0][0]}')

time.sleep(0.5)
x = matrix2
if 2 in matrix2[1] or matrix2[2] or matrix2[0]:
    print('tem 2')
else:
    print('nao tem 2')