# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
# 1634 = 14 + 64 + 34 + 44, 8208 = 84 + 24 + 04 + 84, 9474 = 94 + 44 + 74 + 44, As 1 = 14 is not a sum it is not included.
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.

# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

all_numb = []
upper_limit = 355000
power = 5

for i in range(2, upper_limit):
    mul_value = 1
    temp = i
    total_sum = 0

    while int(temp/10) > 0:
        temp1 = temp % 10
        mul_value = 1
        for j in range(power):
            mul_value *= temp1
        total_sum += mul_value
        temp = int(temp/10)
    else:
        mul_value = 1
        for k in range(power):
            mul_value *= temp
        total_sum += mul_value

    if i == total_sum:
        all_numb.append(total_sum)

print(sum(all_numb))
