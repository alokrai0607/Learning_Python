#direct 
n = 10
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end=" ")
    print()




#using function
def boxpattern(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print("*",end=" ")
        print()
print(boxpattern(5))