#Popping Elements
mylist = [10,20,30,40,50]
a = mylist.pop() #50
print(mylist) #[10, 20, 30, 40]

#Reversing a List
mylist = [10,20,30,40,50,60,70,80,90,100]
mylist.reverse()
print(mylist)

#Sorting a List
mylist = [10,20,30,40,50,60,70,80,90,100]
mylist.sort(reverse=False)
print(mylist)
mylist.sort(reverse=True)
print(mylist)

#Finding the Length of a List
mylist = [10,20,30,40,50,60,70,80,90,100]
res = (len(mylist))
print(res)

#Counting Elements
mylist = [1,2,3,4,1,2,3,4,4,4,5,6,7,8,9,0,9,1,4]
a = mylist.count(4)
print(a)   #5

#List Comprehension
mylist = [1,2,3,4]
listComp = [x**2 for x in mylist]
print(listComp)

#2nd way
mylist = [1,2,3,4]
for x in range(1,len(mylist)+1,1):
    print(x**2,end=" ")
 