class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
            s1Freq = {}
            s2Freq = {}
            left = 0
            right = len(s1)-1

            if len(s1) > len(s2):
                return False
            
            for i in range(len(s1)):
                s1Freq[s1[i]] = s1Freq.get(s1[i], 0)+1
                s2Freq[s2[i]] = s2Freq.get(s2[i], 0)+1
            for j in range(len(s1)-1, len(s2)):
                if s1Freq == s2Freq:
                    return True
                elif right<len(s2)-1:
                    s2Freq[s2[left]] -= 1

                    if s2Freq[s2[left]] == 0:
                        s2Freq.pop(s2[left])
                    right+=1
                    s2Freq[s2[right]] = s2Freq.get(s2[right], 0)+1
                    left+=1
            return False
