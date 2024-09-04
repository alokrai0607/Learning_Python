#Write a program that finds all numbers between 1 and 1000 
# that are divisible by 7 but are not multiples of 5.

for i in range(1,1000):
    if(i%7 == 0 and i%5 == 1):
        print(i)
