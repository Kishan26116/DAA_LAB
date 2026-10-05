# 1) BUBBLE SORT

import time

# User Input
n = int(input("Enter number of elements: "))

arr = []

print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

# Start Time
start = time.time()

# Bubble Sort
for i in range(n - 1):
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

# End Time
end = time.time()

print("\nSorted Array:")
print(arr)

print("\nTime Complexity:")
print("Best Case    : O(n)")
print("Average Case : O(n^2)")
print("Worst Case   : O(n^2)")

print("Execution Time =", end - start, "seconds")

#2) SELECTION SORT

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

#3) INSERTION SORT

import time

# User Input
n = int(input("Enter number of elements: "))

arr = []

print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

# Start Time
start = time.time()

# Insertion Sort
for i in range(1, n):
    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key

# End Time
end = time.time()

print("\nSorted Array:")
print(arr)

print("\nTime Complexity:")
print("Best Case    : O(n)")
print("Average Case : O(n^2)")
print("Worst Case   : O(n^2)")

print("Execution Time =", end - start, "seconds")

#4) QUICK SORT

import time

def quick_sort(arr, low, high):
    if low < high:

        pivot = arr[low]
        i = low
        j = high

        while i < j:

            while i < high and arr[i] <= pivot:
                i += 1

            while arr[j] > pivot:
                j -= 1

            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        arr[low], arr[j] = arr[j], arr[low]

        quick_sort(arr, low, j - 1)
        quick_sort(arr, j + 1, high)

# User Input
n = int(input("Enter number of elements: "))

arr = []

print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

# Start Time
start = time.time()

quick_sort(arr, 0, n - 1)

# End Time
end = time.time()

print("\nSorted Array:")
print(arr)

print("\nTime Complexity:")
print("Best Case    : O(n log n)")
print("Average Case : O(n log n)")
print("Worst Case   : O(n^2)")

print("Execution Time =", end - start, "seconds")

#5) MERGE SORT

import time

def merge_sort(arr):
    if len(arr) > 1:

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# User Input
n = int(input("Enter number of elements: "))

arr = []

print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

# Start Time
start = time.time()

merge_sort(arr)

# End Time
end = time.time()

print("\nSorted Array:")
print(arr)

print("\nTime Complexity:")
print("Best Case    : O(n log n)")
print("Average Case : O(n log n)")
print("Worst Case   : O(n log n)")

print("Execution Time =", end - start, "seconds")