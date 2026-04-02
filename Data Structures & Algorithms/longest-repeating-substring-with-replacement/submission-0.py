class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
            left = 0
            maxif = 0
            count = {}
            res = 0

            for right in range(len(s)):
                count[s[right]] = 1+ count.get(s[right], 0)
                maxif = max(maxif, count[s[right]])

                while(right-left + 1) -maxif > k:
                    count[s[left]] -=1
                    left+=1
                
                res  = max(res, right-left+1)
            return res
        