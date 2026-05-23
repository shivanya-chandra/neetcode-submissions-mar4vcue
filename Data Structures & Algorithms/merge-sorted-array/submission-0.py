class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        i = m-1
        j = n-1
        l = len(nums1)-1
        while i >=0 and j >=0:
              
                if nums2[j] > nums1[i]:
                        nums1[l] = nums2[j]
                        l -=1
                        j -= 1
                elif nums1[i] > nums2[j]:
                        nums1[l] = nums1[i]
                        l-=1
                        i-=1
                elif nums1[i] == nums2[j]:
                        nums1[l] = nums2[j]
                        l-=1
                        j-=1
        while j>=0 and l>=0:
                nums1[l] = nums2[j]
                j-=1
                l-=1
        