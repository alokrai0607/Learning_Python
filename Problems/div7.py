# Print all numbers from 1 to 100 that are divisible by 7.

for i in range(1,50):
    if(i%7==0):
        print(i,end=" ")

#Way 2nd
def print_mul(start,end):
    for i in range(start,end):
        if(i%7==0):
            print(i,end=" ")

print(print_mul(1,50))