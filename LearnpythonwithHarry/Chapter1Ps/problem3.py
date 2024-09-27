import os


directory = "C:/Users/91904/OneDrive/Desktop/"
contents = os.listdir(directory)
print("Contents of the directory:")
for item in contents:
    print(item)
