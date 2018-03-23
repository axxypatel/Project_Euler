# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value.
# For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words,
# how many are triangle words?
from math import sqrt
n_cnt = 0

alphabet_dictionary = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16,
                       'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

with open(r'C:\Users\AKSHAY_PC\Desktop\sample_input.txt', 'r') as input_file:
    file_string = input_file.read()  # use read() to extract the input file data in single string
    file_string = file_string.replace("\"", "")
    word_list = file_string.split(",")

    for temp in word_list:
        temp_len = len(temp)
        temp_sum = 0
        print(temp)
        while temp_len > 0:
            temp_sum += alphabet_dictionary[temp[temp_len-1]]
            temp_len -= 1
        delta_numb = 1 + (4 * 2 * temp_sum)
        if sqrt(delta_numb).is_integer():
            first_n = int((-1 + sqrt(delta_numb)) / 2)
            # second_n = int((-1 - sqrt(delta_numb)) / 2)   this solution will always be negative so no need to consider for this code
            n_cnt += 1

print("Total number of triangle number:", n_cnt)
