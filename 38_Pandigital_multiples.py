# Take the number 192 and multiply it by each of 1, 2, and 3:
# 192 × 1 = 192, 192 × 2 = 384, 192 × 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?


def check_pan_digital(final_numb):
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


def pan_multiples():
    final_pan_digital_numb = 0
    for i in range(9999, 8999, -1):
        final_pan_digital_numb = str(i) + str(i*2)
        if check_pan_digital(final_pan_digital_numb):
                break
    print("Highest number:", final_pan_digital_numb)


pan_multiples()
