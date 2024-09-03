inp = int(input("Please pass the value for get you factorial value  which you want :  "))
prod = 1
for i in range(1,inp+1):
    prod *= i
print(prod)


#i am writing factorial function .

def fun_fact(n):
    product=1
    for i in range(1,n+1):
        product *= i
    return product

print(fun_fact(5))