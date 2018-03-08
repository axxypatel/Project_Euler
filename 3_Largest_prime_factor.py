# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
# In Below code, I have used two approach to get the largest prime factor

import math
number = 13195
number2 = 600851475143
prime_list = []
prime_list2 = []


def is_prime(x):  # simple primality test algorithm implemented
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


for i in range(2, number):  # Traditional approach to search the prime factor
    if number % i == 0:
        if is_prime(i):
            prime_list.append(i)


def check_prime(numb):    # New approach which is way faster than the usual one
    j = 2
    while numb > 1:
        if numb % j == 0:
            prime_list2.append(j)
            numb = int(numb/j)
            while True:
                if numb % j != 0:
                    break
                else:
                    numb = numb/j
                    prime_list2.append(j)
        j += 1


check_prime(number2)
print(prime_list)
print(max(prime_list))
print(prime_list2)
print(max(prime_list2))
