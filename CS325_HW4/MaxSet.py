# max_set runs in O(n) time
def max_independent_set(nums):
    elements = []
    # check for all negative
    allNeg = True
    for i in range(len(nums)):
        if nums[i] > 0:
            allNeg = False
    if allNeg:
        return elements
    maxSum = [0] * len(nums)
    maxSum[0] = nums[0]
    maxSum[1] = nums[1]
    chosenidx = lastchosenidx = len(nums) + 1
    for i in range(1, len(nums)):
        choice1 = maxSum[i - 1]
        if i == 1:
            choice2 = 0
        else:
            choice2 = maxSum[i - 2]
        maxSum[i] = max(choice1, nums[i] + choice2)
        if maxSum[i] == choice1:
            chosenidx = i - 1
        else:
            chosenidx = i
        if chosenidx - lastchosenidx > 1 or i == 1:
            elements.append(nums[chosenidx])
            lastchosenidx = chosenidx
    return elements


print(max_independent_set([3, 5, 7, 10]))
