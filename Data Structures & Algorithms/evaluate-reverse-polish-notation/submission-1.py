import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul
        }

        for token in tokens:
            if token in "+-*/":
                b = stack.pop()
                a = stack.pop()

                if token == "/":
                    res = int(a / b)
                else:
                    res = ops[token](a, b)

                stack.append(res)
            else:
                stack.append(int(token))

        return stack[-1]
        