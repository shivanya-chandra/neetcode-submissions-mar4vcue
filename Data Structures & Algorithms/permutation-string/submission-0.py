class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
            left = 0
            freq1 = {}
            freq2 = {}

            for i in range(len(s1)):
                freq2[s1[i]] = 1 + freq2.get(s1[i], 0)
            if len(s1) > len(s2):
                return False
            
            for right in range(len(s2)):
                freq1[s2[right]] = 1+freq1.get(s2[right], 0)

                while (right - left +1) > len(s1):
                    freq1[s2[left]] -= 1
                    if freq1[s2[left]] == 0:
                        del freq1[s2[left]]
                    left +=1
                if(freq1 == freq2):
                    return True
            return False
        