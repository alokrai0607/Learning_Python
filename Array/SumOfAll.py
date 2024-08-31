#Addnin reverse Order
arr = [10, 20, 30, 40]
Sum=0
for i in range(len(arr)-1,-1,-1):
    Sum += arr[i]
print(Sum)


#Add in simple order
arr = [10, 20, 30, 40]
Sum=0
for i in range(-1,len(arr)-1,1):
    Sum += arr[i]
print(Sum)

