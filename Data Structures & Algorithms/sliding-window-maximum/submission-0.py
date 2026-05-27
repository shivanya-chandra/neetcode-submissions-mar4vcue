class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
            maxi = []
            left = 0
            right = k
            while right < len(nums)+1:
                # print(left, right)
                # print(nums[left:right])
                # print(max(nums[left:right]))
                maxi.append(max(nums[left:right]))
                left += 1
                right+=1
            return maxi
        