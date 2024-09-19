'''You are given an array of strings strs[], consisting of lowercase letters. 
Your task is to find the longest common prefix shared among all the strings. If there is no ☑ common prefix, 
return an empty string " ".
A common prefix is a substring that appears at the beginning of od all the strings in the array.
The task is to identify the longest such prefix that all strings share.

Example

Input: ["flower", "flow", "flight"]

Output: "fl"
'''
def longest_common_prefix(strs):
    if not strs:
        return ""
    
    # Start by assuming the first string is the common prefix
    prefix = strs[0]
    
    for string in strs[1:]:
        # Compare the current prefix with each string and shorten the prefix if necessary
        while string[:len(prefix)] != prefix and prefix:
            prefix = prefix[:-1]
        # If there's no common prefix, return an empty string
        if not prefix:
            return ""
    
    return prefix

# Example usage:
strs = ["flower", "flow", "flight"]
result = longest_common_prefix(strs)
print(result)  # Output: "fl"