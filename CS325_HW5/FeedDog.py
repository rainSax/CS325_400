# dogs can only get one biscuit
# same biscuit can't be given to 2 dogs


def feedDog(hunger_level, biscuit_size):
    count = 0
    fedDogs = [False] * len(hunger_level)
    usedBiscuits = [False] * len(biscuit_size)
    for i in range(0, len(biscuit_size)):
        for j in range(0, len(hunger_level)):
            if not fedDogs[j] and not usedBiscuits[i]:
                if biscuit_size[i] == hunger_level[j]:
                    count += 1
                    fedDogs[j] = True
                    usedBiscuits[i] = True
    for i in range(0, len(biscuit_size)):
        for j in range(0, len(hunger_level)):
            if not fedDogs[j] and not usedBiscuits[i]:
                if biscuit_size[i] > hunger_level[j]:
                    count += 1
                    fedDogs[j] = True
                    usedBiscuits[i] = True
    return count


# print(feedDog([1, 2, 3], [1, 1]))
# print(feedDog([1, 2], [1, 2, 3]))
print(feedDog([2, 3, 4], [1, 2, 3]))
print(feedDog([3, 4, 2], [4, 6, 3]))
