import math

def print_matrix(name, matrix, depth):
    """Helper to print matrices with indentation based on recursion depth."""
    indent = "  " * depth
    print(f"{indent}{name}:")
    for row in matrix:
        print(f"{indent}  {row}")
    print()

def add_matrix(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def sub_matrix(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def split_matrix(matrix):
    """Splits a matrix into 4 equal quadrants."""
    mid = len(matrix) // 2
    A11 = [row[:mid] for row in matrix[:mid]]
    A12 = [row[mid:] for row in matrix[:mid]]
    A21 = [row[:mid] for row in matrix[mid:]]
    A22 = [row[mid:] for row in matrix[mid:]]
    return A11, A12, A21, A22

def merge_matrix(C11, C12, C21, C22):
    """Merges 4 quadrants back into a single matrix."""
    n = len(C11)
    merged = [[0 for _ in range(n * 2)] for _ in range(n * 2)]
    for i in range(n):
        for j in range(n):
            merged[i][j] = C11[i][j]
            merged[i][j + n] = C12[i][j]
            merged[i + n][j] = C21[i][j]
            merged[i + n][j + n] = C22[i][j]
    return merged

def strassen_recursive(A, B, depth=0):
    indent = "  " * depth
    n = len(A)
    
    print(f"\n{indent}--- Strassen Level {depth} (Size: {n}x{n}) ---")
    print_matrix("Matrix A", A, depth)
    print_matrix("Matrix B", B, depth)

    # Base case: 1x1 matrix
    if n == 1:
        result = [[A[0][0] * B[0][0]]]
        print(f"{indent}Base case reached. Multiplying {A[0][0]} * {B[0][0]} = {result[0][0]}\n")
        return result

    # Step 1: Split matrices into quadrants
    print(f"{indent}Splitting matrices into quadrants...")
    A11, A12, A21, A22 = split_matrix(A)
    B11, B12, B21, B22 = split_matrix(B)

    # Step 2: Calculate the 7 Strassen products recursively
    print(f"{indent}Calculating P1 = A11 * (B12 - B22)")
    P1 = strassen_recursive(A11, sub_matrix(B12, B22), depth + 1)
    
    print(f"{indent}Calculating P2 = (A11 + A12) * B22")
    P2 = strassen_recursive(add_matrix(A11, A12), B22, depth + 1)
    
    print(f"{indent}Calculating P3 = (A21 + A22) * B11")
    P3 = strassen_recursive(add_matrix(A21, A22), B11, depth + 1)
    
    print(f"{indent}Calculating P4 = A22 * (B21 - B11)")
    P4 = strassen_recursive(A22, sub_matrix(B21, B11), depth + 1)
    
    print(f"{indent}Calculating P5 = (A11 + A22) * (B11 + B22)")
    P5 = strassen_recursive(add_matrix(A11, A22), add_matrix(B11, B22), depth + 1)
    
    print(f"{indent}Calculating P6 = (A12 - A22) * (B21 + B22)")
    P6 = strassen_recursive(sub_matrix(A12, A22), add_matrix(B21, B22), depth + 1)
    
    print(f"{indent}Calculating P7 = (A11 - A21) * (B11 + B12)")
    P7 = strassen_recursive(sub_matrix(A11, A21), add_matrix(B11, B12), depth + 1)

    # Step 3: Calculate the 4 quadrants of the result matrix C
    print(f"\n{indent}--- Combining P1 through P7 at Level {depth} ---")
    C11 = add_matrix(sub_matrix(add_matrix(P5, P4), P2), P6)
    C12 = add_matrix(P1, P2)
    C21 = add_matrix(P3, P4)
    C22 = sub_matrix(sub_matrix(add_matrix(P5, P1), P3), P7)

    # Step 4: Merge the quadrants into a single matrix
    C = merge_matrix(C11, C12, C21, C22)
    print_matrix("Merged Result Matrix C", C, depth)
    
    return C

def get_next_power_of_2(n):
    return 2 ** math.ceil(math.log2(n))

def pad_matrix(matrix, new_size):
    """Pads a matrix with zeros up to new_size x new_size."""
    padded = [[0 for _ in range(new_size)] for _ in range(new_size)]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            padded[i][j] = matrix[i][j]
    return padded

def get_matrix_input(name, n):
    """Gets matrix input from the user."""
    print(f"\nEnter elements for {name} ({n}x{n}):")
    matrix = []
    for i in range(n):
        while True:
            try:
                row = list(map(int, input(f"Row {i+1} (space-separated integers): ").strip().split()))
                if len(row) != n:
                    print(f"Please enter exactly {n} integers.")
                    continue
                matrix.append(row)
                break
            except ValueError:
                print("Invalid input. Please enter integers only.")
    return matrix

def main():
    print("=== Strassen's Matrix Multiplication ===")
    while True:
        try:
            n = int(input("Enter the dimension of the square matrices (e.g., 2 for 2x2): "))
            if n > 0:
                break
            print("Dimension must be greater than 0.")
        except ValueError:
            print("Please enter a valid integer.")

    # Get user input for matrices
    A = get_matrix_input("Matrix A", n)
    B = get_matrix_input("Matrix B", n)

    # Strassen's algorithm requires sizes to be a power of 2.
    power_of_2_size = get_next_power_of_2(n)
    
    # Pad matrices if necessary
    if n != power_of_2_size:
        print(f"\n[!] Padding matrices with zeros to {power_of_2_size}x{power_of_2_size} (nearest power of 2)")
        A_padded = pad_matrix(A, power_of_2_size)
        B_padded = pad_matrix(B, power_of_2_size)
    else:
        A_padded = A
        B_padded = B

    # Run Strassen
    print("\nStarting recursive Strassen calculations...")
    C_padded = strassen_recursive(A_padded, B_padded)

    # Strip padding for final output
    C = [row[:n] for row in C_padded[:n]]

    print("\n=== FINAL RESULT ===")
    for row in C:
        print(row)

if __name__ == "__main__":
    main()