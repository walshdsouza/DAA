def next_value(k):
    while True:
        x[k] = (x[k] + 1) % (m + 1)      # next highest colour
        if x[k] == 0:                    # all colours used
            return
        for j in range(1, n + 1):
            if G[k][j] != 0 and x[k] == x[j]:
                break                    # adjacent vertex has same colour
        else:
            return                       # new colour found


def m_coloring(k):
    global count
    while True:
        next_value(k)
        if x[k] == 0:                    # no new colour possible
            return
        if k == n:
            count += 1
            print(f"Solution {count}:", x[1:n + 1])
        else:
            m_coloring(k + 1)


n = int(input("Enter number of vertices (n): "))

print(f"Enter the {n}x{n} adjacency matrix (row by row, 0/1 separated by spaces):")
G = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, n + 1):
        G[i][j] = row[j - 1]

chromatic = None
for m in range(1, n + 1):                # m = 1, 2, ..., n
    x = [0] * (n + 1)
    count = 0
    print(f"\nTrying m = {m} ...")
    m_coloring(1)
    if count > 0:
        chromatic = m
        print(f"Total colourings with {m} colours = {count}")
        break
    print("No colouring possible.")

if chromatic is None:
    print("\nNo valid colouring exists (graph has a self-loop).")
else:
    print(f"\nMinimum chromatic number = {chromatic}")