def febo(n):
    a,b = 0,1
    i = 0

    while i < n:
        print(a," ")
        a,b = b,a+b
        i += 1

print(febo(10))