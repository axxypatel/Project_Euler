# The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include leading zeros.) 1000000
upper_limit = 1000000
all_numb = []


def is_palindrome(numb):
    check_numb = str(numb)
    status = False
    length_numb = len(check_numb)
    k = 1
    if int(numb) < 10:
        status = True

    while k <= int(length_numb // 2):
        if check_numb[k-1] == check_numb[length_numb-k]:
            status = True
        else:
            status = False
            break
        k += 1
    return status


for i in range(1, upper_limit):
    binary_status = is_palindrome(bin(i)[2:])
    numb_status = is_palindrome(i)

    if binary_status is True and numb_status is True:
        all_numb.append(i)

print("Total sum:", sum(all_numb))
