class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
            temps = temperatures

            answer = [0] * len(temps)
            stack = []

            for i, t in enumerate(temps):
                while stack and stack[-1][0] < t:
                    stack_t, stack_i = stack.pop()
                    answer[stack_i]  = i-stack_i
                stack.append((t,i))
            return answer
        