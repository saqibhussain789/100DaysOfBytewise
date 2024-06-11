# Fibonacci Sequence
n = int(input("How many terms? "))
fib_sequence = [0, 1]

if n <= 0:
    print("Please enter a positive integer")
elif n == 1:
    print("Fibonacci sequence:")
    print(fib_sequence[0])
else:
    for i in range(2, n):
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)
    print("Fibonacci sequence:")
    print(' '.join(map(str, fib_sequence[:n])))
