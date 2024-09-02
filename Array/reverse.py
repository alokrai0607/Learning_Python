#Write a Python program that accepts the user's first and last name 
# and prints them in reverse order with a space between them.


string = "Alok Rai"

for i in range(len(string)-1,-1,-1):
    print(string[i],end="")