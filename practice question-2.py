# You are given an unsorted array of integers. Your task is to find the median of the array.
# The median is the middle value in an ordered list of numbers. If the list has an even number of elements,
# the median is 100 the average of the two middle numbers.



# Implement a function that returns the median of the array without explicitly sorting the entire array.

# Example 1:
# arr = [3, 2, 1, 4, 5]
# Output: 3

# Example 2:
# arr = [7, 10, 4, 3, 20, 15]
        
import random

def sortarr(arr, k):
    if len(arr) == 1:
        return arr[0]
    
    pivot = random.choice(arr)
    smallno= [el for el in arr if el < pivot]
    greater= [el for el in arr if el > pivot]
    equal= [el for el in arr if el == pivot]
    
    if k < len(smallno):
        return sortarr(smallno, k)
    elif k < len(smallno) + len(equal):
        return equal[0]
    else:
        return sortarr(greater, k - len(smallno) - len(equal))

def find_median(arr):
    n = len(arr)
    if n % 2 == 1:
        return sortarr(arr, n // 2)
    else:
        return (sortarr(arr, n // 2 - 1) + sortarr(arr, n // 2)) / 2
 
arr1 = [3, 2, 1, 4, 5]
print(find_median(arr1))  

arr2 = [7, 10, 4, 3, 20, 15]
print(find_median(arr2))          
