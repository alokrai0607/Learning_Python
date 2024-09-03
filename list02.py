#Slicing (extract a portion of the list using slicing.)
my_list = [10, 20, 30, 40, 50]

print(my_list[0:2]) #[10, 20]
print(my_list[:-1]) #[10, 20, 30, 40]
print(my_list[0:])  #[10, 20, 30, 40, 50]
print(my_list[::2]) #[10, 30, 50]

#Appending Element
my_list = [10, 20, 30]
my_list.append(40)
print(my_list)  # [10, 20, 30, 40]


#Inserting Elements
my_list = [10, 20, 30]
my_list.insert(3,15) #[10, 15, 20, 30]  (3 is index)
print(my_list)

#Extending a List
my_list = [10, 20, 30]
my_list.extend([40, 50])
print(my_list)  # [10, 20, 30, 40, 50]

#Remove
my_list = [10, 20, 30, 20]
my_list.remove(20)
print(my_list)  # [10, 30, 20]


