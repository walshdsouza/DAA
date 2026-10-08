import math

def print_matrices(k, A, P):
    n = len(A)
    print(f"\n{'-'*40}")
    print(f"Step k = {k} (A_{k} and P_{k})")
    print(f"{'-'*40}")
    
    print(f"A_{k}:")
    header = "    " + "   ".join([f"{i+1:>3}" for i in range(n)])
    print(header)
    print("  " + "-" * len(header))
    for i in range(n):
        row_vals = []
        for j in range(n):
            if A[i][j] == math.inf:
                row_vals.append(f"{'∞':>3}")
            else:
                row_vals.append(f"{int(A[i][j]):>3}")
        print(f"{i+1} | " + "   ".join(row_vals))
        
    print("\n")
    
    print(f"P_{k}:")
    print(header)
    print("  " + "-" * len(header))
    for i in range(n):
        row_vals = []
        for j in range(n):
            if P[i][j] == -1 or i == j:
                row_vals.append(f"{'-':>3}")
            else:
                row_vals.append(f"{P[i][j] + 1:>3}")
        print(f"{i+1} | " + "   ".join(row_vals))


def get_path(i, j, P):
    if P[i][j] == -1:
        return []
    
    path = [j]
    curr = j
    while curr != i:
        curr = P[i][curr]
        if curr == -1:
            return []
        path.append(curr)
        
    return path[::-1]


def all_pairs_shortest_path(cost):
    n = len(cost)
    
    A = [[cost[i][j] for j in range(n)] for i in range(n)]
    P = [[-1] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i != j and cost[i][j] != math.inf:
                P[i][j] = i 
                
    print_matrices(0, A, P)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if A[i][k] != math.inf and A[k][j] != math.inf:
                    if A[i][j] > A[i][k] + A[k][j]:
                        A[i][j] = A[i][k] + A[k][j]
                        P[i][j] = P[k][j] 
                        
        print_matrices(k + 1, A, P)

    print("\n" + "="*50)
    print(f"{'src':<5} {'dest':<5} {'len':<5} {'path'}")
    print("="*50)
    
    for i in range(n):
        for j in range(n):
            if i != j:
                length = A[i][j]
                if length == math.inf:
                    print(f"{i+1:<5} {j+1:<5} {'∞':<5} No Path")
                else:
                    path_indices = get_path(i, j, P)
                    path_str = " -> ".join([str(v + 1) for v in path_indices])
                    print(f"{i+1:<5} {j+1:<5} {int(length):<5} {path_str}")


def get_user_input():
    while True:
        try:
            n = int(input("Enter the number of vertices: "))
            break
        except ValueError:
            print("Please enter a valid integer.")

    print("\nEnter the cost matrix row by row.")
    print("Use spaces to separate values (e.g., '0 12 21 inf 32').")
    
    cost_matrix = []
    for i in range(n):
        while True:
            row_input = input(f"Row {i+1}: ").strip().split()
            
            if len(row_input) != n:
                print(f"Please enter exactly {n} values.")
                continue
                
            row = []
            try:
                for val in row_input:
                    if val.lower() in ['inf', 'i', 'infinity']:
                        row.append(math.inf)
                    else:
                        row.append(float(val))
                cost_matrix.append(row)
                break
            except ValueError:
                print("Invalid input. Please enter numbers or 'inf'.")
                
    return cost_matrix


if __name__ == "__main__":
    cost_matrix = get_user_input()
    all_pairs_shortest_path(cost_matrix)