# Find the "Kth" max and min element of an array
def kthSmallest(arr, k):
    arr.sort()

    return arr[k - 1]

def kthLargest(arr, k):
    arr.sort()

    return arr[-k]


arr = [12, 3, 5, 7, 19]

print(kthSmallest(arr, 2))
print(kthLargest(arr, 2))