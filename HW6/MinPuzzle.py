def minEffort(puzzle):
    m, n = len(puzzle), len(puzzle[0])
    costs = []
    visited = [[0, 0]]
    currentX, currentY = 0, 0
    while True:
        current = puzzle[currentY][currentX]
        upCost = downCost = rightCost = leftCost = float('inf')
        if (currentY - 1) >= 0 and [currentY - 1, currentX] not in visited:
            upCost = abs(current - puzzle[currentY - 1][currentX])
        if (currentY + 1) <= (m - 1) and [currentY + 1, currentX] not in visited:
            downCost = abs(current - puzzle[currentY + 1][currentX])
        if (currentX + 1) <= (n - 1) and [currentY, currentX + 1] not in visited:
            rightCost = abs(current - puzzle[currentY][currentX + 1])
        if (currentX - 1) >= 0 and [currentY, currentX - 1] not in visited:
            leftCost = abs(current - puzzle[currentY][currentX - 1])
        if current == puzzle[m - 1][n - 1]:
            break
        minCost = min(upCost, downCost, rightCost, leftCost)
        costs.append(minCost)
        if minCost == upCost:
            currentY = currentY - 1
        elif minCost == downCost:
            currentY = currentY + 1
        elif minCost == rightCost:
            currentX = currentX + 1
        else:
            currentX = currentX - 1
        visited.append([currentY, currentX])
    return max(costs)


print(minEffort([[1, 3, 5], [2, 8, 3], [3, 4, 5]]))
