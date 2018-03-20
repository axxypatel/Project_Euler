# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

total_sum = 0
numb = 1000
tot_mul = 1

for i in range(1, numb+1):
    tot_mul *= 2

tot_mul = str(tot_mul)
# print(tot_mul)
for j in range(0, len(tot_mul)):
    total_sum += int(tot_mul[j])

print("Total sum:", total_sum)

