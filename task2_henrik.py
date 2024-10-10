import numpy as np

def create_stencil_matrix(n):
    A = np.zeros((n, n))
    
    for i in range(n):
        A[i, i] = -2  # Diagonal elements
        
        if i > 0:
            A[i, i-1] = 1  # Lower 1
        
        if i < n-1:
            A[i, i+1] = 1  # Upper 1
            
    return A

# Approximate dominant eigenvalue
def dominant_eigenvalue_approz(A, v, iterations=100):
    for _ in range(iterations):
        v = A @ v
        v = v / np.linalg.norm(v)
    
    eigenvalue_approx = (v.T @ A @ v) / (v.T @ v)
    return eigenvalue_approx

def check_with_eig(A):
    Lambda, v = np.linalg.eig(A)
    dominant_eigenvalue = np.max(np.abs(Lambda))
    return dominant_eigenvalue


# Size of the matrix
n = 50
A = create_stencil_matrix(n)
v = np.random.rand(50)

# Find approximate eig. value
print(f"Approximate dominant eigevalue: {dominant_eigenvalue_approz(A, v)}")

# Check with np.linalg.eig
print(f"Exact dominant eigenvalue: {check_with_eig(A)}")