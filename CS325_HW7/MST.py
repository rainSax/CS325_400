def union(setCount, u, v):
    if setCount[u] < setCount[v]:
        setCount[u] += setCount[v]
        setCount[v] = u
    else:
        setCount[v] += setCount[u]
        setCount[u] = v


def find(setCount, u):
    x, v = u, 0
    while setCount[x] > 0:
        x = setCount[x]
    while u != x:
        v = setCount[u]
        setCount[u] = x
        u = v
    return x


def Kruskal(G):
    n, e, i, u, v, k = 0, len(G[0]), 0, -1, -1, -1
    setCount = [-1] * e
    included = [0] * e
    # use nested for loop to find the max # of vertices
    for i in range(len(G) - 1):
        for j in range(len(G[0])):
            if G[i][j] > n:
                n = G[i][j]
    i, j = 0, 0
    # create empty solution tree of V - 1 size
    tree = [[0 for x in range(n - 1)] for y in range(2)]
    while i < n - 1:
        minimum = float('inf')
        for j in range(0, e):
            if included[j] == 0 and G[2][j] < minimum:
                minimum = G[2][j]
                k = j
                u = G[0][j]
                v = G[1][j]
        if find(setCount, u) != find(setCount, v):
            tree[0][i] = u
            tree[1][i] = v
            union(setCount, find(setCount, u), find(setCount, v))
            i += 1
        included[k] = 1
    return tree


def Prims(G):
    n, e, i, u, v, k = 0, len(G[0]), 0, -1, -1, -1
    # use nested for loop to find the max # of vertices
    for i in range(len(G) - 1):
        for j in range(len(G[0])):
            if G[i][j] > n:
                n = G[i][j]
    adjacent = [float('inf')] * (n + 1)
    minimum = float('inf')
    i, j = 0, 0
    # create empty solution tree of V - 1 size
    tree = [[0 for x in range(n - 1)] for y in range(2)]
    costs = [[float('inf') for x in range(n + 1)] for y in range(n + 1)]
    # represent the edge costs in a 2d matrix bidirectionally
    for i in range(len(G[0])):
        costs[G[0][i]][G[1][i]] = G[2][i]
        costs[G[1][i]][G[0][i]] = G[2][i]
    i, j = 1, 1
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if costs[i][j] < minimum:
                minimum = costs[i][j]
                u = i
                v = j
    tree[0][0] = u
    tree[1][0] = v
    adjacent[u] = adjacent[v] = 0
    i, j = 1, 1
    for i in range(1, n + 1):
        if adjacent[i] != 0:
            if adjacent[i] != 0 and costs[i][u] < costs[i][v]:
                adjacent[i] = u
            else:
                adjacent[i] = v
    i, j = 1, 1
    for i in range(1, n - 1):
        minimum = float('inf')
        for j in range(1, n + 1):
            if adjacent[j] != 0 and costs[j][adjacent[j]] < minimum:
                minimum = costs[j][adjacent[j]]
                k = j
        tree[0][i] = k
        tree[1][i] = adjacent[k]
        adjacent[k] = 0
        i, j = 1, 1
        for j in range(1, n + 1):
            if adjacent[j] != 0 and costs[j][k] < costs[j][adjacent[j]]:
                adjacent[j] = k
    return tree


print(Kruskal([[1, 1, 2, 2, 3, 4, 4, 5, 5, ],
               [2, 6, 3, 7, 4, 5, 7, 6, 7, ],
               [25, 5, 12, 10, 8, 16, 14, 20, 18]]))

print(Prims([[1, 1, 2, 2, 3, 4, 4, 5, 5, ],
             [2, 6, 3, 7, 4, 5, 7, 6, 7, ],
             [25, 5, 12, 10, 8, 16, 14, 20, 18]]))
