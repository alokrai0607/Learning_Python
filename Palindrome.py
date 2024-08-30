name = "radar"
bag = ""

for i in range(len(name)-1, -1, -1):
    bag += name[i]

if bag == name:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
