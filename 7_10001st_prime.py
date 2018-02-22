#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10001st prime number?

prime_pos= 10001

def is_prime(numb):
    status = True
    for i in range(2,numb+1):
        if numb % i == 0 and numb != i:
            status= False
            break
        else:
            status = True
    return status

def check_cond(prime_pos):
    numb_position=0
    j=2
    while True:
        if is_prime(j) == True:
            numb_position += 1
            if numb_position == prime_pos:
                print("Position of the prine number:",numb_position,"\n","Prime Number:",j)
                break
        j+=1

check_cond(prime_pos)
