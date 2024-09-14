'''You are given an integer array arr of size n. Your task is to find all the subarrays 
whose elements sum up to zero. A subarray is defined as a contiguous part on of the array,
and you must return the starting and ending indices of each subarray.

Example Input: [1, 2, -3, 3, -1, 2]

Output: [(0, 2), (1, 3)]'''

def find_zero_sum_subarrays(arr):
    result = []
    
    # Traverse through the array
    for i in range(len(arr)):
        current_sum = 0
        
        # Check every subarray starting from index i
        for j in range(i, len(arr)):
            current_sum += arr[j]
            
            # If the sum becomes 0, we found a subarray
            if current_sum == 0:
                result.append((i, j))
                
    return result

# Example usage
arr = [1, 2, -3, 3, -1, 2]
output = find_zero_sum_subarrays(arr)
print(output)