# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.
import math
import time
start_time = time.time()

all_numb = []


# Fast algorithm to find the divisors of number and add them
def calculate_divisors(n):
    j = 2
    total_sum = 1
    sqt_num = int(math.sqrt(n))
    # check if number is perfect square and if yes then execute below statements
    if n == sqt_num * sqt_num:
        total_sum += sqt_num
        sqt_num -= 1

    while j <= sqt_num:
        if n % j == 0:
            total_sum += j + (n / j)
        j += 1
    return int(total_sum)


for i in range(1, 10000):
    if i not in all_numb:
        first_sum = calculate_divisors(i)
        if first_sum != i:
            second_sum = calculate_divisors(first_sum)
            if i == second_sum:
                all_numb.append(i)
                all_numb.append(first_sum)
                # print(i,first_sum)

print("Total Sum:", sum(all_numb))

print("time elapsed: {:.2f}s".format(time.time() - start_time))
