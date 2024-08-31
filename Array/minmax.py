list = [3, 5, 7, 2, 8]

largest =list[0]
smallest=list[0]

for i in list:
    
    if(i>largest):
        largest = i
  
    if(i<smallest):
        smallest = i
    
print("Smallest:", smallest)
print("Largest:", largest)

#way 2
list = [3, 5, 7, 2, 8]

smallest = min(list)
largest = max(list)
print("Smallest:", smallest)
print("Largest:", largest)

