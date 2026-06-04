class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
    
        i= 0
        j=0
        a = []
        median = 0

        while i< m and j < n:
            print(i,j)
            if(nums1[i] < nums2[j]):
                a.append(nums1[i])
                i += 1
            else:
                a.append(nums2[j])
                j+=1
        
        while j < n:
            a.append(nums2[j])
            j+=1
        while i < m:
            a.append(nums1[i])
            i+=1
        right = len(a) - 1
        left = 0

        mid = (left + right) // 2

        if(len(a)%2 ==0):
            median = (a[mid] + a[mid+1])/2
        else:
            median = a[mid]
        print(a)
        return median