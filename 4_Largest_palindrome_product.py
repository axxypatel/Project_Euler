#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.


max_mult=999
max_numb=max_mult * max_mult
max_len=len(str(max_mult))
print(max_numb)


def ispalindrome(numb):
    check_numb=str(numb)
    status = False
    length_numb=len(check_numb)
    k=1
    while k <= int(length_numb // 2):
        if check_numb[k-1] == check_numb[length_numb-k]:
            status=True
        else:
            status=False
            break
        k += 1
    return status

if __name__ == "__main__":
    for i in range(max_numb,1,-1):
        status2 = False
        if ispalindrome(i) == True:
            for j in range(max_mult,1,-1):
                if i % j == 0:
                    mul1=str(j)
                    mul2=str(int(i/j))
                    if len(mul1) == max_len and len(mul2) == max_len:
                        print(i,j,int(i/j),"Biggest palindromic number")
                        status2= True
                        break
            if status2 == True: break
    print("Finish the program")


