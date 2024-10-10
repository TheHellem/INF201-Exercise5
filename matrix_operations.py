import numpy as np

# Create a 5000x5000 array with random integers between 0 and 100
array = np.random.randint(0, 101, size=(5000, 5000))
print(array)

# Function to find total sum
def total_sum_matrix(matrix: list) -> int: sum(sum(row) for row in matrix)

# Function to find mean of matrix
def mean_matrix(matrix : list) -> float:
    total_entries =sum(len(row) for row in array)
    return total_sum_matrix(matrix) / total_entries 

# Function to find variance of matrix
def variance_matrix(matrix: list) -> float:
    mean = mean_matrix(matrix)

    # Find squared differenses
    total_squared_diff = sum((element - mean) ** 2 for row in matrix for element in row)
    
    return total_squared_diff / total_sum_matrix(matrix)


def multiply_matrix_by_number(matrix: list, number: int) -> list: 
    return [[element * number for element in row] for row in matrix]