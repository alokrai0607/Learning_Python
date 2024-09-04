word = "Everyone"
with open(r"C:\Users\91904\OneDrive\Desktop\Learning_Python\Problems\file_io\Assignment1\newFile.txt","r") as f:
    data = f.read()
    if (data.find(word) != -1 ):
        print("Found")
    else:
        print("Not Found")