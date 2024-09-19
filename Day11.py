'''You are given a string s. Your task is to generate and return all possible permutations of the characters in the string. A permutation is a rearrangement of the characters in the string, and 100 each character must appear exactly 011 once in every permutation. If there are duplicate characters in the string, the resulting permutations should also be unique (i.e., no repeated permutations).

Example

Input: "abc"

Output: ["abc", "acb", "bac", "bca", "cab", "cba"]'''

def generate_permutations(s):
    if len(s) == 0:
        return []
    
    # If there's only one character, return it as the only permutation
    if len(s) == 1:
        return [s]
    
    # List to store all unique permutations
    permutations = []
    
    
    for i in range(len(s)):
        char = s[i]
        # Get the remaining characters after removing the current character
        remaining_chars = s[:i] + s[i+1:]
        
        # Generate permutations of the remaining characters
        for perm in generate_permutations(remaining_chars):
            # Add the current character to the front of each permutation
            permutations.append(char + perm)
    
    # Return only unique permutations by converting to a set and back to a list
    return list(set(permutations))

# Example usage:
s = "abc"
result = generate_permutations(s)
print(result)  

# Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']