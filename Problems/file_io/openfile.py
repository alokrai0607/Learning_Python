f = open(r"C:\Users\91904\OneDrive\Desktop\Learning_Python\Problems\file_io\demo.txt", "r")
data = f.read()
print(data)
f.close()


#Way 2
f = open(r"C:\Users\91904\OneDrive\Desktop\Learning_Python\Problems\file_io\demo.txt", "r")
line1 =f.readline()
print(line1)

#append 
f = open(r"C:\Users\91904\OneDrive\Desktop\Learning_Python\Problems\file_io\demo.txt", "a")
f.write("Also i want to learn JS")
print(f)
f.close()

#Rewrite
f = open(r"C:\Users\91904\OneDrive\Desktop\Learning_Python\Problems\file_io\demo.txt", "w")
f.write("I hope all clear")
print(f)
f.close()
