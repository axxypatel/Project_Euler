# The following iterative sequence is defined for the set of positive integers:
#n → n/2 (n is even)
#n → 3n + 1 (n is odd)
#Using the rule above and starting with 13, we generate the following sequence:
#13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem),
# it is thought that all starting numbers finish at 1.
#Which starting number, under one million, produces the longest chain?
#NOTE: Once the chain starts the terms are allowed to go above one million.
#1000000

numb = 1000000

chain_list = {}

for i in range(numb-1, 1, -1):
    #print(i, end="-->")
    c = 1
    j = i
    while i > 1:
        #if i > 1000000: break
        if i % 2 == 0:
            i = i // 2
            #print(i,end="-->")
        else:
            i = 3*i + 1
            #print(i,end="-->")
        c += 1
    chain_list[j] = c


#print(chain_list)
max_chain_cnt = max(chain_list.values())
print(list(chain_list.keys()) [list(chain_list.values()).index(max_chain_cnt)],max_chain_cnt)
print("Program finished")
