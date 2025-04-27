# Basic implementation of Bubble sort
# arr = [7, 12, 9, 11, 3]
arr = [7, 14, 11, 8, 9]

n = len(arr)
for i in range(n - 1):

    for j in range(n - i - 1):

        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)


# Improved Implementation
# If the algorithm goes through the array one time without swapping any values, the array must be finished sorted, and we can stop the algorithm
imp_arr = [7, 3, 9, 12, 11]

x = len(imp_arr)
for i in range(x - 1):

    # swapped = False
    for j in range(x - i - 1):

        if imp_arr[j] > imp_arr[j+1]:
            imp_arr[j], imp_arr[j+1] = imp_arr[j+1], imp_arr[j]
            swapped = True

    if not swapped:
        break

print(f"Improved algo: {imp_arr}")
