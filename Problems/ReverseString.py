 #  Way 1
name = "ALOK"
reverseName = name[::-1]#is a Pythonic way to reverse a string using slicing
print(reverseName)

#Way 2 
name = "Alok Kumar Rai"
bag = ""
# (for i in range(len(name)length , Stop , Step):)
for i in range(len(name)-1,-1,-1):
    bag += name[i]
print(bag)

#Way 3
def reverse_string(string):
    if len(string) == 0:
        return string
    else:
        return reverse_string(string[1:]) + string[0]#( slices the string to get all characters except the first one)
my_string = "Alok Kumar Rai"
rev_string = reverse_string(my_string)
print(rev_string)