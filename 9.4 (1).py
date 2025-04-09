import numpy as np
import time

array = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print("\n",array)

time.sleep(0.5)

matriz0 = np.zeros((4,4))
print("\n",matriz0)

time.sleep(0.5)

matriz1 = np.ones((4,4))
print("\n",matriz1)

time.sleep(0.5)

print("\n",np.random.randint(1,51,((3,3))))

time.sleep(0.5)

matrix = np.array([
    [3,2,1],
    [6,5,4],
    [9,8,7]
])
print('\n',matrix + array)

time.sleep(0.5)

print('\n',array * 2)
print('\n',array / 2)

time.sleep(0.5)

det = np.linalg.det(array)
print('\n',det)

time.sleep(0.5)

array4 = np.random.randint(0,16,((4,4)))

print('\n',np.sum(array4,axis=0))

time.sleep(0.5)

print('\n',np.sum(array4,axis=1))

