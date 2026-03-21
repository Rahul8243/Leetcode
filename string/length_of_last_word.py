# 58. Length of Last Word
# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        print("Original string:", s)
        
        stripped = s.strip()
        print("After strip:", stripped)
        
        words = stripped.split(" ")
        print("Words list:", words)
        
        last_word = words[-1]
        print("Last word:", last_word)
        
        length = len(last_word)
        print("Length of last word:", length)
        
        return length