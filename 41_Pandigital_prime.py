# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
# For example, 2143 is a 4-digit pandigital and is also prime.
# What is the largest n-digit pandigital prime that exists?
start_numb = 7654321
final_numb1 = 0


def check_pan_digital(final_numb):
    final_numb_len = len(final_numb)
    total_len = final_numb_len
    digit_list = []
    status = False
    final_numb = int(final_numb)
    while final_numb_len > 0:
        digit = final_numb % 10
        if digit in digit_list or digit == 0 or digit > total_len:
            status = False
            break
        digit_list.append(digit)
        final_numb = int(final_numb / 10)
        final_numb_len -= 1
        status = True

    return status


def is_prime(x):  # simple primality test algorithm implemented
        import math
        if x <= 1:
            return False
        if x == 2 or x == 3:
            return True
        if x % 2 == 0 or x % 3 == 0:
            return False

        y = 5
        sqt_numb = int(math.sqrt(x))

        while y <= sqt_numb:  # check divisibility till the square root of the number
            if x % y == 0:
                return False
            y += 2
        return True


while start_numb > 999:
    if len(str(start_numb)) in [6]:
        print(start_numb)
        start_numb = 4321
        continue
    else:
        if check_pan_digital(str(start_numb)) is True:
            if is_prime(start_numb) is True:
                print("Highest pandigital prime number is:", start_numb)
                final_numb1 = start_numb
                break
        start_numb -= 2
