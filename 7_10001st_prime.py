# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number? 104743
import random
import math

prime_pos = 10001


# Fermat method algorithm implemented to check the prime number
def power(a, n, k):
    res = 1
    a = a % k

    while n > 0:
        if (n & 1) == 1:
            res = (res * a) % k

        n = n >> 1
        a = (a * a) % k
    return res


def is_prime_fermat(numb):  # This method is slow in this problem
    if numb <= 1 or numb == 4:
        return False
    if numb <= 3:
        return True

    k = 3

    while k > 0:
        a = 2 + random.randint(2, numb-2) % (numb - 4)
        if power(a, numb - 1, numb) != 1:
            return False
        k -= 1
    # print("Prime:",numb)
    return True


# simple primality test algorithm implemented
def is_prime_primal(x):  # This code is fast in current problem
    if x <= 1:
        return False
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False

    i = 5
    while i*i <= x:  # check divisibility till the square root of the number
        if x % i == 0 or x % (i + 2) ==0 :
            return False
        i += 6
    return True


def check_cond(prime_pos1):
    numb_position = 0
    j = 2
    while True:
        if is_prime_primal(j):
            numb_position += 1
            # print(numb_position)
            if numb_position == prime_pos1:
                print("Position of the prime number:", numb_position, "\n", "Prime Number:", j)
                break
        j += 1


check_cond(prime_pos)
