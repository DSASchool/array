def selection_sort(arr):
    min = arr[0]
    n = len(arr)
    for i in range(n - 1):
        for j in range(i+1, n):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]


arr = [7, 12, 9, 11, 3]

print(f"Before sorting: {arr}")

selection_sort(arr)

print(f"After sorting: {arr}")
