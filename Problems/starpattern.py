
# * 
# * * 
# * * * 
# * * * * 


for i in range(1,5):
    for j in range(i):
        print("*",end=" ")
    print()


    #with function


def patternOne(n):
        for i in range(1,n):
            for j in range(i):
                print("*",end=" ")
            print()

print(patternOne(10))