with open(r"C:\Users\91904\OneDrive\Desktop\Learning_Python\Problems\file_io\demo2.txt", "r") as f:
    data = f.read()
    print(data)

with open(r"C:\Users\91904\OneDrive\Desktop\Learning_Python\Problems\file_io\demo2.txt", "w") as f:
    f.write("New Data is here \n Hello My Name is Alok.")

with open(r"C:\Users\91904\OneDrive\Desktop\Learning_Python\Problems\file_io\demo2.txt", "a") as f:
    f.write("I am from vNS \n look at me .")

