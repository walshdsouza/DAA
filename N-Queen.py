x = []          # global array: x[j] = column of the queen in row j (1-indexed)
count = 0       # number of solutions found


def Place(k, i):
    """Return True if a queen can be placed in row k, column i.
    The first k-1 values of x[] are already set."""
    for j in range(1, k):
        # same column, or same diagonal
        if x[j] == i or abs(j - k) == abs(x[j] - i):
            return False
    return True


def print_solution(n):
    global count
    count += 1
    print(f"\nSolution {count}: {x[1:n + 1]}")
    for row in range(1, n + 1):
        print(" ".join("Q" if x[row] == col else "." for col in range(1, n + 1)))


def NQueen(k, n):
    """Using backtracking, print all possible placements of n queens
    on an n x n chessboard so that no two queens attack each other."""
    for i in range(1, n + 1):
        if Place(k, i):
            x[k] = i
            if k == n:
                print_solution(n)
            else:
                NQueen(k + 1, n)


def main():
    global x, count
    while True:
        try:
            n = int(input("Enter the number of queens (n): "))
            if n >= 1:
                break
            print("  Please enter a number >= 1.")
        except ValueError:
            print("  Invalid input, enter an integer.")

    x = [0] * (n + 1)   # index 0 unused, so rows/columns are 1..n
    count = 0
    NQueen(1, n)

    if count == 0:
        print(f"\nNo solution exists for n = {n}.")
    else:
        print(f"\nTotal solutions for n = {n}: {count}")


if __name__ == "__main__":
    main()