# s = {1, 2, 3, 4, 5, 6, 7, 8}
def removeElum(s=()):
    box = set()
    for i in s :
        if i%3 != 0:
            box.add(i)
    return box

print(removeElum({1, 2, 3, 4, 5, 6, 7, 8}))