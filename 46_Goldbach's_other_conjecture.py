# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2
# 21 = 3 + 2×3^2
# 25 = 7 + 2×3^2
# 27 = 19 + 2×2^2
# 33 = 31 + 2×1^2
# It turns out that the conjecture was false.
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
import math
prime_list = [2, 3]


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


def generate_prime_list():
    i = 5
    while i < 10000:
        if is_prime(i):
            prime_list.append(i)
        i += 1


def is_twice_sqr(temp_numb):
    temp_numb = math.sqrt(temp_numb / 2)
    if temp_numb.is_integer():
        return True
    return False


def check_goldbach_conjecture():
    generate_prime_list()
    global result
    result = 3
    notfound = True
    while notfound:
        j = 0
        notfound = False
        while result >= prime_list[j]:
            if is_twice_sqr(result - prime_list[j]):
                notfound = True
                break
            j += 1
        result += 2
    print("Final number", result-2)


check_goldbach_conjecture()
