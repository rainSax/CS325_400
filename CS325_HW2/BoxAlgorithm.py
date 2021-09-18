def doBoxesOverlap(box1, box2):
    # check if the x ranges are overlapping
    if box1[0] < box2[2] and box2[0] < box1[2]:
        # check if the y ranges are overlapping
        if box1[1] < box2[3] and box2[1] < box1[3]:
            return True
    return False


boxA = [3, 3, 5, 5]
boxB = [2, 4, 4, 6]

boxC = [0, 0, 2, 2]
boxD = [1, 1, 3, 3]

print(doBoxesOverlap(boxA, boxB))
print(doBoxesOverlap(boxC, boxD))
