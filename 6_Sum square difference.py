# The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

till_numb = 100


class SquareDiff:

    def __init__(self, till_numb1):
        self.numb = till_numb1

    def sum_sqr_numb(self):
        total_sum = 0
        for i in range(1, self.numb+1):
            total_sum = total_sum + (i*i)

        return total_sum

    def sqr_sum_numb(self):
        total_sum = 0
        for i in range(1, self.numb+1):
            total_sum = total_sum + i
        return total_sum * total_sum


sample_obj = SquareDiff(till_numb)
numb1 = sample_obj.sum_sqr_numb()
print(numb1)
numb2 = sample_obj.sqr_sum_numb()
print(numb2)
print(numb2-numb1)
