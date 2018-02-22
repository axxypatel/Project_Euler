# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
#2000000


import math
below_numb= 2000000

def is_prime(numb): # use simple primality test algorithm having O(sqrt(N)) time complexity

    if numb == 2 or numb == 3:
        return True
    if numb % 2 == 0:
        return False
    if numb % 3 == 0:
        return False
    i = 5
    sqrt_numb = int(math.sqrt(numb))

    while i <= sqrt_numb: # Check till square root of number and test the divisibity
        if numb % i == 0:
            return False
        i += 2
    return True


def calc_sum(below_numb):
    sum=0
    for i in range(2,below_numb):
        if is_prime(i) == True:
            sum = sum+i

    return sum

sum= calc_sum(below_numb)
print("Sum:",sum)
