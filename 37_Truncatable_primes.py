# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right,
# and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
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


numb = 11
cnt = 1

while cnt < 12:

    if is_prime(numb):
        numb_len = len(str(numb))
        numb_list = []
        temp_numb = numb

        while temp_numb > 0:
            numb_list.append(int(temp_numb % 10))
            temp_numb = int(temp_numb/10)
        numb_list.reverse()
        prime_left_check = True
        prime_right_check = True
        for j in range(0, 2):

            if j == 0:
                for k in range(0, numb_len):
                    str1 = ""
                    for char in numb_list[0:k+1]:
                        str1 += str(char)
                    temp_num2 = int(str1)
                    if not is_prime(temp_num2):
                        prime_right_check = False
                if prime_right_check is False:
                    break
            else:
                for k in range(0, numb_len):
                    str1 = ""
                    for char in numb_list[k:numb_len]:
                        str1 += str(char)
                    temp_num2 = int(str1)
                    if not is_prime(temp_num2):
                        prime_left_check = False
                if prime_left_check is False:
                    break
        if prime_left_check is True and prime_right_check is True:
            all_numb.append(numb)
            cnt += 1

    numb += 1

print(sum(all_numb))
