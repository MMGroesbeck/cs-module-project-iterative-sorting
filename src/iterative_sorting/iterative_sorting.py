def swap(arr, i1, i2):
    if i1 != i2:
        arr[i1], arr[i2] = arr[i2], arr[i1]

# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        # Your code here
        swap(arr, cur_index, smallest_index)
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    for i in range(len(arr) - 2):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                swap(arr, j, j+1)
    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here
    if len(arr) == 0:
        return arr
    count = []
    if maximum != None:
        for i in range(maximum + 1):
            count.append(0)
    for i in arr:
        if i < 0:
            return "Error, negative numbers not allowed in Count Sort"
        # Next part is needed because maximum is not always given:
        while (len(count) - 1) < i:
            count.append(0)
        count[i] += 1
    arr = []
    for j in range(len(count)):
        while count[j] > 0:
            arr.append(j)
            count[j] -= 1
    return arr
