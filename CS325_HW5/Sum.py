from copy import deepcopy


def combination_sum_helper(remainder, length, combo, result, last):
    if remainder == 0 and length == 0:
        result.append(deepcopy(combo))
        return
    if remainder < 0 or length < 0:
        return
    for i in range(last, 10):
        combo.append(i)
        combination_sum_helper(remainder - i, length - 1,
                               combo, result, i + 1)
        combo.pop()


def combination(n, k):
    result = []
    combination_sum_helper(n, k, [], result, 1)
    return result


print(combination(9, 3))
