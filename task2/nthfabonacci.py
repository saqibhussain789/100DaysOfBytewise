# Nth Fibonacci Number
n = int(input("Enter the position of the Fibonacci number: "))

def fibonacci(n):
    if n <= 0:
        return "Invalid position"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return b

nth_fib = fibonacci(n)
print(f"The {n}th Fibonacci number is {nth_fib}")
