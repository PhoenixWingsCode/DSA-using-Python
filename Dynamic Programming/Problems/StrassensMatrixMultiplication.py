import numpy as np

def add_matrix(A, B):
    return np.add(A, B)

def subtract_matrix(A, B):
    return np.subtract(A, B)

def strassen(A, B):
    n = len(A)
    
    if n == 1:
        return A * B
    
    # Splitting the matrices into quadrants
    mid = n // 2
    A11 = A[:mid, :mid]
    A12 = A[:mid, mid:]
    A21 = A[mid:, :mid]
    A22 = A[mid:, mid:]
    
    B11 = B[:mid, :mid]
    B12 = B[:mid, mid:]
    B21 = B[mid:, :mid]
    B22 = B[mid:, mid:]
    
    # Computing the 7 products, recursively (p1, p2...p7)
    P1 = strassen(A11, subtract_matrix(B12, B22))
    P2 = strassen(add_matrix(A11, A12), B22)
    P3 = strassen(add_matrix(A21, A22), B11)
    P4 = strassen(A22, subtract_matrix(B21, B11))
    P5 = strassen(add_matrix(A11, A22), add_matrix(B11, B22))
    P6 = strassen(subtract_matrix(A12, A22), add_matrix(B21, B22))
    P7 = strassen(subtract_matrix(A11, A21), add_matrix(B11, B12))
    
    # Computing the values of the 4 quadrants of the final matrix C
    C11 = add_matrix(subtract_matrix(add_matrix(P5, P4), P2), P6)
    C12 = add_matrix(P1, P2)
    C21 = add_matrix(P3, P4)
    C22 = subtract_matrix(subtract_matrix(add_matrix(P5, P1), P3), P7)
    
    # Combining the 4 quadrants into a single matrix by stacking horizontally and vertically
    C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))
    
    return C

# Example usage:
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

C = strassen(A, B)
print("Result of Strassen's Matrix Multiplication:\n", C)
