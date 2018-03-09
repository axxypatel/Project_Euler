# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
'''
21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13
'''
# It can be verified that the sum of the numbers on the diagonals is 101.

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
import numpy as np
import time

start_time = time.time()
ary_size = 1001
sample_ip = np.array([0] * (ary_size * ary_size))
sample_ip = sample_ip.reshape(ary_size, ary_size)


def create_spiral_matrix():
    j = 0
    row_index = int(ary_size/2)
    col_index = row_index
    numb_cnt = 1

    while j < ary_size:
        if j == 0:
            sample_ip[row_index][col_index] = numb_cnt
            numb_cnt += 1
        else:
            sign = 1 if j % 2 != 0 else -1
            temp = 1

            while temp <= j * 2:
                if temp <= j:
                    col_index += 1 * sign
                    sample_ip[row_index][col_index] = numb_cnt
                    numb_cnt += 1
                else:
                    row_index += 1 * sign
                    sample_ip[row_index][col_index] = numb_cnt
                    numb_cnt += 1
                temp += 1

        if row_index == 0 and col_index == 0:
            j = 1
            while j < ary_size:
                col_index += 1
                sample_ip[row_index][col_index] = numb_cnt
                numb_cnt += 1
                j += 1

        j += 1
    print("Matrix:", "\n", sample_ip)


def matrix_diagonal_sum():
    diagonal_sum = 0
    mid_index = int(ary_size/2)
    for i in range(2):
        if i == 0:
            row_index = 0
            col_index = 0
            for j in range(ary_size):
                diagonal_sum += sample_ip[row_index+j][col_index+j]
        else:
            row_index = 0
            col_index = ary_size - 1
            for j in range(ary_size):
                diagonal_sum += sample_ip[row_index+j][col_index-j]
    diagonal_sum -= sample_ip[mid_index][mid_index]
    print("Total Sum:", diagonal_sum)


create_spiral_matrix()
matrix_diagonal_sum()

print("time elapsed: {:.2f}s".format(time.time() - start_time))

