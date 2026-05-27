class Solution:
    def minWindow(self, s: str, t: str) -> str:
            tFreq = {}
            def hasAllChars(needFreq, windowFreq):
                for ch in needFreq:
                    if(windowFreq.get(ch, 0) < needFreq[ch]):
                        return False
                return True
            sFreq = {}
            left = 0
            best = ""
            if len(t) > len(s):
                return ""
            for j in range(len(t)):
                tFreq[t[j]] = tFreq.get(t[j], 0)+1

            for right in range(len(s)):
                sFreq[s[right]] = sFreq.get(s[right],0)+1

                while hasAllChars(tFreq, sFreq):
                    currWindow = s[left:right+1]

                    if(best == "" or len(currWindow) < len(best)):
                        best=currWindow
                    sFreq[s[left]] -=1
                
                    if(sFreq[s[left]] == 0):
                        sFreq.pop(s[left])
                    left +=1
            return best