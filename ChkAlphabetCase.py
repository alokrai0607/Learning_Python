#Write a program that takes a single character as input and checks whether it is uppercase or lowercase.

def cheack_char(val):
    if val.islower():
        print(f"{val}"," :is in lower case")
    elif val.isupper():
        print(f"{val}"," :is in Upper case")

cheack_char("a")
cheack_char("A")
cheack_char("Y")
cheack_char("1") #it will not work
