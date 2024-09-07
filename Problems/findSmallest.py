numbers = [3, 1, 4, 1, 0,5, 9, 2, 6]

smallest = numbers[0]
for i in numbers:
    if(smallest>i):
        smallest=i
print(smallest)

#Smallest

numbers = [3, 1, 4, 1, 0,5, 9, 2, 6]
smallest = min(numbers)
print(smallest)
