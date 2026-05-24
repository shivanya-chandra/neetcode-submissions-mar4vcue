class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        m = n- k

        temp = nums[m:]
        i = m -1 # to prevent index out of bounds

        while i >= 0:
            nums[i+k] = nums[i]
            i-=1

        i=0
        while i < k:
            nums[i] = temp[i]
            i+=1
        