# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
import time
start_time = time.time()

max_mult = 999
max_numb = max_mult * max_mult


def is_palindrome(numb):
    check_numb = str(numb)
    status = False
    if check_numb == check_numb[::-1]:
        return True
    return status


if __name__ == "__main__":
    for i in range(max_numb, 10000, -1):
        status2 = False
        if is_palindrome(i) is True:
            j = max_mult
            while i//j <= max_mult:
                if i % j == 0:
                    print(i, j, int(i/j), "Biggest palindromic number")
                    status2 = True
                    break
                j -= 1
            if status2 is True:
                break
    print("Finish the program")

print("time elapsed: {:.2f}s".format(time.time() - start_time))
