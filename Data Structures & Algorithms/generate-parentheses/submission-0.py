class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(open_count, close_count,cur):
            if close_count == n and open_count == n:
                res.append(cur)
                return
            
            # cur += "()"
            # dfs(i+1, cur)

            # cur removes () somehow
            # dfs(i+1, cur)
            if open_count < n:
                dfs(open_count + 1, close_count, cur+ "(")
            if cur and close_count< open_count:
                dfs(open_count, close_count+1, cur+")")

        dfs(0, 0,"")
        return res
        