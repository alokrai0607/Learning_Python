def divide_numbers(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero."

# Input
num1 = 5
num2 = 0

# Output
output = divide_numbers(num1, num2)
print(output)
