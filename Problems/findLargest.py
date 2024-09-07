numbers = [3, 1, 4, 1, 5, 9, 2, 6]

largest = numbers[0]
for i in numbers :
    if i>largest:
        largest=i
print(largest)
#way2
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
largest = max(numbers)
print(largest)