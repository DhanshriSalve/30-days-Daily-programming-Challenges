'''You are given a string s that consists of multiple words separated by spaces.
Your task is to reverse the order of the words in the string. Words are defined as sequences of
non- space characters. The output 10 string should not contain leading or trailing spaces, 
and multiple spaces between words should be reduced to a single space.

Example

Input: "the sky is blue"

Output: "blue is sky the"'''

def reverse_words(s):
    words = s.split()  # Split the string into words
    reversed_words = words[::-1]  # Reverse the list of words
    return ' '.join(reversed_words)  # Join the words with a single space

# Example
s = "the sky is blue"
print(reverse_words(s))  # Output: "blue is sky the"