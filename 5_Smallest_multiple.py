# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
final_numb=1
for i in range (2,20):
    if final_numb % i == 0:
        continue
    numb = i

    while numb <=20:
        temp= numb
        numb = numb * i

    final_numb = final_numb* temp

print("final number",final_numb)
print("program completed")

