def patternmatch2(string, p):
    strLen = len(string)
    pLen = len(p)
    matrix = [[False for i in range(pLen + 1)] for j in range(strLen + 1)]
    matrix[0][0] = True
    string = "_" + string
    p = "_" + p
    for i in range(1, pLen + 1):
        if p[i] == '*':
            matrix[0][i] = matrix[0][i - 1]
    for i in range(1, strLen + 1):
        for j in range(1, pLen + 1):
            if string[i] == p[j] or p[j] == '?':
                matrix[i][j] = matrix[i - 1][j - 1]
            if p[j] == '*':
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
    return matrix[strLen][pLen]


print(patternmatch2("ba", "*a"))
print(patternmatch2("ba", "*"))
print(patternmatch2("bab", "*?*"))
print(patternmatch2("abacd", "*a?a*"))
print(patternmatch2("abacd", "*a?a*"))
print(patternmatch2("abacd", "***cd"))
