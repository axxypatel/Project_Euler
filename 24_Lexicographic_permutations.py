# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
# If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
# The lexicographic permutations of 0, 1 and 2 are: 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
import itertools
import math
import time
start_time = time.time()

per_numb = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def permute_itertools_module():
    permute_data = list(itertools.permutations("0123456789"))[999999]  # Used itertools module to find the permutation
    print(''.join(permute_data))


def permute_brute_force_approach():
    total_cnt = 1
    while total_cnt <= 999999:
        lst_len = len(per_numb)
        org_len = lst_len - 1

        while per_numb[org_len - 1] >= per_numb[org_len]:
            org_len -= 1

        temp_len = lst_len
        while per_numb[temp_len-1] <= per_numb[org_len-1]:
            temp_len -= 1

        swap_numb(org_len-1, temp_len-1)

        org_len += 1
        temp_len = lst_len

        while org_len < temp_len:
            swap_numb(org_len-1, temp_len-1)
            org_len += 1
            temp_len -= 1

        total_cnt += 1
    print("Expected combination is:", ''.join(per_numb))


def swap_numb(x, y):
    temp = per_numb[x]
    per_numb[x] = per_numb[y]
    per_numb[y] = temp


def count_combination_approach():
    lst_len = len(per_numb)
    remain = 999999
    final_number = ""
    per_numb_temp = [i for i in range(10)]

    for i in range(1, lst_len):
        j = int(remain / math.factorial(lst_len-i))
        remain = remain % math.factorial(lst_len-i)
        final_number += str(per_numb_temp[j])
        per_numb_temp.remove(per_numb_temp[j])

        if remain == 0:
            final_number += "0"
            break
    print("Expected combination is:", final_number)


permute_itertools_module()          # python inbuilt library to get the combinations
permute_brute_force_approach()      # brute force approach
count_combination_approach()        # Fastest algorithm to get the expected value as per this problem

print("time elapsed: {:.2f}s".format(time.time() - start_time))
