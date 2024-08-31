number = 12345
new = str(number)
bag = ""
for i in new:
    bag = i + bag  # Add each digit to the front of the 'bag' string

print(bag)
