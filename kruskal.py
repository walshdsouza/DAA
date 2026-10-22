# ---------- Min-heap (1-indexed, as in the notes) ----------
# Each heap element is a tuple (cost, u, v), so comparisons use the edge cost.

def Adjust(a, i, n):
    j = 2 * i
    item = a[i]
    while j <= n:
        if j < n and a[j] > a[j + 1]:
            j = j + 1
        if item <= a[j]:
            break
        a[j // 2] = a[j]
        j = 2 * j
    a[j // 2] = item


def Heapify(a, n):
    for i in range(n // 2, 0, -1):
        Adjust(a, i, n)


def DelMin(a, n):
    """Remove and return the minimum element; returns (element, new heap size)."""
    if n == 0:
        print("Heap Empty")
        return None, 0
    x = a[1]
    a[1] = a[n]
    Adjust(a, 1, n - 1)
    return x, n - 1


# ---------- Union-Find (as in the notes) ----------

def Find(i, parent):
    while parent[i] > 0:
        i = parent[i]
    return i


def Union(i, j, parent):
    parent[i] = j


# ---------- Printing ----------

def print_step(step, u, v, w, accepted, mincost, parent, n):
    status = "ACCEPTED" if accepted else "REJECTED (Cycle)"
    print(f"Step {step:2d} | Edge ({u:2d}, {v:2d}) w={w:3d} -> {status:<16} | Running Cost: {mincost:4d}")
    print("        parent: [" + " ".join(f"{parent[k]:3d}" for k in range(1, n + 1)) + "]\n")


def print_t_table(t, n):
    print("\n" + "-" * 30)
    print("   Final MST Edges (t)")
    print("-" * 30)
    print("Row (i) |  t[i,1] |  t[i,2]")
    print("-" * 30)
    for i in range(1, n):
        print(f"   {i:<4} |    {t[i][1]:<4} |    {t[i][2]:<4}")
    print("-" * 30)


# ---------- Kruskal's algorithm ----------

def Kruskals(heap, m, n, t):
    """
    heap : 1-indexed min-heap of (cost, u, v) edges, m edges
    n    : number of vertices
    t    : t[i][1], t[i][2] store the i-th MST edge
    Returns the minimum cost, or None if no spanning tree exists.
    """
    Heapify(heap, m)                    # construct a heap out of edges

    parent = [-1] * (n + 1)             # each vertex is in a different set
    i = 0
    mincost = 0
    step = 0

    while i < n - 1 and m > 0:
        (w, u, v), m = DelMin(heap, m)  # delete min cost edge and reheapify
        step += 1
        j = Find(u, parent)
        k = Find(v, parent)
        if j != k:
            i += 1
            t[i][1] = u
            t[i][2] = v
            mincost += w
            Union(j, k, parent)
            print_step(step, u, v, w, True, mincost, parent, n)
        else:
            print_step(step, u, v, w, False, mincost, parent, n)

    if i != n - 1:
        print("No Spanning Tree")
        return None
    return mincost


# ---------- Input ----------

def read_int(prompt, minimum=None):
    while True:
        try:
            val = int(input(prompt))
            if minimum is not None and val < minimum:
                print(f"  Please enter a number >= {minimum}.")
                continue
            return val
        except ValueError:
            print("  Invalid input, enter an integer.")


def read_graph():
    n = read_int("Number of vertices: ", 1)
    m = read_int("Number of edges: ", 0)
    heap = [None]                       # index 0 unused (1-indexed heap)
    print(f"Enter each edge as: u v cost   (vertices are 1..{n})")
    count = 0
    while count < m:
        try:
            u, v, w = map(int, input(f"  Edge {count + 1}: ").split())
        except ValueError:
            print("  Enter exactly three integers: u v cost")
            continue
        if not (1 <= u <= n and 1 <= v <= n):
            print(f"  Vertices must be between 1 and {n}.")
            continue
        if u == v:
            print("  Self-loops are not allowed.")
            continue
        heap.append((w, u, v))
        count += 1
    return n, m, heap


def main():
    print("Kruskal's Minimum Spanning Tree (min-heap version)")
    n, m, heap = read_graph()

    if n == 1:
        print("\nSingle vertex: Minimum Cost = 0")
        return

    t = [[0, 0, 0] for _ in range(n)]
    print()
    mincost = Kruskals(heap, m, n, t)
    if mincost is not None:
        print(f"\nFinal Minimum Cost = {mincost}")
        print_t_table(t, n)


if __name__ == "__main__":
    main()