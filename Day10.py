'''You are given an array of strings strs[]. Your task is to group all the strings 
that are anagrams of each other. An anagram is a word or phrase formed by rearranging the letters of a 
different word or 100 phrase, typically using all the original letters exactly once. The goal is to return 
the grouped anagrams as a list of lists, where each sublist contains words that are anagrams of each other.

Example

Input: strs[] = ["eat", "tea", • "tan", "ate", "nat", "bat"]

Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]'''

def group_anagrams(strs):
    anagram_groups = {}
    
    for word in strs:
        # Sort the word to use as a key
        sorted_word = ''.join(sorted(word))
        
        # If the key is not in the dictionary, add it
        if sorted_word not in anagram_groups:
            anagram_groups[sorted_word] = []
        
        # Append the word to the corresponding group
        anagram_groups[sorted_word].append(word)
    
    # Return the grouped anagrams as a list of lists
    return list(anagram_groups.values())

# Example usage:
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(strs)
print(result)  

# Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]