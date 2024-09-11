li = [1,2,3,4,5,6,4,5,6,4,5,6,1,2,3,4,5,6,4,5,6,2,5,2,1,0,2,0,2,1,2,2,2,2,2,1]

emptyset = set()

for i in range(0,len(li)-1,1):
    emptyset.add(li[i])
print(emptyset)