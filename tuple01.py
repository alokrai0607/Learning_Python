# #Returns the number of elements in a tuple.

tup = (1,5,9,3,5,7,4,5,6,8,5,2,1,2,5,4,4,2,5,1,0,0)
print(len(tup))   #22

# #Returns the largest element in the tuple
tup = (1,5,9,3,5,7,4,5,6,8,5,2,1,2,5,4,4,2,5,1,0,0)
print(max(tup))

#way2
maximum = tup[0]
for i in range(0,len(tup),1):
    #print(tup[i],end=" ")
    if(tup[i]>maximum):
        maximum = tup[i]
print(maximum)