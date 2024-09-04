def swap(a,b):
    a = int(input ("Please pass the first value Here : "))
    b = int(input ("Please pass the second value Here : "))
    a = a + b
    b = a - b
    a = a - b
    print("a will be : ",a)
    print("b will be : ",b)

swap(4,5)