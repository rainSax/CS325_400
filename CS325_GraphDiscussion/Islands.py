import collections


def numIslands(area):
    count = 0
    for i in range(len(area)):
        for j in range(len(area[0])):
            if area[i][j] == "1":
                dfs(area, i, j)
                count += 1
    return count


def dfs(area, i, j):
    if i < 0 or j < 0 or i >= len(area) or j >= len(area[0]) or area[i][j] != "1":
        return
    area[i][j] = "0"
    dfs(area, i + 1, j)
    dfs(area, i - 1, j)
    dfs(area, i, j + 1)
    dfs(area, i, j - 1)


def numIslands2(grid):
    m, n = len(grid), len(grid[0])
    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                land = [[i, j]]
                grid[i][j] = '0'
                while land:
                    x, y = land.pop()
                    for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                        xx, yy = x + dx, y + dy
                        if 0 <= xx < m and 0 <= yy < n and grid[xx][yy] == '1':
                            land.append([xx, yy])
                            grid[xx][yy] = '0'
                count += 1
    return count


print(numIslands2([
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]))

print(numIslands2([
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]))