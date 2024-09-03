tup = (1,5,9,3,5,7,4,5,6,8,5,2,1,2,5,4,4,2,5,1,0,0)
min = tup[0]
for i in range(0,len(tup)-1,1):
    if tup[i]<min:
        min = tup[i]
print(min)


#2nd way
tup = (1,5,9,3,5,7,4,5,6,8,5,2,1,2,5,4,4,2,5,1,0,0)
print(min(tup))

