def DACDays(days, counts, start, end):
    if start < end:
        mid = (start + end) // 2
        DACDays(days, counts, start, mid)
        DACDays(days, counts, mid + 1, end)
    else:
        counts[days[start] - 1] = counts[days[start] - 1] + 1


def MajorityDays(days):
    dayCounts = [0, 0, 0, 0, 0, 0, 0]
    start = 0
    end = len(days) - 1
    DACDays(days, dayCounts, start, end)
    maxDay = max(dayCounts)
    return (dayCounts.index(maxDay, 0, len(dayCounts))) + 1


print(MajorityDays([1, 1, 3, 4, 5, 6, 2]))
print(MajorityDays([3, 2, 3]))
print(MajorityDays([2, 2, 1, 1, 1, 2, 2]))
