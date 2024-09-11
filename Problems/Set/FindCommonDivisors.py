#Write a function that takes two integers and returns a set of their
#common divisors. For example, for num1 = 12 and num2 = 18, the common divisors
#would be {1, 2, 3, 6}.


def CommanDiv(num1 , num2):

    def divisors(n):
        return {i for i in range(1, n+1) if n % i == 0}
    divisors_num1 = divisors(num1)
    divisors_num2 = divisors(num2)

    return divisors_num1 & divisors_num2

num1 = 12
num2 = 18

common_divs = CommanDiv(num1, num2)
print(common_divs)

