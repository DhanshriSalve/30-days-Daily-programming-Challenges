'''You are given an array arr containing n+1 integers,
where each integer is in the range [1, n] inclusive. There is exactly one duplicate number in the array,
but it 101 may appear more than once.Your task is to find the duplicate number without modifying the 
array and using constant extra space.

Example:1
arr = [3, 1, 3, 4, 2]
Output: 3
'''

def find_duplicate(arr):
    slow = arr[0]
    fast = arr[0]
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break

    slow = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
    return slow
arr = [3, 1, 3, 4, 2]
print(find_duplicate(arr))  