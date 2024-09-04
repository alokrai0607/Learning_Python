# Write a function that takes a list of numbers and returns the
# sum of the squares of the numbers.

def sum_of_squares(numbers:list):
    total = 0
    for number in numbers:
        total += number ** 2
    return total

print(sum_of_squares([11,22,33]))

