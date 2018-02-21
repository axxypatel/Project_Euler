#The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385
#The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

till_numb = 100

def sum_sqr_numb(numb):
    sum=0
    for i in range(1,numb+1):
        sum = sum + (i*i)

    return sum

def sqr_sum_numb(numb):
    sum=0
    for i in range(1,numb+1):
        sum=sum+i
    return sum*sum


numb1=sum_sqr_numb(till_numb)
print(numb1)
numb2=sqr_sum_numb(till_numb)
print(numb2)

print(numb2-numb1)
