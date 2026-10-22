def dijkstra(matrix, n):
    INF = float('inf')
    s = [False] * (n + 1)
    prev = [1] * (n + 1)

    dist = [INF] * (n + 1)
    for i in range(1, n + 1):
        dist[i] = matrix[1][i]
    dist[1] = 0                      # distance from source to itself

    prev[1] = None
    curr = 1
    for step in range(1, n + 1):
        print(f"Step {step} ", end="")
        print("v = 1") if step == 1 else print(f"u = {curr}")
        s[curr] = True
        print(f"s = {s[1:]}")

        minVal = INF
        minIdx = None
        for j in range(1, n + 1):
            if s[j]:
                continue
            # relax edge (curr, j): is going through curr shorter?
            if dist[curr] + matrix[curr][j] < dist[j]:
                dist[j] = dist[curr] + matrix[curr][j]
                prev[j] = curr
            if dist[j] < minVal:
                minVal = dist[j]
                minIdx = j
        print(f"Distance = {dist[1:]}\n")

        if minIdx is None:           # remaining nodes are unreachable
            break
        curr = minIdx

    print("Source | Destination | Length | Path")
    for i in range(2, n + 1):
        if dist[i] == INF:
            print(f"{1:^7}|{i:^13}|{'inf':^8}|No path")
            continue

        path = []
        j = i
        while j != 1:
            path.append(j)
            j = prev[j]
        path.append(1)

        print(f"{1:^7}|{i:^13}|{dist[i]:^8}|{path[::-1]}")


def main():
    n = int(input("Enter the number of nodes: "))
    print("Enter the adjacency matrix (use inf for no direct edge):")
    matrix = [[]]  # matrix[0] unused
    for i in range(1, n + 1):
        print(f"Enter row {i}: ")
        matrix.append([None] + [float(x) for x in input().split()])

    print()
    dijkstra(matrix, n)


if __name__ == "__main__":
    main()