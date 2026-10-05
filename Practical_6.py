# Chain Matrix Multiplication

import time


def matrix_chain_order(p):
    n = len(p) - 1

    # Create DP table
    dp = [[0 for _ in range(n)] for _ in range(n)]

    # length is the chain length
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            dp[i][j] = float('inf')

            # Try every possible split
            for k in range(i, j):
                cost = (
                    dp[i][k]
                    + dp[k + 1][j]
                    + p[i] * p[k + 1] * p[j + 1]
                )

                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[0][n - 1]


# -------------------------------
# Taking user input
# -------------------------------

print("Matrix Chain Multiplication using Dynamic Programming")

n = int(input("Enter the number of matrices: "))

p = []

print("\nEnter the dimensions of the matrices.")

rows = int(input("Enter rows of Matrix 1: "))
cols = int(input("Enter columns of Matrix 1: "))

p.append(rows)
p.append(cols)

previous_cols = cols

for i in range(2, n + 1):
    rows = previous_cols
    cols = int(input(f"Enter columns of Matrix {i}: "))

    p.append(cols)
    previous_cols = cols


# -------------------------------
# Display matrix dimensions
# -------------------------------

print("\nMatrix dimensions:")

for i in range(n):
    print(f"Matrix {i + 1}: {p[i]} x {p[i + 1]}")


# -------------------------------
# Calculate minimum multiplication cost
# -------------------------------

start_time = time.perf_counter()

minimum_cost = matrix_chain_order(p)

end_time = time.perf_counter()

execution_time = end_time - start_time


# -------------------------------
# Display results
# -------------------------------

print("\nMinimum number of scalar multiplications:",
      minimum_cost)

print("Time Complexity: O(n^3)")

print("Space Complexity: O(n^2)")

print("Execution Time: {:.10f} seconds".format(execution_time))