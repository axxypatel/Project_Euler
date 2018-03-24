# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order,
# but it also has a rather interesting sub-string divisibility property.
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.
from itertools import permutations
start_numb = "0123456789"
divide_list = [2, 3, 5, 7, 11, 13, 17]
all_numb = []


def check_pan_digital(final_numb):
    final_numb_len = len(final_numb)
    total_len = final_numb_len
    digit_list = []
    status = False
    final_numb = int(final_numb)

    while final_numb_len > 0:
        digit = final_numb % 10
        if digit in digit_list or digit > total_len:
            status = False
            break
        digit_list.append(digit)
        final_numb = int(final_numb / 10)
        final_numb_len -= 1
        status = True

    return status


for i in permutations(start_numb):
    temp_numb = ''.join(i)
    temp_status = True
    if check_pan_digital(temp_numb) is True:
        digit_place = 1
        temp = 0
        while temp < len(divide_list):
            if not int(temp_numb[digit_place] + temp_numb[digit_place+1] + temp_numb[digit_place+2]) % divide_list[temp] == 0:
                temp_status = False
                break
            digit_place += 1
            temp += 1

        if temp_status:
            all_numb.append(int(temp_numb))

print("Total sum:", sum(all_numb))
