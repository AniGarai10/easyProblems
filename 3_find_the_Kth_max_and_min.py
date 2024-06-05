# Find the "Kth" max and min element of an array
def kthSmallest(arr, k):
    arr.sort()

    return arr[k - 1]

def kthLargest(arr, k):
    arr.sort()

    return arr[-k]


def sort_array(arr):
    # sort using Bubble sort
    for i in range(1, len(arr)):
        for j in range(len(arr)- i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def kthSmallest_s(arr, k):
    return sort_array(arr)[k - 1]

def kthLargest_s(arr, k):
    return sort_array(arr)[-k]


arr = [12, 3, 5, 7, 19]

print(kthSmallest(arr, 2))
print(kthLargest(arr, 2))

print(kthLargest_s(arr, k=3))
print(kthSmallest_s(arr, k=3))