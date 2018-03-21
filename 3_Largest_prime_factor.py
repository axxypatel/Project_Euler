# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
# In Below code, I have used two approach to get the largest prime factor


class PrimeFactorMethod:

    def __init__(self):
        self.number = 13195
        self.number2 = 600851475143
        self.prime_list = []
        self.prime_list2 = []

    def is_prime(self, x):  # simple primality test algorithm implemented
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

    def traditional_approach(self):
        for i in range(2, self.number):  # Traditional approach to search the prime factor
            if self.number % i == 0:
                if self.is_prime(i):
                    self.prime_list.append(i)

    def check_prime(self):    # New approach which is way faster than the usual one
        j = 2
        numb = self.number2
        while numb > 1:
            if numb % j == 0:
                self.prime_list2.append(j)
                numb = int(numb/j)
                while True:
                    if numb % j != 0:
                        break
                    else:
                        numb = numb/j
                        self.prime_list2.append(j)
            j += 1


sample_object = PrimeFactorMethod()
sample_object.traditional_approach()
sample_object.check_prime()

print(sample_object.prime_list)
print(max(sample_object.prime_list))
print(sample_object.prime_list2)
print(max(sample_object.prime_list2))
