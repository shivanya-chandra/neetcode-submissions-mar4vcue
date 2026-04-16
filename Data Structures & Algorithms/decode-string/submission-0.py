class Solution:
    def decodeString(self, s: str) -> str:
            chr = ""
            num = 0
            stack =[]


            for ch in s:
                if ch.isdigit():
                    num = num * 10 + int(ch)
                elif ch == "[":
                    stack.append((chr, num))
                    chr = ""
                    num = 0
                    
                elif ch == "]":
                    prev, n = stack.pop()
                    chr = prev + n * chr
            
                else:
                    chr += ch

            
                    

            return chr
        