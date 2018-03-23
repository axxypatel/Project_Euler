# An irrational decimal fraction is created by concatenating the positive integers: 0.123456789101112131415161718192021...
# It can be seen that the 12th digit of the fractional part is 1.
# If dn represents the nth digit of the fractional part, find the value of the following expression.
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
max_length = 1000000
fraction_string = ""
str_length = len(fraction_string)
i = 1
multiplier = 1
final_numb = 1

while str_length < max_length:
    if multiplier <= str_length:
        final_numb *= int(fraction_string[multiplier-1])
        multiplier *= 10
    fraction_string += str(i)
    str_length = len(fraction_string)
    i += 1


print("Total multiplication:", final_numb)
