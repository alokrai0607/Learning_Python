word = "Everyone"
with open(r"C:\Users\91904\OneDrive\Desktop\Learning_Python\Problems\file_io\Assignment1\newFile.txt","r") as f:
    data = f.read()
    if (data.find(word) != -1 ):
        print("Found")
    else:
        print("Not Found")



def check_line():
    word = "learning"
    data = True
    lineNo = 1
    with open(r"C:\Users\91904\OneDrive\Desktop\Learning_Python\Problems\file_io\Assignment1\newFile.txt","r") as f:
        while data :
            data = f.readline()
            if(word in data):
                print(f"{word}","is in line no :",lineNo)
                return
            lineNo += 1

    return -1

check_line()