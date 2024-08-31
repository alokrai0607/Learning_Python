# Write a program to find the second largest element in an array.

arr = [12, 35, 1, 10, 34, 1]
arr.sort()
p= arr[-2]
print(p)


#2nd way
arr = [12, 35, 1, 10, 34, 1]
    
if len(arr)<2:
    print ("Array should be more than 2 elements present in athe array")
else:
    arr.sort()
    p = arr[-2]
    print(p)
