def blockPuzzleBF(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return blockPuzzleBF(n - 1) + blockPuzzleBF(n - 2)


def blockpuzzle_dp(N, puzzlememo=None):
    if puzzlememo is None:
        puzzlememo = {1: 1, 2: 2}
    if N not in puzzlememo:
        puzzlememo[N] = blockpuzzle_dp(N - 1, puzzlememo) + blockpuzzle_dp(N - 2, puzzlememo)
    return puzzlememo[N]


print(blockpuzzle_dp(5))
print(blockpuzzle_dp(9))
