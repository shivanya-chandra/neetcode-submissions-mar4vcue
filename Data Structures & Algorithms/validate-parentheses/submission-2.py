class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        flag = False
        for br in s:
            if stack and br == "}" and stack.pop() == "{":
                flag = True
            elif stack and br == "]" and stack.pop() == "[":
                flag =  True
            elif stack and br == ")" and stack.pop() == "(":
                flag = True
            else:
                stack.append(br)
        if stack != [] and flag: 
            flag = False
        return flag

        
        