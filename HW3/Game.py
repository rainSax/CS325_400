def game_topdown(N):
    turn = 0
    return game_topHelper(N, turn)


def game_topHelper(N, turn):
    if turn % 2 != 0 and N == 1:
        return True
    elif turn % 2 == 0 and N == 1:
        return False
    turn = turn + 1
    return game_topHelper(N - divisionHelper(N), turn)


def divisionHelper(N):
    val = N - 1
    if N > 1:
        while True:
            if N % val == 0:
                return val
            val = val - 1


def game_bottomup(N):
    values = [0] * N
    values[0] = 1
    values[1] = 2
    turn = 1
    for i in range(2, N):
        values[i] = values[i - 1] + multiplyHelper(values[i - 1], N)
        turn = turn + 1
        if values[i] == N:
            break
    if turn % 2 != 0:
        return True
    else:
        return False


def multiplyHelper(current, maxVal):
    if current + current > maxVal:
        return 1
    else:
        factor = 1
        while (current * factor) + current < maxVal:
            factor = factor + 1
        return current * (factor - 1)


print(game_topdown(2))
print(game_topdown(3))
print(game_topdown(5))
print(game_bottomup(2))
print(game_bottomup(3))
print(game_bottomup(5))
print(game_bottomup(50))
