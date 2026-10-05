#1)Linear Search

import time

# User Input
n = int(input("Enter the number of elements: "))
arr = []

for i in range(n):
    value = int(input(f"Enter element at index {i}: "))
    arr.append(value)

key = int(input("Enter the element to search: "))

# Start Execution Time
start = time.perf_counter()

# Linear Search
index = -1

for i in range(n):
    if arr[i] == key:
        index = i
        break

# End Execution Time
end = time.perf_counter()

# Output
if index != -1:
    print("\nElement found at Index:", index)
else:
    print("\nElement not found.")

print(f"Execution Time: {end - start:.10f} seconds")
print("Time Complexity:")
print("Best Case    : O(1)")
print("Average Case : O(n)")
print("Worst Case   : O(n)")


#2)Binary Search

import time

# User Input
n = int(input("Enter the number of elements: "))
arr = []

for i in range(n):
    value = int(input(f"Enter element at index {i}: "))
    arr.append(value)

# Sort the array
arr.sort()
print("\nSorted Array:", arr)

key = int(input("Enter the element to search: "))

# Start Execution Time
start = time.perf_counter()

# Binary Search
low = 0
high = n - 1
index = -1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == key:
        index = mid
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

# End Execution Time
end = time.perf_counter()

# Output
if index != -1:
    print("\nElement found at Index:", index)
else:
    print("\nElement not found.")

print(f"Execution Time: {end - start:.10f} seconds")
print("Time Complexity:")
print("Best Case    : O(1)")
print("Average Case : O(log n)")
print("Worst Case   : O(log n)")