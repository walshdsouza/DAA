def dijkstra(matrix, n):
    s = [False] * (n+1)
    prev = [1] * (n+1)

    dist = [None] * (n+1)
    for i in range(1, n+1):
        dist[i] = matrix[1][i]

    prev[1] = None
    curr = 1
    for i in range(1, n+1):
        print(f"Step {i} ", end="")
        print("v = 1") if(i == 1) else print(f"u = {curr}")
        s[i] = True
        print(f"s = {s[1:]}")

        min = float('inf')
        minIdx = None
        for j in range(1, n+1):
            if s[j]:
                continue
            if dist[i] + matrix[i][j] < dist[j]:
                dist[j] = dist[i] + matrix[i][j]
                prev[j] = i
            if dist[j] < min:
                min = dist[j]
                minIdx = j
        curr = minIdx
        print(f"Distance = {dist[1:]}\n")

    print("Source | Destination | Length | Path")
    for i in range(2, n+1):
        path = []

        j = i
        while(j != 1):
            path.append(j)
            j = prev[j]
        path.append(1)

        print(f"{1:^7}|{i:^13}|{dist[i]:^8}|{path[::-1]}")

def main():
    n = int(input("Enter the number of nodes: "))
    print("Enter the adjacency matrix:")
    matrix = []
    matrix.append([]) #matrix[0]
    for i in range(1, n+1):
        print(f"Enter row {i}: ")
        matrix.append([None] + [float(x) for x in input().split()])

    print()
    dijkstra(matrix, n)


if __name__ == "__main__":
    main()