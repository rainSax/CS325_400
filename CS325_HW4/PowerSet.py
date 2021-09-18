def powerset_helper(pointer, choices_made, input, result):
    if pointer < 0:
        # append choices_made to results # make a deep copy since we are working with objects
        result.append(deep_copy(choices_made))
        return

    choices_made.append(input[pointer])
    powerset_helper(pointer - 1, choices_made, input, result)
    # backtracking
    # remove last element added to choices_made
    choices_made.pop()
    powerset_helper(pointer - 1, choices_made, input, result)


def powerset(input):
    result = []
    powerset_helper(len(input) - 1, [], input, result)
    return result


def deep_copy(obj):
    # base case for single elements
    if type(obj) != list:
        return obj
    copy = []
    for i in range(len(obj)):
        copy.append(deep_copy(obj[i]))
    return copy


print(powerset([1, 2, 3]))
print(powerset("ABC"))
