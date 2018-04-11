# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
# 2000000
below_numb = 2000000


def is_prime(x):  # use simple primality test algorithm having O(sqrt(N)) time complexity

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


def calc_sum(below_numb1):
    total_sum = 0
    for i in range(2, below_numb1):
        if is_prime(i) is True:
            total_sum = total_sum + i

    return total_sum


total_sum1 = calc_sum(below_numb)
print("Sum:", total_sum1)
