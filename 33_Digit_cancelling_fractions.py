# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
# which is correct, is obtained by cancelling the 9s.
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
import numpy as np

a = 100
numerator_set = set()
denominator_set = set()
final_num = 1
final_den = 1


def check_prime(numb):    # New approach which is way faster than the usual one
    prime_list2 = []
    j = 2
    while numb > 1:
        if numb % j == 0:
            prime_list2.append(j)
            numb = int(numb/j)
            while True:
                if numb % j != 0:
                    break
                else:
                    numb = numb/j
                    prime_list2.append(j)
        j += 1
    return prime_list2


for numerator in range(11, a):
    for denominator in range(99, numerator, -1):
        numerator_set.clear()
        denominator_set.clear()
        temp_numerator = numerator
        temp_denominator = denominator

        for temp in range(0, 2):
            numerator_set.add(temp_numerator % 10)
            denominator_set.add(temp_denominator % 10)
            temp_numerator = int(temp_numerator / 10)
            temp_denominator = int(temp_denominator / 10)

        if not numerator_set.isdisjoint(denominator_set) and numerator % 10 != 0 and denominator % 10 != 0:
            temp = (numerator_set.intersection(denominator_set))
            match_value = temp.pop()
            numerator_set.remove(match_value)
            denominator_set.remove(match_value)

            if len(numerator_set) != 0 and len(denominator_set) != 0:
                num_value = numerator_set.pop()
                den_value = denominator_set.pop()
                if den_value != 0 and (numerator / denominator) == (num_value / den_value):
                    final_num *= numerator
                    final_den *= denominator

numerator_list = check_prime(final_num)
denominator_list = check_prime(final_den)
for value in numerator_list:
    denominator_list.remove(value)

print("Product of denominator is:", np.product(np.array(denominator_list)))
