#  Create a Python program that uses a loop to calculate the sum of all 
#  numbers divisible by 3 or 5 below 1000.


def calculator(n):
    sum = 0
    for i in range(1,n):
        if i%3==0 or i%5==0:
            sum += i
    return sum
print(calculator(10000))