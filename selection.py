import time

# User Input
n = int(input("Enter number of elements: "))

arr = []

print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

# Start Time
start = time.time()

# Selection Sort
for i in range(n - 1):
    min_index = i

    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j

    temp = arr[i]
    arr[i] = arr[min_index]
    arr[min_index] = temp

# End Time
end = time.time()

print("\nSorted Array:")
print(arr)

print("\nTime Complexity:")
print("Best Case    : O(n^2)")
print("Average Case : O(n^2)")
print("Worst Case   : O(n^2)")

print("Execution Time =", end - start, "seconds")