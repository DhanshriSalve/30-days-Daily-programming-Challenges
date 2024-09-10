'''You are given an array arr consisting only of Os, 1s, and 2s.
The task is to sort the array in increasing order in linear time (i.e., O(n)) without using any extra space.

This means you need to rearrange the array in-place.

Example 1

arr = [0, 1, 2, 1, 0, 2, 1, 0] 
Output: [0, 0, 0, 1, 1, 1, 2, 2]'''


def sort_012(arr):
    low = 0
    mid = 0
    high = len(arr) - 1
    
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1
    
    return arr

arr = [0, 1, 2, 1, 0, 2, 1, 0]
print(sort_012(arr))