# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28
# would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24.
# By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
# However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the
# sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
import math
import numpy
import time
start_time = time.time()
limit = 28124


def calculate_divisors(numb):
    temp_sum = 1
    srt_num = int(math.sqrt(numb))

    if srt_num * srt_num == numb:
        temp_sum += srt_num
        srt_num -= 1
    j = 2
    while j <= srt_num:
        if numb % j == 0:
            temp_sum += j + int(numb / j)
        j += 1
    return int(temp_sum)


def set_method_approach():
    all_numb = numpy.array([])    # numpy array are more efficient than list object of core python
    all_numb2 = set([])           # set is more effective in term of search operation than list object
    for k in range(2, limit):
        if k < calculate_divisors(k):
            all_numb = numpy.append(all_numb, k)
            all_numb2.update(all_numb+k)
    print(sum(set(range(limit)).difference(all_numb2)))


def set_method_approach2():     # fastest approach to get the sum
    total_sum = 1
    ans = set()
    for p in range(2, limit):
        if p < calculate_divisors(p):
            ans.add(p)
        for ab_num in ans:         # checking the abundant pair by doing subtraction of number to each elements available in set
            if p - ab_num in ans:  # don't sum the number if its subtraction with elements in set is available in set
                break
        else:
            total_sum += p


    print(total_sum)

#set_method_approach()
set_method_approach2()

print("time elapsed: {:.2f}s".format(time.time() - start_time))
