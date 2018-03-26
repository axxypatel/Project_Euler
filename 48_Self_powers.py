# The series, 11 + 22 + 33 + ... + 1010 = 10405071317.
# Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
upper_limit = 1000
temp = 1
total_sum = 0

while temp <= upper_limit:
    total_sum += (temp ** temp)
    temp += 1

total_sum = str(total_sum)
print(total_sum[-10:])
