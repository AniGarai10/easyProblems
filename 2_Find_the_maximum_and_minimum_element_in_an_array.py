# Find the maximum and minimum element in an array

def min_arr(arr):
    min_ar = arr[0]
    for i in arr:
        if i < min_ar:
            min_ar = i

    return min_ar

def max_arr(arr):
    max_ar = arr[0]
    for i in arr:
        if i > max_ar:
            max_ar = i

    return max_ar


arr = [5, 2, 8, 3, 9]
print(min_arr(arr))
print(max_arr(arr))