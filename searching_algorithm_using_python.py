# Implement the python code for various searching algorithm

# Sequential search
sample_list2 = [4, 5, 6, 8, 9, 10, 28, 34, 77, 78, 81, 87, 89]


class SearchNumber:
    def __init__(self):
        self.sample_list = [4, 5, 6, 8, 9, 10, 28, 34, 77, 78, 81, 87, 89]
        self.search_numb = 78

    def sequential_search(self):                      # Basic sequential search algorithm
        for i in range(len(self.sample_list)):
            if self.sample_list[i] == self.search_numb:
                print("Number found", self.search_numb)
                return

    def binary_search(self):                          # Binary search algorithm using sorted input list
        first_pos = 0
        last_pos = len(self.sample_list) - 1

        while first_pos <= last_pos:
            midpoint = (first_pos + last_pos) // 2
            if self.sample_list[midpoint] == self.search_numb:
                print("Number found", self.search_numb)
                return
            elif self.sample_list[midpoint] < self.search_numb:
                first_pos = midpoint + 1
            else:
                last_pos = midpoint - 1
        else:
            if self.sample_list[last_pos] == self.search_numb:
                print("Number found", self.search_numb)
            else:
                print("Number not found")

    def binary_search_recursion(self, sample_list1):    # binary search algorithm using recursion
        midpoint = len(sample_list1) // 2
        if sample_list1[midpoint] == self.search_numb:
            print("Number found", self.search_numb)
            return
        else:
            if sample_list1[midpoint] < self.search_numb:
                self.binary_search_recursion(sample_list1[midpoint+1:])
            else:
                self.binary_search_recursion(sample_list1[:midpoint])


if __name__ == '__main__':
    seq_object = SearchNumber()
    seq_object.sequential_search()
    print("Sequential search completed")
    binary_object = SearchNumber()
    binary_object.binary_search()
    print("Binary search completed")
    binary_rec_object = SearchNumber()
    binary_rec_object.binary_search_recursion(sample_list2)
    print("Binary recursion search completed")
