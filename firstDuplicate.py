def firstDuplicate(a):
    non = set()
    for item in a:
        if item in non:
            return item
        else:
            non.add(item)
    return -1


a = [2, 1, 3, 5, 3, 2]
print(firstDuplicate(a))