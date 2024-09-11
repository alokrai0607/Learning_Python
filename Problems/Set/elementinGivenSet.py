def is_elem_in_givenSet(elem , gvnSet):
    return elem in gvnSet 

sample = {1,3,4,6,7,9}

print(is_elem_in_givenSet(1,sample))
print(is_elem_in_givenSet(2,sample))
print(is_elem_in_givenSet(4,sample))
print(is_elem_in_givenSet(5,sample))
print(is_elem_in_givenSet(6,sample))
print(is_elem_in_givenSet(11,sample))
print(is_elem_in_givenSet(9,sample))