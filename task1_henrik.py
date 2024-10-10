import numpy as np
import copy

# Create a 5000x5000 array with random integers between 0 and 100
array = np.random.randint(0, 101, size=(5000, 5000))
print(array)

# Function to find total sum
def total_sum_matrix(matrix: list) -> int:
    return sum(sum(row) for row in matrix)

print(f"Total sum: {total_sum_matrix(array)}")


# Function to find mean of matrix
def mean_matrix(matrix: list) -> float:
    total_entries = len(matrix) * len(matrix[0])
    return total_sum_matrix(matrix) / total_entries

print(f"Mean: {mean_matrix(array)}")


# Function to find variance
def variance_matrix(matrix: list) -> float:
    mean = mean_matrix(matrix)
    total_entries = len(matrix) * len(matrix[0])
    
    # Find the sum of ((\mu - A_{ij} )
    total_squared_diff = sum((element - mean) ** 2 for row in matrix for element in row)
    
    # Calculate variance
    variance = total_squared_diff / total_entries
    
    return variance

print(f"Variance: {variance_matrix(array)}")


# Function to multiply matrix by given number
def multiply_matrix_by_number(matrix: list, number: int) -> list:
    # Create a deep copy of the matrix to avoid modifying the original matrix
    multiplied_matrix = copy.deepcopy(matrix)
    
    for row in range(len(multiplied_matrix)):
        for col in range(len(multiplied_matrix[0])):
            multiplied_matrix[row][col] *= number
    
    return multiplied_matrix
    

# Choose 4 as given number:
print(f"Multiply by given n, where n=4: {multiply_matrix_by_number(array, 4)}")
