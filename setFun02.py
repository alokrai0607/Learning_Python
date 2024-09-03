#difference

set1 = {2,3,4}
set2 = {4,5,6}
newSet = set1.difference(set2) 
print(newSet) #{2, 3}

#symmetric_difference
set1 = {2,3,4}
set2 = {4,5,6}
newSet = set2.symmetric_difference(set1)
print(newSet)        #{2, 3, 5, 6}


set1 = {1, 2}
set2 = {1, 2, 3}
print(set1.issubset(set2))  # True
print(set2.issubset(set1))  # False

#issuperset
set1 = {1, 2, 3}
set2 = {1, 2}
print(set1.issuperset(set2))  # True
print(set2.issuperset(set1))  # False


#isdisjoint
#Checks if the set has no elements in common with another set.
set1 = {1,2,3}
set2 = {4,5,6}

print(set1.isdisjoint(set2)) #true
print(set2.isdisjoint(set1)) #true

