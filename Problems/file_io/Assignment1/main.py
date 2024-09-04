
with open(r"C:\Users\91904\OneDrive\Desktop\Learning_Python\Problems\file_io\Assignment1\newFile.txt","w") as f:
    data = f.write(" Hii Everyone \n We are learning file i/o \n using Java \n I like Programing in Java")
    print(data)


with open(r"C:\Users\91904\OneDrive\Desktop\Learning_Python\Problems\file_io\Assignment1\newFile.txt","w+") as f:
    data = f.write(" Hii Everyone \n We are learning file i/o \n using Python \n I like Programing in Python")
    print(data)