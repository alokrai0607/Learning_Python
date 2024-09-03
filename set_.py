myset1 = {1,2,3,4,5,1,2}
print(myset1)   #{1, 2, 3, 4, 5}

#add(element)
myset1 = {1,2,3,4,5,1,2}
myset1.add(99)
print(myset1) #{1, 2, 3, 4, 5, 99}

#remove(element)
myset1 = {1,2,3,4,5,1,2}
myset1.remove(1)
print(myset1) #{2, 3, 4, 5}

#discard(element)Removes a specific element from the set if it is present. 
#Does not raise an error if the element is not found.
myset1 = {1,2,3,4,5,1,2}
myset1.discard(3)
print(myset1) #{1, 2, 4, 5}

#pop()
myset1 = {1,2,3,4,5,1,2}
myset1.pop()
print(myset1) #{2, 3, 4, 5}

# myset2 = {}
# myset2.pop()
#print(myset2) #TypeError: pop expected at least 1 argument, got 0

#clear()
myset1 = {1,2,3,4,5,1,2}
myset1.clear()
print(myset1) #set()

#union
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {5, 6, 7}

newset = set1.union(set2,set3)
print(newset)

#Intersection
set1 = {1, 2, 3}
set2 = {3, 1, 4}
set3 = {1, 3, 7}

newset = set1.intersection(set2,set3)
print(newset)
