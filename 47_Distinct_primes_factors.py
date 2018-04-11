# The first two consecutive numbers to have two distinct prime factors are:
# 14 = 2 × 7
# 15 = 3 × 5
# The first three consecutive numbers to have three distinct prime factors are:
# 644 = 2 × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.

# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
import math
numb = 2
final_list = []


def calculate_divisors(n):
    temp_n = n
    all_numb = set()
    cnt = 0

    while n % 2 == 0:
        cnt += 1
        all_numb.add(2)
        n = n / 2

    for j in range(3, int(math.sqrt(temp_n)), 2):
        cnt = 0
        while n % j == 0:
            cnt += 1
            all_numb.add(j)
            n /= j
    if n > 2:
        all_numb.add(int(n))

    return all_numb


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


def check_prime_list(prime_list):
    for k in prime_list:
        if not is_prime(k):
            return False
    return True


while True:
    temp_numb = list(calculate_divisors(numb))
    if len(temp_numb) == 4:
        if check_prime_list(temp_numb):
            final_list.append(numb)
        if len(final_list) == 4:
            print("first four consecutive integers are:", final_list)
            break
    else:
            final_list.clear()

    numb += 1
