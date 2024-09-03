#sum()

my_tup = (9,8,7,6,5,4,3,2,1)
print(sum(my_tup))

sum = 0
for i in range(0 , len(my_tup), 1):
        sum += my_tup[i]
print(sum)


#sorted()
#Returns a new list containing all tuple elements in ascending order

my_tup = (5,6,8,7,2,8,2,1,3)
print(sorted(my_tup))

#way2
def sortingmachine(arr):
    arr = list(arr)
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

my_tup = (5, 6, 8, 7, 2, 8, 2, 1, 3)
print(sortingmachine(my_tup))
