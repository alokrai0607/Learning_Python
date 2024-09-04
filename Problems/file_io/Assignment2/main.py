
with open(r"C:\Users\91904\OneDrive\Desktop\Learning_Python\Problems\file_io\Assignment2\prectice.txt","r") as f:
    data = f.read()
    #print(data)

#1st way
    num=""
    for i in range(len(data)):
        if(data[i]==","):
            print(num)
            num=""
        else:
            num += data[i]
    
#2nd way
count = 0
with open(r"C:\Users\91904\OneDrive\Desktop\Learning_Python\Problems\file_io\Assignment2\prectice.txt","r") as f:
    data = f.read()
    nums = data.split(",")
    for value in nums :
        if(int(value)%2 == 0):
            count += 1
    print(count)
        
