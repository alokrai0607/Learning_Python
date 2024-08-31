#Way 1
name = "radar"
bag = ""
for i in range(len(name)-1, -1, -1):
    bag += name[i]

if bag == name:
    print("It is a palindrome")
else:
    print("It is not a palindrome")

#Way 2 
def check_palindrome(word):
    container=""
    for i in range(len(word)-1,-1,-1):
        container += word[i]

    if word==container:
        print("It is Palindrome")
    else:
        print("It is not a Palindrome")

print(check_palindrome("Hello"))
print(check_palindrome("MadaM"))