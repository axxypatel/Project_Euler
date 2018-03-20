# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
# 2000000
import math

below_numb = 2000000


def is_prime(numb):  # use simple primality test algorithm having O(sqrt(N)) time complexity

    if numb == 2 or numb == 3:
        return True
    if numb % 2 == 0:
        return False
    if numb % 3 == 0:
        return False
    i = 5
    srt_numb = int(math.sqrt(numb))

    while i <= srt_numb:  # Check till square root of number and test the divisibity
        if numb % i == 0:
            return False
        i += 2
    return True


def calc_sum(below_numb1):
    total_sum = 0
    for i in range(2, below_numb1):
        if is_prime(i) is True:
            total_sum = total_sum + i

    return total_sum


total_sum1 = calc_sum(below_numb)
print("Sum:", total_sum1)
