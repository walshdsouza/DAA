def Prim(E, cost, n, t):
    # Step 1: Find the edge with minimum cost to start the tree
    mincost = float('inf')
    k = l = -1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if cost[i][j] < mincost:
                mincost = cost[i][j]
                k, l = i, j

    if mincost == float('inf'):
        print("No spanning tree exists")
        return -1

    # First edge of MST
    t[0] = (k, l)
    mincost = cost[k][l]

    # near[i] tells us which vertex in the current tree is closest to vertex i
    # near[i] = 0 means vertex i is already included in the tree
    near = [0] * (n + 1)

    for i in range(1, n + 1):
        if cost[i][l] < cost[i][k]:
            near[i] = l
        else:
            near[i] = k

    near[k] = near[l] = 0   #already in the tree

    for i in range(2, n):          # we already have 1 edge
        # find the vertex j not yet in tree
        min_val = float('inf')
        j = -1
        for idx in range(1, n + 1):
            if near[idx] != 0 and 0 < cost[idx][near[idx]] < min_val:
                min_val = cost[idx][near[idx]]
                j = idx

        if j == -1:
            print("No spanning tree exists")
            return -1

        # Add edge (j, near[j]) to MST
        t[i - 1] = (j, near[j])
        mincost += cost[j][near[j]]
        near[j] = 0

        # Update near[] for all vertices still outside the tree
        for idx in range(1, n + 1):
            if near[idx] != 0 and cost[idx][near[idx]] > cost[idx][j]:
                near[idx] = j

    return mincost