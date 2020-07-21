def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found

import math

# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    if len(arr) == 0:
        return -1
    min = 0
    max = len(arr) - 1
    while min != max:
        mid = math.floor((min + max)/2)
        if arr[mid] == target:
            return mid
        else:
            if arr[mid] < target:
                min = mid
            else:
                max = mid
    return -1  # not found
