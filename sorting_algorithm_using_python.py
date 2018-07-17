# Sorting algorithm using python
un_order_list = [5, 7, 1, 3, 2, 90, 45, 87, 23, 87, 65, 34, 78, 94, 88, 82, 10, 33, 54]
temp_list = [3, 4, 7, 1, 2]
# order_list = [1, 2, 3, 5, 7, 10, 23, 33, 34, 45, 54, 65, 78, 82, 87, 87, 88, 90, 94]


class SortingAlgorithms:
    def __init__(self):
        pass

    @staticmethod
    def bubble_sort(bubble_list):      # Most inefficient sorting algorithm [ O(n^2) complexity ]
        list_len = len(bubble_list)
        short_list_flag = True         # Implement this flag to make this algorithm more efficient(short bubble algorithm)
        while list_len > 0 and short_list_flag:
            short_list_flag = False
            for i in range(list_len - 1):
                if bubble_list[i] > bubble_list[i+1]:
                    short_list_flag = True
                    bubble_list[i], bubble_list[i+1] = bubble_list[i+1], bubble_list[i]  # simultaneous assignment can be done in python instead using temp variable to store the intermediate value
        print("Bubble sorted list is: ", bubble_list)

    @staticmethod
    def selection_sort(select_list):
        """
        Selection sort improve bubble sort by only one exchange for every pass through list [ O(n^2) complexity ]
        """
        list_len = len(select_list)

        while list_len > 0:
            max_position = 0
            for j in range(list_len):
                if select_list[j] > select_list[max_position]:
                    max_position = j
            select_list[max_position], select_list[list_len-1] = select_list[list_len-1], select_list[max_position]
            list_len -= 1
        print("Selection sorted list is:", select_list)

    @staticmethod
    def insertion_sort(insert_list):   # Insertion sort is having of O(n^2) complexity but works differently
        list_len = len(insert_list)
        for index in range(1, list_len):
            temp_var = index
            insert_value = insert_list[index]
            while temp_var > 0 and insert_list[temp_var-1] > insert_value:
                insert_list[temp_var] = insert_list[temp_var - 1]
                temp_var -= 1
            insert_list[temp_var] = insert_value    # Insert value at the position where new element fix as in sorted order
        print("Insertion sorted list is:", insert_list)

    def shell_sort(self, shell_sort):
        """
        Shell sort improves on insertion sort by breaking the list into smaller part,
        perform insertion sort on them and finally insertion sort on whole list again [ between O(n) and O(n^2) complexity ]
        """
        list_len = len(shell_sort) // 2

        def gap_insertion_sort(shell_sort, start, gap):
            current_value = 0
            position = 0
            for p in range(start+gap, len(shell_sort), gap):
                current_value = shell_sort[p]
                position = p
            while position >= gap and shell_sort[position-gap] > current_value:
                shell_sort[position] = shell_sort[position - gap]
                position -= gap
            shell_sort[position] = current_value

        while list_len > 0:
            for start_pos in range(list_len):
                gap_insertion_sort(shell_sort, start_pos, list_len)
            list_len //= 2

        self.insertion_sort(shell_sort)            # Final insertion sort on whole list

    @staticmethod
    def merge_sort(merge_list):
        """
        Merge sort is using divide and conquer strategy as a way to improve the performance of sorting algorithms.
        A merge sort is an O(nlogn) algorithm.
        """
        def merge_sort_temp(merge_list):
            if len(merge_list) > 1:
                mid_point = len(merge_list) // 2
                left_list = merge_list[:mid_point]
                right_list = merge_list[mid_point:]
                merge_sort_temp(left_list)
                merge_sort_temp(right_list)

                i, j, k = 0, 0, 0
                while i < len(left_list) and j < len(right_list):
                    if left_list[i] < right_list[j]:
                        merge_list[k] = left_list[i]
                        i += 1
                    else:
                        merge_list[k] = right_list[j]
                        j += 1
                    k += 1
                while i < len(left_list):
                    merge_list[k] = left_list[i]
                    i += 1
                    k += 1

                while j < len(right_list):
                    merge_list[k] = right_list[j]
                    j += 1
                    k += 1
        merge_sort_temp(merge_list)
        print("Merge sorted list is:", merge_list)

    @staticmethod
    def quick_sort(quick_list):
        """
        The quick sort uses divide and conquer to gain the same advantages as the merge sort, while not using additional storage.
        Time complexity is O(nlogn). In addition, there is no need for additional memory as in the merge sort process.
        """
        def quick_sort_support(quick_list, first, last):
            if first < last:
                print("1")
                split_point = quick_sort_recursion(quick_list, first, last)
                print("secnd call",quick_list, first, split_point-1)
                quick_sort_support(quick_list, first, split_point-1)
                print("third call")
                quick_sort_support(quick_list, split_point + 1, last)

        def quick_sort_recursion(quick_list, first, last):
            pivot_value = quick_list[first]
            left_mark = first + 1
            right_mark = last
            status = True
            while status:
                print("enter", pivot_value, quick_list[left_mark], quick_list[right_mark])
                while quick_list[left_mark] <= pivot_value and left_mark <= right_mark:
                    left_mark += 1
                    print("left", left_mark)
                while quick_list[right_mark] >= pivot_value and right_mark >= left_mark:
                    right_mark -= 1
                    print("right", right_mark)
                if right_mark < left_mark:
                    status = False
                else:
                    print("swap")
                    quick_list[right_mark], quick_list[left_mark] = quick_list[left_mark], quick_list[right_mark]

            quick_list[first], quick_list[right_mark] = quick_list[right_mark], quick_list[first]
            print(quick_list)
            return right_mark

        quick_sort_support(quick_list, 0, len(quick_list)-1)



sample_object = SortingAlgorithms()
# sample_object.bubble_sort(un_order_list)
# sample_object.selection_sort(un_order_list)
# sample_object.insertion_sort(un_order_list)
# sample_object.shell_sort(un_order_list)
# sample_object.merge_sort(un_order_list)
sample_object.quick_sort(temp_list)
