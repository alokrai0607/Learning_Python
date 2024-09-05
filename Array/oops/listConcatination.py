list1 = ["H","M","N","i","A"]
list2 = ["ey!","y","ame","s","lok"]
container =[]
min_len = min(len(list1),len(list2))

for i in range(min_len):
    container.append(list1[i] + list2[i])

container.extend(list1[min_len:])
container.extend(list2[min_len:])
print(container) #['Hey!', 'My', 'Name', 'is', 'Alok']