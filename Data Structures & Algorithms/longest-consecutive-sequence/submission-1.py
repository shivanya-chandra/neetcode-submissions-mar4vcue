class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
            num_sets = set(nums)
            longest = 0

            for nums in num_sets:
                if nums - 1 not in num_sets:
                    current = nums
                    length = 1

                    while current + 1 in num_sets:
                        current= current + 1
                        length = length + 1

                    longest = max(length, longest)
            return longest
        