
def countUniqW(word):
    newWord = word.split(" ")
    newSet = set()
    for i in newWord:
        newSet.add(i)

    return(len(newSet))

print(countUniqW("Hello Hii how are you ! Hello"))  #6
print(countUniqW("One Two Ka Four Four Two Ka One"))   #4