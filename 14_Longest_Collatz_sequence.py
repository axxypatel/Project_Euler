# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem),
# it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million. 1000000
import time
start_time = time.time()

numb = 1000000
chain_list = {}


def normal_approach():
    for i in range(numb-1, 1, -1):
        # print(i, end="-->")
        c = 1
        j = i
        while i > 1:
            if i % 2 == 0:
                i = i // 2
                # print(i,end="-->")
            else:
                i = 3*i + 1
                # print(i,end="-->")
            c += 1
        chain_list[j] = c

    return chain_list


# below function is used to calculate the longest chain by using memoization concept which is faster than normal approach
def memoization_approach():
    final_numb = 1
    chain_list[final_numb] = 1
    for j in range(final_numb, 1000000):
        c = 1
        k = j
        while j > 1:
            if j in chain_list.keys():
                c = c + (chain_list[j] - 1)
                break
            if j % 2 == 0:
                j = j // 2
                # print(j,end="-->")
            else:
                j = 3 * j + 1
                # print(j,end="-->")
            c += 1

        chain_list[k] = c

    return chain_list


# chain_list = normal_approach()
chain_list1 = memoization_approach()
max_chain_cnt = max(chain_list1.values())
print(list(chain_list1.keys())[list(chain_list1.values()).index(max_chain_cnt)], max_chain_cnt)
print("Program finished")

print("time elapsed: {:.2f}s".format(time.time() - start_time))
