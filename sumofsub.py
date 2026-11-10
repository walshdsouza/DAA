w = []   #weight from w[1]
x = []   # solution vector
m = 0    # target sum
n = 0    # number of elements


def SumOfSub(s, k, r):
    # Generate left child (include w[k])
    x[k] = 1

    if s + w[k] == m:
        print("Subset found:", [w[i] for i in range(1, k + 1) if x[i] == 1],
              "| x =", x[1:k + 1])
    elif k < n and s + w[k] + w[k + 1] <= m:
        SumOfSub(s + w[k], k + 1, r - w[k])

    # Generate right child (exclude w[k]) and evaluate B_k
    if k < n and (s + r - w[k] >= m) and (s + w[k + 1] <= m):
        x[k] = 0
        SumOfSub(s, k + 1, r - w[k])


def main():
    global w, x, m, n

    n = int(input("Enter number of elements: "))
    weights = list(map(int, input(f"Enter {n} weights (space separated): ").split()))
    m = int(input("Enter target sum m: "))

    if len(weights) != n:
        print("Error: number of weights does not match n.")
        return

    weights.sort()             
    w = [0] + weights
    x = [0] * (n + 2)

    total = sum(weights)

    if w[1] > m or total < m:
        print("No solution possible.")
        return

    print("\nSorted weights:", weights)
    print("Target sum:", m, "\n")
    SumOfSub(0, 1, total)       


if __name__ == "__main__":
    main()