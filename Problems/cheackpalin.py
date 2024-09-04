# name = "naman"
def cheack_palindrome(name):
    bag = ""

    for i in range(len(name)-1,-1,-1):
        bag += name[i]
    #print(bag)

    if(bag == name):
        print("Palindrome")
    else:
        print("Not Palindrome")

print(cheack_palindrome("NAMAN"))
print(cheack_palindrome("ASHISH"))
