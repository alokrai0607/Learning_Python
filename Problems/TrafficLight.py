
while True:
    
    light = input("Please pass your Traffic light color here (or type 'exit' to end): ")

    if light.lower() == "exit":
        print("Exiting the program. Goodbye!")
        break

    if light.lower() == "red":
        print("Stop here because light is", light)
    elif light.lower() == "yellow":
        print("You can get ready to go because light is:", light)
    elif light.lower() == "green":
        print("You can go because traffic light is:", light)
    else:
        print("Please enter a valid traffic light color or type 'exit' to end.")
