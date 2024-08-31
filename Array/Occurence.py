Array= [1, 2, 2, 3, 4, 2, 5]
n = int(input())
count=0
for i in range(0,len(Array),1):
        if(Array[i]==n):
                count += 1
print(count)