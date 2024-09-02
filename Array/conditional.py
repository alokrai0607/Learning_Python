# print ("Please pass the value of Value1 & Value2 for Evaluation : ")
# value1 = int(input("First Number :"))
# value2 = int(input("Second Number :"))

# if (value1 > value2) :
#     print (value1 ,"is Greater than " , value2)
# elif (value2 > value1 ) :
#     print (value2 , "is Greater than " , value1)
# elif (value2 == value1 ) : 
#     print ("both are equal")
# else :
#     print ("Please Check correct input ")


# -------------------------------------------------------------------------------

print("Please pass the value of Value1 & Value2 for Evaluation : ")

def get_value(prompt):
    value = input(prompt)
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            return get_value(prompt)


value1 = get_value("First Number: ")
value2 = get_value("Second Number: ")

if value1 > value2:
    print(value1, "is Greater than", value2)
elif value2 > value1:
    print(value2, "is Greater than", value1)
else:
    print("Both are equal")
