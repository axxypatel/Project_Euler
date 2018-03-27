# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
# (i) each of the three terms are prime
# (ii) each of the 4-digit numbers are permutations of one another.
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

# What 12-digit number do you form by concatenating the three terms in this sequence?
from itertools import permutations
upper_limit = 10000
lower_limit = 1488
prime_list = []


def is_prime(x):  # simple primality test algorithm implemented
        import math
        if x <= 1:
            return False
        if x == 2 or x == 3:
            return True
        if x % 2 == 0 or x % 3 == 0:
            return False

        y = 5
        sqt_numb = int(math.sqrt(x))

        while y <= sqt_numb:  # check divisibility till the square root of the number
            if x % y == 0:
                return False
            y += 2
        return True


def generate_prime_list():
    i = lower_limit
    while i < upper_limit:
        if is_prime(i):
            prime_list.append(i)
        i += 1


def check_numb():
    for first_numb in range(0, len(prime_list)):
        for second_numb in range(first_numb+1, len(prime_list)):
            temp_permutation = [''.join(i) for i in list(permutations(str(prime_list[first_numb])))]
            third_numb = prime_list[second_numb] + (prime_list[second_numb] - prime_list[first_numb])
            if third_numb < upper_limit and is_prime(third_numb):
                if str(third_numb) in temp_permutation and str(prime_list[second_numb]) in temp_permutation:
                    print("Number is:", str(prime_list[first_numb])+str(prime_list[second_numb])+str(third_numb))
                    return


generate_prime_list()
check_numb()
