# Factorial with Iteration method

import time

def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact


# User input
n = int(input("Enter a number: "))

# Measure execution time
start = time.perf_counter()

result = factorial(n)

end = time.perf_counter()

# Output
print("Factorial:", result)
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")
print("Execution Time:", end - start, "seconds")


# Factorial with Recursion method

import time

def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


# User input
n = int(input("Enter a number: "))

# Measure execution time
start = time.perf_counter()

result = factorial(n)

end = time.perf_counter()

# Output
print("Factorial:", result)
print("Time Complexity: O(n)")
print("Space Complexity: O(n)")
print("Execution Time:", end - start, "seconds")