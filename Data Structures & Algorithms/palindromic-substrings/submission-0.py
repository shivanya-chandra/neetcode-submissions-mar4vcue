class Solution:
    def countSubstrings(self, s: str) -> int:
        c = 0
        def checkP(l,r):
            count = 0
            while l>=0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -=1
                r +=1
            return count
        for i in range(len(s)):
            c += checkP(i,i) + checkP(i,i+1)
           
        return c




        # for i in range(len(s)):
        #     l,r=i,i
        #     while l>=0 and r < len(s) and s[l] == s[r]:
        #         l +=1
        #         r -=1
        #         return True
            
        #     l,r = i, i+1

        #     while l>=0 and r < len(s) and s[l] == s[r]:
        #         l +=1
        #         r -=1
        #         return True
        # return False
        