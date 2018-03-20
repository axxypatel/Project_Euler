# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in compliance with British usage.


unit_digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
               'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens_digits = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
other_digit = ['hundred', 'thousand', 'and']
total_sum = 0

# nine hundred and ninety nine
for i in range(1, 1001):
    unit_place = i % 10
    tens_place = i // 10
    hnd_place = i // 100
    thou_place = i // 1000

    if i < 20:
        # print(unit_digits[i-1])
        total_sum += len(unit_digits[i - 1])
        # print(total_sum, end=' ')
    elif tens_place > 1 and hnd_place == 0:
        if unit_place == 0:
            # print(tens_digits[tens_place - 2])
            total_sum += len(tens_digits[tens_place - 2])
        else:
            # print(tens_digits[tens_place - 2],unit_digits[unit_place-1])
            total_sum += (len(tens_digits[tens_place - 2]) + len(unit_digits[unit_place-1]))
    elif hnd_place != 0:
        if i % 100 == 0 and thou_place != 1 and i / 100 > 0:
            temp = (i//100) - 1
            # print(unit_digits[temp], other_digit[0])
            total_sum += (len(unit_digits[temp]) + len(other_digit[0]))
        elif i % 1000 == 0:
            # print(unit_digits[0],other_digit[1])
            total_sum += (len(unit_digits[0]) + len(other_digit[1]))
        else:
            last_digit = i - (hnd_place * 100)
            if 0 < last_digit < 20:
                # print(unit_digits[hund_place-1],other_digit[0],other_digit[2],unit_digits[last_digit-1])
                total_sum += (len(unit_digits[hnd_place-1]) + len(other_digit[0]) + len(other_digit[2]) + len(unit_digits[last_digit-1]))
            else:
                unit_place = last_digit % 10
                tens_place = last_digit // 10
                # print(last_digit,unit_place,tens_place)
                if unit_place == 0:
                    # print(unit_digits[hund_place-1],other_digit[0],other_digit[2],tens_digits[tens_place-2])
                    total_sum += (len(unit_digits[hnd_place-1]) + len(other_digit[0]) + len(other_digit[2]) + len(tens_digits[tens_place-2]))
                else:
                    # print(unit_digits[hund_place-1],other_digit[0],other_digit[2],tens_digits[tens_place-2],unit_digits[unit_place-1])
                    total_sum += (len(unit_digits[hnd_place-1]) + len(other_digit[0]) + len(other_digit[2]) + len(tens_digits[tens_place-2]) + len(unit_digits[unit_place-1]))
    # print(i,sum)
print("Total sum:", total_sum)
