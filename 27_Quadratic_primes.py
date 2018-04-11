# Euler discovered the remarkable quadratic formula:
# n2+n+41
# It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when n=40,402+40+41=40(40+1)+41 is divisible by 41,
# and certainly when n=41,412+41+41 is clearly divisible by 41.
# The incredible formula n2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.
# Considering quadratics of the form:
# n2+an+b, where |a|<1000 and |b|≤1000
# where |n| is the modulus/absolute value of n e.g. |11|=11 and |−4|=4

# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.
import math
import time
start_time = time.time()


def is_prime(x):  # simple primality test algorithm implemented
    if x <= 1:
        return False
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False

    y = 5
    while y*y <= x:  # check divisibility till the square root of the number
        if x % y == 0 or x % (y + 2) == 0:
            return False
        y += 6
    return True


def brute_force_approach():
    n_max = 0
    final_a = 0
    final_b = 0
    for a in range(-1000, 1001, 1):
        for b in range(-1000, 1001, 1):
            n = 0
            n_prev = n_max
            while is_prime((n*n)+(n*a)+b):
                n += 1
            if n_prev < n:
                n_max = n
                final_a = a
                final_b = b
    print("Product of coefficient:", final_a * final_b, "Value of a:", final_a, "Value of b:", final_b)


def shrink_approach():
    n_max = 0
    final_a = 0
    final_b = 0

    for a in range(-999, 1001, 2):
        for b in prime_numb_list():
            for temp in range(2):
                n = 0
                b_sign = 1 if temp == 0 else -1
                a_odd = -1 if b % 2 == 0 else 0
                while is_prime(n * n + (a + a_odd) * n + b_sign * b):
                    n += 1
                if n > n_max:
                    n_max = n
                    final_b = b
                    final_a = a

    print("Product of coefficient:", final_b * final_a, "Value of a:", final_a, "Value of b:", final_b)


def prime_numb_list():
    prime_list = []
    for numb in range(1, 1001):
        if is_prime(numb):
            prime_list.append(numb)
    return prime_list


brute_force_approach()
shrink_approach()

print("time elapsed: {:.2f}s".format(time.time() - start_time))
