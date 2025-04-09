import numpy as np
import time
array = np.array([1,23,20,98,62,69,11,17,62,28])
print(f"negativo: ",array * -1)
#negativou td

time.sleep(1)
x = 0
while x < 10:
 if array[x] > 50:
    array[x] = 50
 x = x + 1
print(f"maximo = 50: ",array)
#virou 50

time.sleep(1)
array2 = np.array([2,32,11,56,7,43,2,45,9,100])
print("a diferença é ",abs(array - array2))
#achou a diff

time.sleep(1)
array.sort
print(array[0],' é o menor numero')
print(array[9],' é o maior numero')