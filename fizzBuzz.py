for i in range(1,100):
    if(i%3==0 & i%5==0):
        print("FizzBuzz",end=" ")
    elif(i%3==0):
        print("FIzz",end=" ")
    elif(i%5==0):
        print("Buzz",end=" ")
    else:
        print(i,end=" ")