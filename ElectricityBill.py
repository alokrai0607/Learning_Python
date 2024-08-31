# Write a program that calculates the electricity bill based on the following conditions:
# For the first 100 units: ₹10 per unit
# For the next 100 units: ₹15 per unit
# For units above 200: ₹20 per unit
# Example:
# Input: 250 units
# Output: "Total bill: ₹3500"


def billCalc(unit):
    if unit<=100:
        return unit*10
    elif unit <= 200 and unit > 100 :
        return 100*10 + (unit-100)*15
    else:
        return 100*10 + 100*15 + (unit-200)*20
    
print(billCalc(250))