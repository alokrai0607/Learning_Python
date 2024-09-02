def plist(li):
    li = list(input("Pass your input in list : "))
    bag = ""
    for i in range(0,len(li),1):
        if(li[i]%2==0):
            bag += li[i]
        return bag
    
    print(plist([1,2,3,4,5,6,7,8,9]))