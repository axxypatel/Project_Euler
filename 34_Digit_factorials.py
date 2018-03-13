# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.
upper_limit = 2540160
all_fact = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
final_sum = 0

for i in range(3, upper_limit):
    temp = i
    total_sum = 0

    while temp > 0:
        last_digit = temp % 10
        temp = int(temp / 10)
        if last_digit != 0:
            total_sum += all_fact[last_digit-1]
        else:
            total_sum += 1

    if total_sum == i:
        final_sum += i

print("Total sum:", final_sum)
