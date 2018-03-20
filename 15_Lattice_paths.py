# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?
# Code implemented based on Combinatorics which is part of P&C theory


def normal_combination():
    mul1 = 1
    mul2 = 1

    for i in range(21, 41):
        # print(i, end=' ')
        mul1 = mul1 * i
    for j in range(1, 21):
        # print(j, end=' ')
        mul2 = mul2 * j

    return int(mul1/mul2)


print("Total Path:", normal_combination())
