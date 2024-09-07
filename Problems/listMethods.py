list = [5,9,7,8,1,3,2]

#append(element)
list.append(11)
print(list)

#sort
list.sort()
print(list)

#sort + reverse Order
list.sort(reverse=True)
print(list)

#not reverse(acending)
list.sort(reverse=False)
print(list)

#insert(index,value)
list.insert(3,"A")
print(list)


#sort
str = ['z','d','s','a','c']
str.sort()
print(str)


#sort(reverse=True)
str = ['z','d','s','a','c']
str.sort(reverse=True)
print(str)


#remove
str = ['z','d','s','a','c']
str.remove("z")
print(str)  


#pop
str = ['z','d','s','a','c']
str.pop(-3)
print(str)
