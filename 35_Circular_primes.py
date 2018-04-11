# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million? 1000000
upper_limit = 1000000
all_numb = []


def is_prime(x):  # simple primality test algorithm implemented
    if x <= 1:
        return False
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False

    y = 5
    while y*y <= x:  # check divisibility till the square root of the number
        if x % y == 0 or x % (y + 2) == 0:
            return False
        y += 6
    return True


for i in range(2, upper_limit):
    if is_prime(i):
        temp_str = ""
        rotate_limit = len(str(i))
        temp = i
        numb_temp = []
        tot = rotate_limit

        if i < 10:
            all_numb.append(i)

        while rotate_limit > 0:
            numb_temp.append(temp % 10)
            temp = int(temp / 10)
            rotate_limit -= 1
        numb_temp.reverse()

        for j in range(1, tot):
            temp = j
            neg_index = tot
            tot1 = tot
            temp_str = ""
            while tot1 > 0:
                if temp < tot:
                    temp_str += str(numb_temp[temp])
                else:
                    temp_str += str(numb_temp[(-1 * neg_index)])
                    neg_index -= 1
                temp += 1
                tot1 -= 1
            if not is_prime(int(temp_str)):
                break
            if j == tot-1:
                all_numb.append(i)

print("Number of circular primes", len(all_numb))
