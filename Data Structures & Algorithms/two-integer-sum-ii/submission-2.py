class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        final = []


        for i in range(len(numbers)):
            complement = target - numbers[i]
            print(complement)
            if complement in numbers and (complement != numbers[i]):
                seen[complement] = i+1

        return list(seen.values())