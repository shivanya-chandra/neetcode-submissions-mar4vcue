class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = 0
        left = 0
        right = 1
        d = {}
        left= 0 


        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] =1
            else:
                d[s[i]] +=1
            rep = i -left + 1- max(d.values())
    
            if(rep > k):
                d[s[left]] -=1
                left += 1
                
                count = max(count, i-left)
            elif(rep == k):
                count = max(count, i-left+1)
            else:
                count = max(count, i-left+1)

        return count
        