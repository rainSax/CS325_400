def findAllPaths(G, i, j, m, n, path, pi, costs):
    # if we reach the bottom, move right
    if i == (m - 1):
        for k in range(j, n):
            path[pi + k - j] = G[i][k]
        if k == (n - 1):
            for f in range(0, len(path)):
                costs[-1] += path[f]
            if costs[-1] <= 0:
                costs[-1] = abs(costs[-1]) + 1
            else:
                costs[-1] = 0
            costs.append(0)
        return
    # if we reach the right, move down
    if j == (n - 1):
        for k in range(i, m):
            path[pi + k - i] = G[k][j]
        if k == (m - 1):
            for f in range(0, len(path)):
                costs[-1] += path[f]
            if costs[-1] <= 0:
                costs[-1] = abs(costs[-1]) + 1
            else:
                costs[-1] = 0
            costs.append(0)
        return
    # add current cell to path
    path[pi] = G[i][j]

    # Print all the paths
    # that are possible after moving down
    findAllPaths(G, i + 1, j, m, n, path, pi + 1, costs)

    # Print all the paths
    # that are possible after moving right
    findAllPaths(G, i, j + 1, m, n, path, pi + 1, costs)


def getTesla(M):
    m = len(M)
    n = len(M[0])
    path = [0 for i in range(m + n)]
    costs = [0]
    findAllPaths(M, 0, 0, m, n, path, 0, costs)
    costs.pop()
    return min(costs)

