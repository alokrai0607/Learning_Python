List = [12, 75, 150, 180, 145, 525, 50]

for number in List:
    
    if number % 50 == 0:
        if number > 500:
            break
        elif number > 150:
            continue
        print(number)
