class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
            i = len(word1)
            j = len(word2)
            finalStr = ""

            if i<j:
                for k in range(i):
                    finalStr += word1[k] + word2[k]
                for m in range(i,j):
                    finalStr += word2[m]
            elif j<i:
                for k in range(j):
                    finalStr += word1[k] + word2[k]
                for m in range(j,i):
                    finalStr += word1[m]
            else:
                for k in range(i):
                    finalStr += word1[k] + word2[k]
            return finalStr
        