number = 13  
count = 0  

for num in range(1, number + 1):
    if number % num == 0:
        count += 1
if count == 2:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")



