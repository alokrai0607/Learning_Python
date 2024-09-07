#Write a program that checks whether a given year is a leap year. 
# A year is a leap year if it is divisible by 4 but not divisible by 100,
#  except if it is divisible by 400.

def leepCalc(year):
    if (year%4==0 and year%100 != 0) or year%400 == 0:
        print(f"{year}"" is Leap Year")
    else:
        print(f"{year}"" is not a Leap Year")

print(leepCalc(2021))
print(leepCalc(2022))
print(leepCalc(2000))
print(leepCalc(2024))
         
