
# we cant pass any list value under the set .
#Sets are mutable because we can add and remove element from set .
emptySet = set()

#add element in empty set
emptySet.add(2)
emptySet.add(3)
emptySet.add(2)
print(emptySet)   #{2, 3}


#Remove element from set
emptySet.remove(2)
print(emptySet)  #{3}

#if we want to clear set then we will use clear method .
emptySet.clear()
print(emptySet)  #set()

emptySet.add(2)
emptySet.add(3)
emptySet.add(2)
emptySet.add(5)
emptySet.add(7)
emptySet.add(9)
print(emptySet) #{2, 3, 5, 7, 9}
emptySet.pop()
print(emptySet) #{3, 5, 7, 9}

emptySet.pop()
print(emptySet) #{5, 7, 9}   will remove element in randome order from empty set.