# Brute force solutions using recursion yield a time complexity of 2^n
# due to exponentially increasing number of recursive function calls


def minStepsBF(cost):
    size = len(cost)
    return min(minStepsBFHelper(cost, size - 1), minStepsBFHelper(cost, size - 2))


def minStepsBFHelper(cost, size):
    if size == 0:
        return cost[size]
    if size == 1:
        return cost[size]
    return cost[size] + min(minStepsBFHelper(cost, size - 1), minStepsBFHelper(cost, size - 2))


def minStepsBottomUp(cost):
    n = len(cost)
    costTable = [0] * n
    costTable[0] = cost[0]
    costTable[1] = cost[1]
    for i in range(2, n):
        costTable[i] = min(costTable[i - 1], costTable[i - 2]) + cost[i]
    return min(costTable[n - 1], costTable[n - 2])

# DP approach improves time complexity to n since return values of function
# calls are cached and checked for in each recursive call


def minStepsTop(cost, costMemo=None):
    size = len(cost)
    if costMemo is None:
        costMemo = {0: cost[0], 1: cost[1]}
    return min(minStepsTopHelper(cost, size - 1, costMemo), minStepsTopHelper(cost, size - 2, costMemo))


def minStepsTopHelper(cost, size, costMemo):
    if size == 0:
        return costMemo[0]
    if size == 1:
        return costMemo[1]
    if size not in costMemo:
        costMemo[size] = cost[size] + min(minStepsTopHelper(cost, size - 1, costMemo),
                                          minStepsTopHelper(cost, size - 2, costMemo))
    return costMemo[size]


print(minStepsBF([10, 15, 30]))
print(minStepsBF([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
print(minStepsBottomUp([10, 15, 30]))
print(minStepsBottomUp([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))

print(minStepsTop([10, 15, 30]))
print(minStepsTop([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
print(minStepsTop([10, 15, 30, 12]))
