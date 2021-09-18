def checkPalindrome_1(string, k):
    i = len(string) - 1
    j = 0
    while i > -1:
        if string[i] != string[j]:
            if k > 0:
                # remove string[i] from string
                string = string[:i] + string[i + 1:]
                i -= 1
                k -= 1
                continue
            else:
                return False
        if i == j and k == 1:
            string = string[:i] + string[i + 1:]
            i -= 1
        i -= 1
        j += 1
    return True


def checkPalindrome_2(string, k):
    counts = {}
    odd = 0
    for letter in string:
        if letter not in counts:
            counts[letter] = 1
        else:
            counts[letter] += 1
    for key, val in counts.items():
        odd += val % 2
    if odd <= (k + 1):
        return True
    else:
        return False


print(checkPalindrome_1("abcdcba", 1))
print(checkPalindrome_1("abcdeba", 2))
print(checkPalindrome_1("abcdeba", 1))
print(checkPalindrome_1("abcdea", 3))

print(checkPalindrome_2("abcdcba", 1))
print(checkPalindrome_2("abcdeba", 2))
print(checkPalindrome_2("abcdeba", 1))
print(checkPalindrome_2("abcdea", 3))
