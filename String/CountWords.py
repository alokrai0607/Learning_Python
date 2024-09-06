word = "Hello world, welcome to Python programming"
a = word.split(" ")
count = 0
for i in range(0,len(a)):
    count += 1
print("Total Count of word is :",count)