tupvar = (1,5,7,8,9,4,3,7,6,9,8)
newtup = tupvar + (11,12,15,)
print(newtup)



#way 2
my_tuple = ("a","l","o","k")
mylist = list(my_tuple)
mylist.insert("r","a","i")
newtup = tuple(mylist)

print(newtup)
print(type(newtup))