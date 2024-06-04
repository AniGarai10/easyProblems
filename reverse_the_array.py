# Reverse the array
def reverse_array(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

def rev_arr(arr):
    return arr[::-1]

arr = [1, 2, 3, 4, 5]

print(reverse_array(arr))

print(rev_arr(arr))