'''[11:19 AM, 9/16/2024] Dhanshri Salve: You are given an array height[] 
of non-negative integers where each element represents the height of a bar in a histogram-like structure. 
Your task is to calculate how much water can be trapped between the 100 bars after it rains.
Water is trapped between two bars when the shorter bar on either side forms a boundary, and the space
between them can hold water. Each unit of height between two bars can trap 1 unit of water.

Example

Input: [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

Output:6
 '''
 
def trap(height):
    left, right = 0, len(height) - 1
    left_max = right_max = water = 0
    while left < right:
        if height[left] < height[right]:
            left_max = max(left_max, height[left])
            water += left_max - height[left]
            left += 1
        else:
            right_max = max(right_max, height[right])
            water += right_max - height[right]
            right -= 1
    return water

# Example
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(height))  # Output: 6

