import math
import time
import random

def pprint_eq(*elements):
    if not elements: return
    rows = max([len(e) for e in elements if isinstance(e, list)], default=1)
    out_lines = ["" for _ in range(rows)]
    mid = max(0, (rows - 1) // 2)
    
    for e in elements:
        if isinstance(e, str):
            for i in range(rows):
                if i == mid:
                    out_lines[i] += e
                else:
                    out_lines[i] += " " * len(e)
        elif isinstance(e, list):
            str_mat = [[str(x) for x in row] for row in e]
            col_widths = [max(len(str_mat[r][c]) for r in range(len(e))) for c in range(len(e[0]))]
            for i in range(rows):
                if i < len(e):
                    row_vals = [str_mat[i][c].rjust(col_widths[c]) for c in range(len(e[0]))]
                    out_lines[i] += "[" + " ".join(row_vals) + "]"
                else:
                    out_lines[i] += " " * (sum(col_widths) + len(col_widths) + 1)
    print("\n".join(out_lines))

def add_matrix(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def sub_matrix(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def split_matrix(matrix):
    mid = len(matrix) // 2
    A11 = [row[:mid] for row in matrix[:mid]]
    A12 = [row[mid:] for row in matrix[:mid]]
    A21 = [row[:mid] for row in matrix[mid:]]
    A22 = [row[mid:] for row in matrix[mid:]]
    return A11, A12, A21, A22

def merge_matrix(C11, C12, C21, C22):
    n = len(C11)
    merged = [[0 for _ in range(n * 2)] for _ in range(n * 2)]
    for i in range(n):
        for j in range(n):
            merged[i][j] = C11[i][j]
            merged[i][j + n] = C12[i][j]
            merged[i + n][j] = C21[i][j]
            merged[i + n][j + n] = C22[i][j]
    return merged

def simple_multiply(A, B):
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def strassen_recursive(A, B, depth=0, show_steps=True):
    indent = "  " * depth
    n = len(A)
    
    threshold = 2
    
    if n <= threshold:
        return simple_multiply(A, B)

    if show_steps:
        print(f"\n{indent}--- Strassen Level (Size: {n}x{n}) ---")
        
    A11, A12, A21, A22 = split_matrix(A)
    B11, B12, B21, B22 = split_matrix(B)

    t1, t2 = add_matrix(A11, A22), add_matrix(B11, B22)
    if show_steps: pprint_eq(indent + "P = (", A11, " + ", A22, ")(", B11, " + ", B22, ")")
    P = strassen_recursive(t1, t2, depth + 1, show_steps)
    if show_steps: pprint_eq(indent + "  = ", P, "\n")
    
    t1 = add_matrix(A21, A22)
    if show_steps: pprint_eq(indent + "Q = (", A21, " + ", A22, ")", B11)
    Q = strassen_recursive(t1, B11, depth + 1, show_steps)
    if show_steps: pprint_eq(indent + "  = ", Q, "\n")
    
    t1 = sub_matrix(B12, B22)
    if show_steps: pprint_eq(indent + "R = ", A11, "(", B12, " - ", B22, ")")
    R = strassen_recursive(A11, t1, depth + 1, show_steps)
    if show_steps: pprint_eq(indent + "  = ", R, "\n")
    
    t1 = sub_matrix(B21, B11)
    if show_steps: pprint_eq(indent + "S = ", A22, "(", B21, " - ", B11, ")")
    S = strassen_recursive(A22, t1, depth + 1, show_steps)
    if show_steps: pprint_eq(indent + "  = ", S, "\n")
    
    t1 = add_matrix(A11, A12)
    if show_steps: pprint_eq(indent + "T = (", A11, " + ", A12, ")", B22)
    T = strassen_recursive(t1, B22, depth + 1, show_steps)
    if show_steps: pprint_eq(indent + "  = ", T, "\n")
    
    t1, t2 = sub_matrix(A21, A11), add_matrix(B11, B12)
    if show_steps: pprint_eq(indent + "U = (", A21, " - ", A11, ")(", B11, " + ", B12, ")")
    U = strassen_recursive(t1, t2, depth + 1, show_steps)
    if show_steps: pprint_eq(indent + "  = ", U, "\n")
    
    t1, t2 = sub_matrix(A12, A22), add_matrix(B21, B22)
    if show_steps: pprint_eq(indent + "V = (", A12, " - ", A22, ")(", B21, " + ", B22, ")")
    V = strassen_recursive(t1, t2, depth + 1, show_steps)
    if show_steps: pprint_eq(indent + "  = ", V, "\n")

    C11 = add_matrix(sub_matrix(add_matrix(P, S), T), V)
    C12 = add_matrix(R, T)
    C21 = add_matrix(Q, S)
    C22 = add_matrix(sub_matrix(add_matrix(P, R), Q), U)

    if show_steps:
        pprint_eq(indent + "C11 = ", P, " + ", S, " - ", T, " + ", V)
        pprint_eq(indent + "    = ", C11, "\n")
        
        pprint_eq(indent + "C12 = ", R, " + ", T, " = ", C12, "\n")
        
        pprint_eq(indent + "C21 = ", Q, " + ", S, " = ", C21, "\n")
        
        pprint_eq(indent + "C22 = ", P, " + ", R, " - ", Q, " + ", U)
        pprint_eq(indent + "    = ", C22, "\n")

    C = merge_matrix(C11, C12, C21, C22)
    return C

def get_next_power_of_2(n):
    return 2 ** math.ceil(math.log2(n))

def pad_matrix(matrix, new_size):
    padded = [[0 for _ in range(new_size)] for _ in range(new_size)]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            padded[i][j] = matrix[i][j]
    return padded

def get_matrix_input(name, n):
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
                print("Invalid input.")
    return matrix

def generate_random_matrix(n):
    return [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]

def menu_strassen():
    while True:
        try:
            n = int(input("Enter the dimension of the square matrices: "))
            if n > 0:
                break
        except ValueError:
            pass

    A = get_matrix_input("Matrix A", n)
    B = get_matrix_input("Matrix B", n)

    power_of_2_size = get_next_power_of_2(n)
    
    if n != power_of_2_size:
        A_padded = pad_matrix(A, power_of_2_size)
        B_padded = pad_matrix(B, power_of_2_size)
    else:
        A_padded = A
        B_padded = B

    C_padded = strassen_recursive(A_padded, B_padded, show_steps=True)
    C = [row[:n] for row in C_padded[:n]]

    print("\n=== FINAL RESULT ===")
    pprint_eq(C)

def menu_comparison():
    sizes_input = input("Enter matrix sizes to compare (comma separated, e.g., 2, 4, 8, 16): ")
    try:
        sizes = [int(s.strip()) for s in sizes_input.split(',')]
    except ValueError:
        print("Invalid input.")
        return

    print(f"\n{'Size':<10} | {'Normal Time (s)':<20} | {'Strassen Time (s)':<20}")
    print("-" * 55)

    for n in sizes:
        A = generate_random_matrix(n)
        B = generate_random_matrix(n)

        start_time = time.perf_counter()
        simple_multiply(A, B)
        normal_time = time.perf_counter() - start_time

        power_of_2_size = get_next_power_of_2(n)
        A_padded = pad_matrix(A, power_of_2_size) if n != power_of_2_size else A
        B_padded = pad_matrix(B, power_of_2_size) if n != power_of_2_size else B

        start_time = time.perf_counter()
        strassen_recursive(A_padded, B_padded, show_steps=False)
        strassen_time = time.perf_counter() - start_time

        print(f"{str(n)+'x'+str(n):<10} | {normal_time:<20.6f} | {strassen_time:<20.6f}")

def main():
    while True:
        print("\n=== MAIN MENU ===")
        print("1. Perform Strassen Multiplication")
        print("2. Compare Normal vs Strassen Performance")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            menu_strassen()
        elif choice == '2':
            menu_comparison()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()