# Write a Python program to find the largest of three numbers.
#Way 1
numbers = [1,5,6,9,2,4,7,3]  #9,7,6
numbers.sort(reverse=True)
print(numbers[0:3]) #[9, 7, 6]


#fing largest in three 
def findlargest(a, b, c):
    numbers = [a, b, c]
    largest = numbers[0]

    for i in range(1, len(numbers)):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest

print(findlargest(11, 22, 3))
