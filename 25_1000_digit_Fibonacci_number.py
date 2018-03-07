# The Fibonacci sequence is defined by the recurrence relation:
# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# The 12th term is 144, F12, is the first term to contain three digits.

# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

a, b = 1, 1
index = 2
while True:
    a, b = b, a+b
    index += 1
    if len(str(b)) == 1000:
        print("1000 digits term index is:", index)
        break

print("Program completed")
