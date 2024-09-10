'''You are given an array arr containing n-1 distinct integers. 
The array consists of integers taken from the range 1 ton, meaning one integer is missing from this sequence.
Your task is to find the missing integer.

Example

arr = [1, 2, 4, 5]

Output: 3
In python code'''


def find_missing_number(arr, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    missing_number = expected_sum - actual_sum
    return missing_number

arr = [1, 2, 4, 5]
n = 5
print(find_missing_number(arr, n))  
