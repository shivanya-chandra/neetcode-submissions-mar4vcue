import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
                
        def remove_punctuation_loop(text):
            return ''.join(char for char in text if char not in string.punctuation)

        c=remove_punctuation_loop(s).lower().replace(" ", "")
        return (c==c[::-1])
        
        