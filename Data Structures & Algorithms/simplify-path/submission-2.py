class Solution:
    def simplifyPath(self, path: str) -> str:
        a = []
        st = path.split("/")
    
        n = ""

        for i in range(len(st)):
            if st[i] == "" or st[i] == ".":
                continue
            elif st[i] == "..":
                if len(a) >= 1:
                    a.pop()
            else:
                a.append(st[i])
        print(a)
        for i in a:
            n += "/" + i
        if(n == ""):
            return "/"
        else:
            return n
            