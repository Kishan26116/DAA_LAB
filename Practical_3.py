# Max Heap Sorting

import time

# Function to maintain Max Heap
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Check left child
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check right child
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not the root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # Recursively heapify the affected subtree
        heapify(arr, n, largest)


# Max Heap Sort function
def heap_sort(arr):
    n = len(arr)

    # Build Max Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


# User input
n = int(input("Enter number of elements: "))

arr = []

print("Enter the elements:")
for i in range(n):
    value = int(input(f"Element {i + 1}: "))
    arr.append(value)

print("\nOriginal array:", arr)

# Measure execution time
start_time = time.perf_counter()

heap_sort(arr)

end_time = time.perf_counter()

execution_time = end_time - start_time

print("Sorted array:", arr)
print("Time Complexity: O(n log n)")
print("Space Complexity: O(log n) due to recursion")
print(f"Execution Time: {execution_time:.8f} seconds")