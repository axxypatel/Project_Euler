# Implement the python code for various searching algorithm

# Sequential search
sample_list = [4, 5, 6, 8, 9, 10, 28, 34, 77, 78, 81, 87, 89]
search_numb = 78


def sequential_search():                      # Basic sequential search algorithm
    for i in range(len(sample_list)):
        if sample_list[i] == search_numb:
            print("Number found")
            return


def binary_search():                          # Binary search algorithm using sorted input list
    first_pos = 0
    last_pos = len(sample_list) - 1

    while first_pos <= last_pos:
        midpoint = (first_pos + last_pos) // 2
        if sample_list[midpoint] == search_numb:
            print("Number found", search_numb)
            return
        elif sample_list[midpoint] < search_numb:
            first_pos = midpoint + 1
        else:
            last_pos = midpoint - 1
    else:
        if sample_list[last_pos] == search_numb:
            print("Number found", search_numb)
        else:
            print("Number not found")


def binary_search_recursion(sample_list1):    # binary search algorithm using recursion
    midpoint = len(sample_list1) // 2
    if sample_list1[midpoint] == search_numb:
        print("Number found", search_numb)
        return
    else:
        if sample_list1[midpoint] < search_numb:
            binary_search_recursion(sample_list1[midpoint+1:])
        else:
            binary_search_recursion(sample_list1[:midpoint])


if __name__ == '__main__':
    # sequential_search()
    # binary_search(sample_list)
    binary_search_recursion(sample_list)
