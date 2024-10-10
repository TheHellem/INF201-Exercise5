
import numpy as np

def inplace_add_vectors(v1: list, v2: list) -> list: 
    result = np.array(v1) + np.array(v2)
    for i in range(len(v1)):
        v1[i] = result[i]
    return v1


v1 = [1, 2, 3]
v2 = [4, 5, 6]

# Comment out in order to keep v1 the same
# inplace_add_vectors(v1, v2)
# print(v1)


def add_vectors(v1: list, v2: list) -> list: 
    v3 = v1 
    result = np.array(v1) + np.array(v2)
    for i in range(len(v1)):
        v3[i] = result[i]
    return v3

v3 = add_vectors(v1, v2)

print(v3)