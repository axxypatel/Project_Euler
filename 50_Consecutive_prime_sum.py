# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

# Which prime, below one-million, can be written as the sum of the most consecutive primes? 1000000
import math
all_numb1 = [0]
upper_limit = 1000000


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
    total_sum = 0
    for temp in range(0, upper_limit):
        if is_prime(temp):
            total_sum += temp
            all_numb1.append(total_sum)


generate_prime_list()
max_length = 0
final_numb = 0
for i in range(0, len(all_numb1)):
    for j in range(i+1):
        temp_numb = all_numb1[i]-all_numb1[j]
        if temp_numb > upper_limit:
            break
        if is_prime(temp_numb):
            if i - j > max_length:
                max_length = i - j
                final_numb = temp_numb

print("Highest prime number:", final_numb)
