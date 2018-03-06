# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order.
# Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
# So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?

input_file = open("C:\\Users\\AKSHAY_PC\\Desktop\sample_input.txt", "r")

input_str = input_file.read()
input_str = input_str.replace('"', "")
sample_data = input_str.split(",")
data_length = len(sample_data)
sample_data = sorted(sample_data)

alphabet_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13 ,'N': 14, 'O': 15, 'P': 16, 'Q': 17,
                 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23,'X': 24, 'Y': 25, 'Z': 26}

total_sum = 0
for cnt, i in enumerate(sample_data):
    temp_sum = 0
    for j in range(len(i)):
        temp_sum += alphabet_dict.get(i[j])
    total_sum += (temp_sum * (cnt + 1))

print("Total Sum:", total_sum)
