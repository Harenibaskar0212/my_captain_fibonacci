
def fibonacci(n):
    fib_sequence = [0, 1]

    for _ in range(2, n):
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)

    return fib_sequence

# Get input from the user
n = int(input("Enter the number of Fibonacci numbers to generate: "))

# Generate and print Fibonacci numbers
result = fibonacci(n)
print("Fibonacci Sequence:", result)
