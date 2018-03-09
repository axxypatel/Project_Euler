# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
first_limit = 100
second_limit = 10000
all_numb = []


def check_pandigital(first, second, product):
    final_numb = str(first)+str(second)+str(product)
    final_numb_len = len(final_numb)
    digit_list = []
    status = False

    if final_numb_len == 9:
        final_numb = int(final_numb)

        while final_numb_len > 0:
            digit = final_numb % 10
            if digit in digit_list or digit == 0:
                status = False
                break
            digit_list.append(digit)
            final_numb = int(final_numb / 10)
            final_numb_len -= 1
            status = True

    return status


for i in range(1, first_limit):
    product_num = 1
    for j in range(first_limit, second_limit):
        product_num = i * j
        if check_pandigital(i, j, product_num):
            if product_num not in all_numb:
                all_numb.append(product_num)

print("Total sum for pandigital:", sum(all_numb))
