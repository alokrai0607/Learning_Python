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

#Creating a Tuple From dict
my_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
my_tuple = tuple(my_dict.items())
print(my_tuple)  

#Dictionary to Tuple
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_tuple = tuple(my_dict)  
print(my_tuple)  #('a', 'b', 'c')

#all()
# Returns True if all elements in the tuple are true 
my_tuple = (1, 2, 3)
print(all(my_tuple))  # True
my_tuple = (1, 0, 3)
print(all(my_tuple))  # False

#any()
# Returns True if at least one element in the tuple is true.
my_tuple = (0, 0, 3)
print(any(my_tuple))  # true
my_tuple = (0, 0, 0)
print(any(my_tuple))  # false

#enumerate
# can be converted to a list of tuples where each tuple contains the index
# and the corresponding element.

mytuple = ("a","b","c","d")
for index,value in enumerate(my_tuple):
    print(index,value)

#zip()
#Combines elements from two or more iterables (e.g., lists, tuples) into tuples.
tuple1 = (30, 20, 50)
tuple2 = ('alok', 'Harshit', 'Vishal')
zipped = zip(tuple1, tuple2)
print(list(zipped))  #  [(30, 'alok'), (20, 'Harshit'), (50, 'Vishal')]

#reversed
my_tuple = (10, 20, 30)
reversed_tuple = tuple(reversed(my_tuple))
print(reversed_tuple)  # (30, 20, 10)






