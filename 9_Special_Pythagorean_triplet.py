# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,a^2 + b^2 = c^2. For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.

import math
a=2
b=3
c=1

status=False
for i in range(1,999):
    for j in range(i+1,1000):
        sum=0
        c_sqr = (i * i) + (j*j)
        #print(c_sqr)
        if math.sqrt(c_sqr).is_integer() == False:
            continue
        else:
            sum = i + j+ int(math.sqrt(c_sqr))
            #print("Sum:",i,j,int(math.sqrt(c_sqr)),sum)
            if sum == 1000:
                status = True
                break
    if status == True:
        a,b,c = i,j,int(math.sqrt(c_sqr))
        #print(a*b*c)
        break

print("Sum and Product of a,c and c: ",a+b+c,a*b*c)


