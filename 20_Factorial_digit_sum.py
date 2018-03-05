# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

total_mul = 1

for i in range(1, 101):
    total_mul = total_mul * i

# Used iterable in sum function
total_sum = sum([int(j) for j in str(total_mul)])

print("Total sum:", total_sum)
