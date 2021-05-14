def firstNotRepeatingCharacter(s):
    uniq = []
    for c in s:
        if not c in uniq:
            uniq.append(c)
    for it in uniq:
        count = 0
        for ch in s:
            if ch == it:
                count += 1
        if count == 1:
            return it

    return '_'

s = "abacabad"
print(firstNotRepeatingCharacter(s))