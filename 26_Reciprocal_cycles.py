# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
# 1/2	= 	0.5,1/3	= 	0.(3),1/4	= 	0.25,1/5	= 	0.2,1/6	= 	0.1(6),1/7	= 	0.(142857),1/8	= 	0.125,1/9	= 	0.(1),1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
d = 1
pre_quotient = ""
highest_quotient = ""
final_numb = 0

while d < 1000:
    divisor = 1
    remainder = []
    quotient = ""
    temp_remainder = 0
    pre_quotient = highest_quotient

    while True:
        if divisor != 1:
            divisor = temp_remainder * 10
            quotient += str(int(divisor/d))

        temp_remainder = divisor % d
        divisor = temp_remainder * 10

        if temp_remainder in remainder or temp_remainder == 0:
            break
        remainder.append(temp_remainder)

    if len(pre_quotient) <= len(quotient):
        highest_quotient = quotient
        final_numb = d

    d += 1

print("Final number is:", final_numb, "\nHighest Length:", len(highest_quotient))
