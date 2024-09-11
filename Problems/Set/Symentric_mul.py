def symmetric_difference_of_three(set1, set2, set3):
    return set1 ^ set2 ^ set3

set1 = {1, 2, 3} 
set2 = {3, 4, 5}
set3 = {5, 6, 7}

result = symmetric_difference_of_three(set1, set2, set3)
print(result)   #{1, 2, 4, 6, 7}
