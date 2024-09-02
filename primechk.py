def prime_cheak(n):
    is_prime = True
    #I used int(n ** 0.5) + 1 as the 
    # upper bound for the loop, which
    # is a more efficient way to check 
    # for prime numbers.
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Number is Prime")
    else:
        print("Number is not prime")

prime_cheak(17)