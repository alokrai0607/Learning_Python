 #  Way 1
name = "ALOK"
reverseName = name[::-1]
print(reverseName)

#Way 2 
name = "Alok Kumar Rai"
bag = ""
for i in range(len(name)-1,-1,-1):
    bag += name[i]
print(bag)

#Way 3
def reverse_string(string):
    if len(string) == 0:
        return string
    else:
        return reverse_string(string[1:]) + string[0]
my_string = "Alok"
rev_string = reverse_string(my_string)
print(rev_string)