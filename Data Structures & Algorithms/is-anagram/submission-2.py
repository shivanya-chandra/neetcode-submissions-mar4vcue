class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = []
        l2 = []

        for i in s:
            l1.append(ord(i))
        l1.sort()
        for j in t:
            l2.append(ord(j))
        l2.sort()
        if(l1==l2):
            return True
        return False