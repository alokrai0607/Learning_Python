#index(element)
my_tuple = (10, 20, 30)
print(my_tuple.index(20))  # Output: 1

#count(element) : Returns the number of times the specified element appears in the tuple.
my_tuple = (10, 20, 30)
print(my_tuple.count(50))#0
print(my_tuple.count(10))#1

# in keyword

my_tuple = (10, 20, 30)
print(20 in my_tuple) #True
print(40 in my_tuple)  

#tuple() : Converts an iterable into a tuple.
my_list = [10, 20, 30]
my_tuple = tuple(my_list)
print(my_tuple)  # Output: (10, 20, 30)

