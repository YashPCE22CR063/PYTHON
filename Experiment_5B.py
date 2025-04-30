def sum_even_fibonacci(limit):
    a, b = 0, 1
    sum_even = 0

    while b <= limit:
        if b % 2 == 0:
            sum_even += b
        a, b = b, a + b  # Update to the next Fibonacci numbers

    return sum_even

# Set the limit to 4,000,000
limit = 4000000
print("Sum of even-valued Fibonacci numbers not exceeding", limit, "is:", sum_even_fibonacci(limit))

