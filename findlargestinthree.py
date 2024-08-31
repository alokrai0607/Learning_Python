print ("Please pass your first Number here :")
first = int(input())

print("Please pass your Second Number here :")
second = int(input())

print("Please pass your third number here : ")
third = int(input())

if (first>second and first>third):
    print(f"{first}"," is grater than ",second ,"and", third)
elif (second>first and second>third):
    print(f"{second}"," is greater than ",first," and ",third)
elif (third>first and third>second):
    print(f"{third}", " is greater than ",first," and ",second)



#Using Function
def checkBig(first,second,third):
    if (first>second and first>third):
        print(f"{first}"," is grater than ",second ,"and", third)
    elif (second>first and second>third):
        print(f"{second}"," is greater than ",first," and ",third)
    elif (third>first and third>second):
        print(f"{third}", " is greater than ",first," and ",second)
    elif (first==second==third):
        print("all Qqual")
    else:
        print("Issue")

print(checkBig(1,25,65))
