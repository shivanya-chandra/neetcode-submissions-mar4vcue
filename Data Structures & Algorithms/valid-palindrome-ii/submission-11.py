class Solution:
    def validPalindrome(self, s: str) -> bool:
        rev = s[::-1]
        if (s == rev):
            return True
        def isPalin(l,r):
            while l < r:
                if(s[l] != s[r]):
                    return False
                l+=1
                r-=1
            return True

        p1 = 0
        p2 = len(s) - 1

        while p1 <p2:
            if(s[p1] == s[p2]):
                p1 +=1
                p2 -=1
            else:
                return isPalin(p1+1, p2) or isPalin(p1, p2-1)