def fab_fun(n):
    a, b = 0, 1  
    for i in range(n):
        print(a, end=' ')  
        a, b = b, a + b  

fab_fun(5)


def fab_function(n):
    a,b = 1,2
    for i in range (n):
        print(a, end=" ")
        a,b = b,a+b

fab_function(10)
