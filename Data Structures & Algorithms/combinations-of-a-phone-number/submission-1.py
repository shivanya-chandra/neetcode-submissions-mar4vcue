class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []

        def dfs(cur,i):
            if i >= len(digits):
                res.append(cur)
                return

            digit = digits[i]

            for ch in mapping[digit]:
                dfs( cur+ch,i+1)
            
        dfs("",0)
        return res