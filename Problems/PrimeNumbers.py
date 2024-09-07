#Print all prime numbers between 1 and 100. (A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.)
bag = ""
for num in range(1,101):
    count=0
    for i in range(1,num+1):
        if(num % i==0):
            count += 1

    if count==2:
      bag += str(num)+" "
      
print(bag)


