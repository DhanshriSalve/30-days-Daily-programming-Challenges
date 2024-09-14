'''You are given an integer array arr of size n. An element is considered a leader 
if it is greater than all the elements to its right. Your task is to find all such leader elements in the array.

Example

Input:

arr = [16, 17, 4, 3, 5,2]

Output: Leaders: [17, 5, 2]'''

def find_leaders(arr):
    leaders = []
    max_from_right = arr[-1]
    leaders.append(max_from_right)

    for i in range(len(arr)-2, -1, -1):
        if arr[i] > max_from_right:
            leaders.append(arr[i])
            max_from_right = arr[i]
    
    leaders.reverse()
    return leaders

# Example usage
arr = [16, 17, 4, 3, 5, 2]
output = find_leaders(arr)
print("Leaders:", output)