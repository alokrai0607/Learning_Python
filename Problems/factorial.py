def factorial_fun(n):
    bag=1
    for i in range(1,n+1):
        bag*=i
    print(bag)

print(factorial_fun(15))