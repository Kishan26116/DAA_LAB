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