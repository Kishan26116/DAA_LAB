#Implementation of making a change problem using dynamic programming


import time
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[amount] == float('inf'):
        return -1

    return dp[amount]

coins = list(map(int, input("Enter coin denominations separated by spaces: ").split()))
amount = int(input("Enter the amount: "))

start_time = time.perf_counter()

result = coin_change(coins, amount)

end_time = time.perf_counter()

execution_time = end_time - start_time

print("\n========== MAKING CHANGE PROBLEM ==========")

print("User Input - Coins:", coins)
print("User Input - Amount:", amount)

if result == -1:
    print("Amount cannot be formed using the given coins.")
else:
    print("Minimum number of coins required:", result)

print("Time Complexity: O(n × A)")
print("Space Complexity: O(A)")
print("Execution Time:", execution_time, "seconds")