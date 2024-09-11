
#Write a function that checks if there are any duplicate elements in a list
#using a set. Return True if duplicates are found, otherwise return False.

def hasDuplicates(inpList):
    setContainer = set()
    for element in inpList:
        if element in setContainer:
            return True
        else:
            setContainer.add(element)
    return False


list1 = [1,2,3,4,5,6,7,8,9]
list2 = [2,3,5,8,8,6,8,2,6,2,4,1,2,41,5,5]

print(hasDuplicates(list1)) #False
print(hasDuplicates(list2)) #True

