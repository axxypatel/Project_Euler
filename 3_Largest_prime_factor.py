# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
# In Below code, I have used two approach to get the largest prime factor
number = 13195
number2= 600851475143
prime_list = []
prime_list2=[]

def isprime(x):
    status = False
    for y in range(2, x):
        if x % y == 0:
            status=False
            break
        else:
            status=True
    return status

for i in range(2, number): # Traditional approach to search the prime factor
    if number % i == 0:
        if isprime(i) == True:
            prime_list.append(i)

def check_prime(numb):    # New approach which is way faster than the usual one
    i=2
    while numb>1:
        if numb % i == 0:
            prime_list2.append(i)
            numb=int(numb/i)
            while True:
                if numb%i != 0:
                    break
                else:
                    numb=numb/i
                    prime_list2.append(i)
        i = i+1

check_prime(number2)
print(prime_list)
print(max(prime_list))
print(prime_list2)
print(max(prime_list2))
